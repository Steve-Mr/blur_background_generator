from PIL import Image, ImageFilter, ImageEnhance
import os
import argparse

def process_image(img_path, width, height):
    # Step 1: Read the image
    img = Image.open(img_path)

    # Step 2: Apply Gaussian blur to the image
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=64))  # You can adjust the blur radius as needed

    # Step 3: Resize the image while maintaining the aspect ratio and zoomed fill effect
    img_ratio = img.width / img.height
    target_ratio = width / height

    if img_ratio >= target_ratio:
                # Height is covering the target area, calculate the width
        new_width = int(height * img_ratio)
        resized_img = blurred_img.resize((new_width, height), Image.LANCZOS)
        x_offset = (new_width - width) // 2
        cropped_img = resized_img.crop((x_offset, 0, x_offset + width, height))
    else:

                # Width is covering the target area, calculate the height
        new_height = int(width / img_ratio)
        resized_img = blurred_img.resize((width, new_height), Image.LANCZOS)
        y_offset = (new_height - height) // 2
        cropped_img = resized_img.crop((0, y_offset, width, y_offset + height))

    # Step 4: Return the processed image
    return cropped_img
    
def process_and_overlay_image(img_path, width, height):
    # Step 1: Get the background image
    background = process_image(img_path, width, height)

    # Step 2: Increase contrast of the background image
    enhanced_background = ImageEnhance.Contrast(background).enhance(0.5)  # You can adjust the enhancement factor as needed

    # Step 3: Read the image to overlay
    overlay_img = Image.open(img_path)

    # Step 4: Place the overlay image onto the enhanced background using center zoom effect
    img_ratio = overlay_img.width / overlay_img.height
    target_ratio = width / height

    if img_ratio >= target_ratio:
        # Width is covering the target area, calculate the height
        new_height = int(width / img_ratio)
        print(new_height)
        resized_overlay = overlay_img.resize((width, new_height), Image.LANCZOS)
        y_offset = abs(new_height - height) // 2
        print(y_offset)
        enhanced_background.paste(resized_overlay, (0, y_offset))
    else:
        # Height is covering the target area, calculate the width
        new_width = int(height * img_ratio)
        resized_overlay = overlay_img.resize((new_width, height), Image.LANCZOS)
        x_offset = (new_width - width) // 2
        enhanced_background.paste(resized_overlay, (x_offset, 0))

    # Step 5: Return the resulting image
    return enhanced_background


class ImageProcessor:
    def __init__(self):
        # Create the argument parser
        self.parser = argparse.ArgumentParser(description="Process and overlay images with center zoom effect.")
        self.parser.add_argument("--image_path", required=True, help="Path to the image file.")
        self.parser.add_argument("--width", type=int, required=True, help="Desired width for the output image.")
        self.parser.add_argument("--height", type=int, required=True, help="Desired height for the output image.")
        self.parser.add_argument("--inplace", action="store_true", help="Replace the original image with the processed result.")

    def parse_args(self):
        # Parse the command-line arguments
        args = self.parser.parse_args()

        return args

    def process_image(self, img_path, width, height, inplace=False):
        # Call the process_and_overlay_image function to get the resulting image
        processed_img = process_and_overlay_image(img_path, width, height)

        # Determine the output path based on the "inplace" parameter
        if inplace:
            output_path = img_path
        else:
            # Create an "outputs" folder in the same directory as the input image
            output_folder = os.path.join(os.path.dirname(img_path), "outputs")
            os.makedirs(output_folder, exist_ok=True)

            # Use the same filename as the original, but prepend "processed_"
            output_filename = "processed_" + os.path.basename(img_path)
            output_path = os.path.join(output_folder, output_filename)

        # Save or replace the resulting image
        processed_img.save(output_path)

if __name__ == "__main__":
    processor = ImageProcessor()
    args = processor.parse_args()
    processor.process_image(args.image_path, args.width, args.height, args.inplace)


# # Test code
# if __name__ == "__main__":
#     img_path = "/home/maary/Pictures/Wallpapers/test.jpg"  # Replace with the actual path to your image
#     width = 1080
#     height = 2400
#     processed_img = process_and_overlay_image(img_path, width, height)
#     processed_img.show()  # Display the processed image

