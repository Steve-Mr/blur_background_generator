# 模糊背景生成器 - 说明文档

模糊背景生成器 是一个用 Python 编写的工具，用于增强图像并实现类似于 "zoomed fill" 效果，特别适用于图片比例不理想的情况。它会对图像进行模糊和降低对比度的处理，从而生成一个背景，并保留原始图像的中心内容，实现 "zoomed fill" 效果。该工具特别适用于制作壁纸或其他艺术效果。

## 使用方法

1. **安装**： 在运行模糊背景生成器之前，请确保已安装 Python 3.x，并使用以下命令安装所需的依赖项：  
`pip install Pillow`

2. **命令行执行**： 要使用 "zoomed fill" 效果处理图像，请运行以下命令：
`python your_script.py --image_path "图片路径.jpg" --width 800 --height 600 [--inplace]`
`--image_path`：输入图像文件的路径。请将 "图片路径.jpg" 替换为实际的图像文件路径。  
`--width`：输出图像的期望宽度。以像素为单位指定所需宽度。  
`--height`：输出图像的期望高度。以像素为单位指定所需高度。  
`--inplace`：可选参数。如果提供该参数，则会替换原始图像为处理后的结果。如果不提供该参数，则处理后的图像将保存在图像目录下的 outputs 文件夹中。  
`--radius`: 可选参数。背景的模糊半径，默认值 16。  
`--zoom`: 可选参数。中心图像的缩放比例，默认值 1.0。  
`--background_contrast`: 可选参数。背景的对比度，默认值 0.5。  

## 演示效果

以下是用于演示效果的图像示例：

![](/asset/demo.png)

- 原图像： [图片链接](https://www.pixiv.net/artworks/106033605) (作者：rraluse)
- 处理命令：
`python3 generate_blur_background.py --image_path test.jpg --width 1080 --height 2400`

![](/asset/demo2.png)

- 原图像： [图片链接](https://www.pixiv.net/artworks/101409902) (作者：sz)
- 处理命令：
`python3 generate_blur_background.py --image_path test.jpg --width 1080 --height 2400 --radius 32 --zoom 0.8 --background_contrast 0.8`

## 致谢

模糊背景生成器主要编写工作由 OpenAI 创建的 ChatGPT 完成，其是一种先进的语言模型，用于辅助自然语言处理并为开发该图像处理工具提供指导。

## 免责声明

请注意，模糊背景生成器是按原样提供的，开发者不能保证其适用于特定用途。用户应负责获取图像处理活动的适当权限，并负责负责任地使用该工具。

有关 ChatGPT 和其他基于人工智能的语言模型的更多信息，请访问 [OpenAI 官网](https://openai.com/)。
