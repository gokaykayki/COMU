# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

def rgbToGrayLevel(img):
    img3 = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
                img3[i,j] = sum(img[i,j,:])/3
    return img3

def redIntensity(img): #rgb - 012
    img2 = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i,j,0]+50 > 255):
                img2[i,j,0] = 255
            else:
                img2[i,j,0] = img[i,j,0]+50
            img2[i,j,1] = img[i,j,1]
            img2[i,j,2] = img[i,j,2]
    return img2

def grayLevelIntensity(img): #255'e yaklaştıkça beyazlaşır
    img4 = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i,j]-75 < 0):
                img4[i,j] = 0
            else:
                img4[i,j] = img[i,j] - 75
    return img4

img1 = plt.imread('test4.jpg')
redIntensityImg = redIntensity(img1)
grayLevelImg = rgbToGrayLevel(img1)
grayLevelIntensityImg = grayLevelIntensity(grayLevelImg)

plt.imshow(img1)
plt.show()

plt.imshow(redIntensityImg)
plt.show()  

plt.imshow(grayLevelImg, plt.cm.gray)
plt.show()  

plt.imshow(grayLevelIntensityImg, plt.cm.gray)
plt.show()

