import math
import numpy as np
def myDistance(a, b):
    myPoint1 = a
    myPoint2 = b
    a = (myPoint1[0]-myPoint2[0])**2
    b = (myPoint1[1]-myPoint2[1])**2
    return math.sqrt(a+b)

def findCenter(ListOfPoints):
    a=0
    b=0 
    length = len(ListOfPoints)
    for point in ListOfPoints:
        a = a + point[0]
        b = b + point[1]
    return [a/length,b/length]

myPoint1 = [0,0]
myPoint2 = [1,0]
myPoint3 = [0,1]
myPoint4 = [1,1]

pointList = []

pointList.append(myPoint1)
pointList.append(myPoint2)
pointList.append(myPoint3)
pointList.append(myPoint4)

myDistance(myPoint2,myPoint3)

findCenter(pointList)

myArray = np.array([[1,2,3],[2,6,9]],np.int32)
myArray.ndim, myArray.shape
myArray1 = myArray.reshape(1,6)
print(myArray)
print("")
print(myArray1)

