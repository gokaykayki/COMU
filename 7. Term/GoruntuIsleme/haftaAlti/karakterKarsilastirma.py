
# coding: utf-8

# In[28]:

import matplotlib.pyplot as plt
import numpy as np

aList = []

img1 = plt.imread("a1.jpg")
img1.ndim, img1.shape
img2 = plt.imread("a2.jpg")
img2.ndim, img2.shape
img3 = plt.imread("a3.jpg")
img3.ndim, img3.shape
img4 = plt.imread("a4.jpg")
img4.ndim, img4.shape
img5 = plt.imread("a5.jpg")
img5.ndim, img5.shape
img6 = np.zeros(img1.shape[0:2])
img6.shape
threshold = 120

aList.append(img1)
aList.append(img2)
aList.append(img3)
aList.append(img4)
aList.append(img5)

for k in aList:
    for i in range(k.shape[0]):
        for j in range(k.shape[1]):
            n = k[i,j,0]/3 + k[i,j,1]/3 + k[i,j,2]/3
            if n > threshold:
                k[i,j] = 255
            else:
                k[i,j] = 0

plt.subplot(1,5,1), plt.imshow(aList[0])
plt.subplot(1,5,2), plt.imshow(aList[1])
plt.subplot(1,5,3), plt.imshow(aList[2])
plt.subplot(1,5,4), plt.imshow(aList[3])
plt.subplot(1,5,5), plt.imshow(aList[4])
plt.show()

aList[0].shape
myArray = np.array(aList[0],np.int32).reshape(1,30810) #hata
print(myArray)


# Eksik 

