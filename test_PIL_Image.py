from PIL import Image

# img = Image.open('1.tif')  #打开图像
# 2.通道的合并与分离
# r,g,b,a = img.split()   # 分离成RGB三个通道。。提取R G B分量
# print(img.split())
# pic = Image.merge('RGB',(r,g,b))  # 合并通道
# pic.save("./img.tif")
# pic1=Image.merge("RGB",(a,a,a))
# pic1.save("./img1.tif")



def addTransparency(img, factor=0.7):
    img = img.convert('RGBA')
    img_blender = Image.new('RGBA', img.size, (0, 0, 0, 0))
    img = Image.blend(img_blender, img, factor)
    return img


img = Image.open("matilda2.0001.png")
img = addTransparency(img, factor=0.7)
r,g,b,a = img.split()   # 分离成RGB三个通道。。提取R G B分量
print(img.split())
pic = Image.merge('RGB',(r,g,b))  # 合并通道
pic.save("./img_RGB.tif")
pic1=Image.merge("RGB",(a,a,a))
pic1.save("./img_alpha.tif")

