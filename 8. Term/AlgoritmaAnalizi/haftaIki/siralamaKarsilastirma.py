import random
def bubbleSort(arr):
    bubbleSortCounter = 0;
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            bubbleSortCounter+=1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Bubble sort karşılaştırma sayısı {}".format(bubbleSortCounter))


def insertionSort(arr):
    insertionSortCounter = 0;
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        insertionSortCounter += 1
        while j >=0 and key < arr[j] :
            insertionSortCounter += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print("Insertion sort karşılaştırma sayısı {}".format(insertionSortCounter))
    
def createRandomArray(length):
    tempArray = []
    for i in range(length):
        tempArray.append(random.randint(0,100))
    return tempArray

nLengths = [10,20,30,50]
for i in nLengths:
    print ("############### n = {}".format(i))
    for j in range(3):
        print("--- {}. deneme".format(j+1))
        insertionSort(createRandomArray(i))
        bubbleSort(createRandomArray(i))
       