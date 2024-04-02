from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import os
import argparse

def generate_background(img_path, width, height, radius):
    # Step 1: Read the image
    img = Image.open(img_path)

    # Step 2: Apply Gaussian blur to the image
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius))  # You can adjust the blur radius as needed

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
    return img, cropped_img
    
def process_and_overlay_image(img_path, width, height, radius, zoom, contrast):
    # Step 1: Get the background image
    overlay_img, background = generate_background(img_path, width, height, radius)

    # Step 2: Increase contrast of the background image
    enhanced_background = ImageEnhance.Contrast(background).enhance(contrast)  # You can adjust the enhancement factor as needed

    # Step 4: Place the overlay image onto the enhanced background using center zoom effect
    img_ratio = overlay_img.width / overlay_img.height
    target_ratio = width / height

    if img_ratio >= target_ratio:
        # Width is covering the target area, calculate the height
        new_width = int(width * zoom)
        new_height = int(width / img_ratio * zoom)
        resized_overlay = overlay_img.resize((new_width, new_height), Image.LANCZOS)
        x_offset = abs(new_width - width) // 2
        y_offset = abs(new_height - height) // 2
    else:
        # Height is covering the target area, calculate the width
        new_width = int(height * img_ratio * zoom)
        new_height = int(height * zoom)
        resized_overlay = overlay_img.resize((new_width, new_height), Image.LANCZOS)
        x_offset = abs(new_width - width) // 2
        y_offset = abs(new_height - height) // 2

    # 将阴影添加到 resized_overlay 上
    offset = min(x_offset, y_offset)
    if offset == 0: offset = 32
    
    shadowed_overlay = add_shadow(resized_overlay, offset=offset)
    final_width, final_height = shadowed_overlay.size
    x_offset = (width - final_width) // 2
    y_offset = (height - final_height) // 2
    
    enhanced_background.convert('RGBA')
    mask = shadowed_overlay.split()[3]  # 获取 alpha 通道作为掩码
    

    # 粘贴带阴影的 resized_overlay 到 enhanced_background 中
    enhanced_background.paste(shadowed_overlay, (x_offset, y_offset), mask=mask)

    # Step 5: Return the resulting image
    return enhanced_background


def add_shadow(image, offset=32):
    # 获取原始图片尺寸
    width, height = image.size
    
    # 创建新的背景图片
    background = Image.new("RGBA", (width + offset * 2, height + offset * 2), color="white")
    image.convert('RGBA')
        
    # 创建绘图对象
    draw = ImageDraw.Draw(background)

    b_width, b_height = background.size

    for i in range(offset):
        alpha = int(255 * (2 ** i / 2 ** offset))  # 根据当前距离计算透明度
        shadow_color = (0, 0, 0, alpha)
        draw.rectangle([i, i, b_width - i, b_height - i], fill = shadow_color)

    background = background.filter(ImageFilter.GaussianBlur(8))
    background.paste(image, (offset, offset))

    return background


class ImageProcessor:
    def __init__(self):
        # Create the argument parser
        self.parser = argparse.ArgumentParser(description="Process and overlay images with center zoom effect.")
        self.parser.add_argument("--image_path", required=True, help="Path to the image file.")
        self.parser.add_argument("--width", type=int, required=True, help="Desired width for the output image.")
        self.parser.add_argument("--height", type=int, required=True, help="Desired height for the output image.")
        self.parser.add_argument("--inplace", default=False, action="store_true", help="Replace the original image with the processed result.")
        self.parser.add_argument("--radius", type=int, default=16, help="Set the blur radius of background. Default = 16")
        self.parser.add_argument("--zoom", type=float, default=1.0, help="Set the zoom level of overlay image. Default = 1.0")
        self.parser.add_argument("--background_contrast", type=float, default=0.5, help="Set the contrast of background. Default = 0.5")

    def parse_args(self):
        # Parse the command-line arguments
        args = self.parser.parse_args()

        return args

    def process_image(self, img_path, width, height, inplace, radius, zoom, contrast):
        # Call the process_and_overlay_image function to get the resulting image
        processed_img = process_and_overlay_image(img_path, width, height, radius, zoom, contrast)

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
    processor.process_image(args.image_path, args.width, args.height, args.inplace, args.radius, args.zoom, args.background_contrast)


