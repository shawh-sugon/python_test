# import cv2   #导入模块，opencv的python模块叫cv2
#
#
#
# imgobj = cv2.imread('Camera0010000.TGA') #读取图像
# print (imgobj)
# cv2.namedWindow("image") #创建窗口并显示的是图像类型
# cv2.imshow("image",imgobj)
# cv2.waitKey(0)        #等待事件触发，参数0表示永久等待
# cv2.destroyAllWindows()   #释放窗口
# print(imgobj)
# c_img=cv2.split(imgobj) # 拆分通道cv2.split(img)
# r,g,b=cv2.split(imgobj) # 拆分通道
# print(c_img)
# if len(c_img)==3:
#     r,g,b = cv2.split(imgobj)
# elif len(c_img)==4:
#     r,g,b,a = cv2.split(imgobj)
# rgb_img = cv2.merge((r,g,b))
# cv2.imshow('Merge', rgb_img)
#
# cv2.namedWindow("image") #创建窗口并显示的是图像类型
# cv2.imshow("image",imgobj)
# cv2.waitKey(0)        #等待事件触发，参数0表示永久等待
# cv2.destroyAllWindows()   #释放窗口


import cv2
import numpy as np

# 加载图像
from PIL import Image

temp_hdr = "matilda2_RGB.hdr"
img_read = cv2.imread('matilda2.exr', cv2.IMREAD_UNCHANGED)
cv2.imwrite(temp_hdr, img_read)

img_hdr = cv2.imread(temp_hdr,cv2.IMREAD_UNCHANGED)

b,g,r = cv2.split(img_hdr)
img_RGB = cv2.merge((b,g,r))
print(temp_hdr.split(".")[:-1][0])
cv2.imwrite(temp_hdr.split(".")[:-1][0]+".tif",img_RGB)


# img_hdr = cv2.imread('matilda2.hdr', cv2.IMREAD_UNCHANGED)
# img_tif = cv2.imwrite("matilda2.tif",img_hdr)

# img=cv2.imread('matilda2.exr')
# img_read = cv2.imread(img_input_file, cv2.IMREAD_UNCHANGED)
# img=cv2.imread('matilda2.exr',cv2.IMREAD_UNCHANGED)
# temp_exr=cv2.imread(temp_exr, cv2.IMREAD_UNCHANGED)

# img = Image.open(temp_exr)  #打开图像
# # r,g,b = cv2.split(temp_exr)  #图像的拆分，将彩色图像划分为三种颜色
# r,g,b,a = img.split(temp_exr)
# pic = Image.merge('RGB',(r,g,b))  # 合并通道
# pic.save("./img.tif")
# pic1=Image.merge("RGB",(a,a,a))
# pic1.save("./img1.tif")
#
# print("R:",r)
# print("G:",g)
# print("B:",b)

# img_red = np.zeros(img.shape, np.uint8)
# # cv2.imwrite('cv_red.tif', img23)
# def get_red(img):   # 红
#     redImg = img[:,:,2]
#     return redImg
#
# def get_green(img): # 绿
#     greenImg = img[:,:,1]
#     return greenImg
#
# def get_blue(img):  # 蓝
#     blueImg = img[:,:,0]
#     return blueImg
# b = get_blue(img)
# g = get_green(img)
# r = get_red(img)

# img23 = cv2.merge([r,g,b])  #将三种颜色通道的图片融合
# cv2.imwrite('cv_img.tif', img23)
# cv2.imwrite("cv_r.tif",r)
# cv2.imwrite("cv_g.tif",g)
# cv2.imwrite("cv_b.tif",b)
