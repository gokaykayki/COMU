import numpy as np
import matplotlib.pyplot as plt

test = plt.imread("test.jpg")

plt.imshow(test)
plt.show()

matrix = [[0,-1],[1,0]]

bw = np.zeros((test.shape[0]*2, test.shape[1]*2), dtype=np.uint8)

threshold = 120
for i in range(0,100):
    for j in range(0,100):
        n = test[i,j,0]/3 + test[i,j,1]/3 + test[i,j,2]/3
        if n > threshold:
            bw[i+100,j+100] = 0
        else:
            bw[i+100,j+100] = 255
        bw[i,j] = bw[j+100, i+100]



for i in range(0,100):
    for j in range(0,100):
        bw[i,j] = bw[j+100, i+100]


plt.imshow(bw, plt.cm.binary)
plt.show()
