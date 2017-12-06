
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import numpy as np

class MyMatrix():
    def __init__(self, _d, _f):
        self.D = _d
        self.f = _f

def rgbToBW(img, threshold = 120):
    bw = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(sum(img[i,j,:])/3 > threshold):
                bw[i,j] = 1
            else:
                bw[i,j] = 0
    return bw
    
def createDF(img):
    d = set()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == 1:
                d.add((i,j))
    f = {}
    for i,j in d:
        f[(i,j)] = 1
    return MyMatrix(d,f)

img1 = plt.imread('test3.jpg')
bwImg = rgbToBW(img1)
sparseImg = createDF(bwImg)

plt.subplot(1,2,1), plt.imshow(img1)
plt.subplot(1,2,2), plt.imshow(bwImg, plt.cm.binary)
plt.show()


# In[24]:


print(list(sparseImg.D)[0]) # sparse matris d 0. eleman
print(str(sparseImg.f[list(sparseImg.D)[0]])) # sparse matris f 0. eleman

