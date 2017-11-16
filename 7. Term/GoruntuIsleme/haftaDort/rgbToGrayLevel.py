import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread("test.jpeg")
img_1.ndim,img_1.shape
plt.imshow(img_1)

pixel_1=[0,0,0]
pixel_1_gray_level=0

pixel_1=[10,0,0]
pixel_1_gray_level=10

pixel_1_rgb=[10,10,10]
pixel_1_gray_level=12
   
def convertRGBPixelToGrayLevel(RGB_Pixel):
   return RGB_Pixel[0]/3+RGB_Pixel[1]/3+RGB_Pixel[2]/3

def convertRGB_to_GrayLevel(image_1):
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_1.shape[0]):
        for j in range(img_2.shape[1]):
            img_2[i,j]=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3
convertRGBPixelToGrayLevel([2,5,7])
img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
img_2.shape

for i in range(img_1.shape[0]):
    for j in range(img_2.shape[1]):
        img_2[i,j]=convertRGBPixelToGrayLevel(img_1[i,j,:])
plt.subplot(1,2,1)
plt.imshow(img_1)
plt.subplot(1,2,2)
plt.imshow(img_2,cmap='gray')
plt.show()
