# Blur Background Generator - README

[中文版说明文档](README_CN.md)

The Blur Background Generator is a Python tool that enhances images with a zoomed fill effect, particularly when the image's proportions are non-ideal. It applies blur and contrast reduction to the image to create a background, preserving the central content of the original image and achieving a zoomed fill effect. This tool is particularly useful for creating wallpapers or other aesthetic enhancements.

## Usage

1. **Installation**: Before running the Blur Background Generator, ensure you have Python 3.x installed and install the necessary dependencies using the following command:  
`pip install Pillow`

2. **Command-line Execution**: To process an image with the zoomed fill effect, run the following command:
`python your_script.py --image_path "path/to/image.jpg" --width 800 --height 600 [--inplace]`  
`--image_path`: Path to the input image file. Replace "path/to/image.jpg" with the actual image file path.    
`--width`: Desired width for the output image. Specify the desired width in pixels.    
`--height`: Desired height for the output image. Specify the desired height in pixels.    
`--inplace`: Optional. If provided, the original image will be replaced with the processed result. If not provided, the processed image will be saved in the outputs folder within the image's directory.  
`--radius`: Optional. The blur radius of background. Default = 16  
`--zoom`: Optional. Zoom level of overlay image. Default = 1.0  
`--background_contrast`: Optional. Contrast of background. Default = 0.5  

## Demo

Below is an example of the image used for demonstration:

![](/asset/demo.png)

- Original Image: [Image Link](https://www.pixiv.net/artworks/106033605) (Artist: rraluse)
- Command Used:
`python3 generate_blur_background.py --image_path test.jpg --width 1080 --height 2400`

![](/asset/demo2.png)

- Original Image: [Image Link](https://www.pixiv.net/artworks/101409902) (Artist：sz)
- Command Used：
`python3 generate_blur_background.py --image_path test.jpg --width 1080 --height 2400 --radius 32 --zoom 0.8 --background_contrast 0.8`

## Acknowledgements

The primary development of the Blur Background Generator was completed by ChatGPT, an advanced language model created by OpenAI, to assist with natural language processing and provide guidance in developing this image processing tool.

## Disclaimer

Please note that the Blur Background Generator is provided as-is, and the developers cannot guarantee its suitability for specific use cases. Users are responsible for obtaining proper permissions for image processing activities and using the tool responsibly.

For more information about ChatGPT and other AI-powered language models, visit [OpenAI's website](https://openai.com/).
