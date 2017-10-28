
# coding: utf-8

# In[5]:

import numpy as np
import matplotlib.pyplot as plt
im1=[[1,0],[0,0]]
im2=[[0,1],[0,0]]
im3=[[0,0],[1,0]]
im4=[[0,0],[0,1]]
em1=[[0,1],[1,1]]
em2=[[1,0],[1,1]]
em3=[[1,1],[0,1]]
em4=[[1,1],[1,0]]
im1 = [im1, im2, im3, im4]
em1 = [em1, em2, em3, em4]

img1 = plt.imread("t.jpg")
img1
plt.imshow(img1, plt.cm.binary)
plt.show()
img1.ndim
img1.shape

def count_internal_mask(image):
    counter_internal = 0
    for mask in im1:
        counter_internal = counter_internal + count_mask(image, mask)
    return counter_internal
def count_external_mask(image):
    counter_external = 0
    for mask in em1:
        counter_external = counter_external + count_mask(image, mask)
    return counter_external
def count_mask(image, mask):
    counter = 0
    m = img1.shape[0]
    n = img1.shape[1]
    for i in range(m-1):
        for j in range(n-1):
            a = b = c = d = False
            if(img1[i,j][0] == mask[0][0]):
                a = True
            if (img1[i,j+1][0] == mask[0][1]):
                b = True
            if (img1[i+1,j][0] == mask[1][0]):
                c = True
            if (img1[i+1,j+1][0] == mask[1][1]):
                d = True
            if (a and b and c and d):
                counter = counter + 1
    return counter

c1 = count_internal_mask(img1)
c2 = count_external_mask(img1)

c1, c2


# In[ ]:



