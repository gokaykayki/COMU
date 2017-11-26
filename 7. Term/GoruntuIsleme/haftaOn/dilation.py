# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def defineMask():
    mask = [[1,1,1],[1,1,1],[1,1,1]]
    return mask

def myDilation(img1, mask):
    m = img1.shape[0]
    n = img1.shape[1]
    img2 = np.random.randint(0,1,(img1.shape[0],img1.shape[1]))
    for i in range(1,m-1):
        for j in range(1,n-1):
            x1 = img1[i,j] and mask[1][1]  #center

            x2 = img1[i-1,j-1] and mask[0][0] #scan
            x3 = img1[i-1,j] and mask[0][1]
            x4 = img1[i-1,j+1] and mask[0][2]

            x5 = img1[i,j-1] and mask[1][0]
            x6 = img1[i,j+1] and mask[1][2]

            x7 = img1[i+1,j-1] and mask[2][0]
            x8 = img1[i+1,j] and mask[2][1]
            x9 = img1[i+1,j+1] and mask[2][2]

            result1 = x1 or x2 or x3 or x4 or x5
            result2 = x6 or x7 or x8 or x9

            result = result1 or result2

            img2[i,j] = result

    return img2


test = plt.imread("test.jpg")
bw = np.zeros(test.shape[0:2])

threshold = 120
for i in range(test.shape[0]):
    for j in range(test.shape[1]):
        n = test[i,j,0]/3 + test[i,j,1]/3 + test[i,j,2]/3
        if n > threshold:
            bw[i,j] = 0
        else:
            bw[i,j] = 255

dilated = myDilation(bw,defineMask()) # print dilated image
plt.imshow(test) #default image
plt.show()

plt.imshow(bw, plt.cm.binary) #bw image
plt.show()

plt.imshow(dilated, plt.cm.binary) #dilated image
plt.show()

# plt.subplot(1,3,1), plt.imshow(test)
# plt.subplot(1,3,2), plt.imshow(bw, plt.cm.binary) #bw image
# plt.subplot(1,3,3), plt.imshow(dilated, plt.cm.binary) #dilated image
# plt.show()
