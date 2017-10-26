import matplotlib.pyplot as plt
import numpy as np
img1 = plt.imread("image.jpg")
img1.ndim
img1.shape
img2 = img1[1:575:2, 1:1024:2]
img2.ndim
img2.shape
plt.imshow(img2)
plt.show()
img3 = np.zeros(img2.shape[0:2])
img3.shape
img4 = np.zeros(img2.shape[0:2])
img4.shape
threshold = 120
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        n = img2[i,j,0]/3 + img2[i,j,1]/3 + img2[i,j,2]/3
        img3[i,j] = n
        if n > threshold:
            img4[i,j] = 255
        else:
            img4[i,j] = 0
plt.subplot(1,4,1), plt.imshow(img2)
plt.subplot(1,4,2), plt.imshow(img3, plt.cm.gray)
plt.subplot(1,4,3), plt.imshow(img4, plt.cm.gray)
plt.subplot(1,4,4), plt.imshow(img4, plt.cm.binary)
plt.show()