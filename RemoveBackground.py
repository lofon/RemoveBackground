# 一键抠图
from rembg import remove 
from PIL import Image
# 这里用本机图片所在的目录代替
imgPath='/Users/lofone/Desktop/VSCODE/VsPython/ImageProcessing/img/'
# 输入图像
input_img = imgPath+'feifei.jpg'
# 输出图像, 默认和输入图像路径相同
output_img = imgPath+'feifei.png'
inp = Image.open(input_img)
output = remove(inp)
output. save (output_img)
