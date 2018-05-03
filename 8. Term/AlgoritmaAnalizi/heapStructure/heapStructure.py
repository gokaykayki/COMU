from math import ceil
class Heap:

    DefaultCapacity = 10
    DefaultNumberOfChildren = 5

    def __init__(self, capacity = DefaultCapacity, maxHeap = True , numOfChildren = DefaultNumberOfChildren):
        self.size = 0
        self.capacity = capacity
        self.maxHeap = maxHeap
        self.data = [None]*capacity
        self.maxChildren = numOfChildren

    def __str__(self):
        if self.maxHeap:
            sortOfHeap = "Max Heap"
        else:
            sortOfHeap = "Min Heap"
        text = "It is a {}".format(sortOfHeap)
        return text

    def addToHeap(self, new):
        if self.capacity == self.size :
            print("Heap full. Doubling current capacity to {}".format(self.capacity*2))
            self.capacity *= 2
            temp = self.data
            self.data = [None]*self.capacity
            self.data[:len(temp)] = temp

        self.data[self.size] = int(new)
        self.move_up(self.size)
        self.size += 1


    def bestChild(self, index, lastIndex):
        if self.size < index or self.capacity < (index * 2) + 2:
            return
        if self.maxHeap:
            if self.data[(index * 2 ) + 1] is None or self.data[(index * 2 ) + 2] is None:
                return self.data[(index * 2 ) + 1]
            else:
                if self.data[(index * 2) + 1] > self.data[(index * 2 ) + 2]:
                    return self.data[(index * 2) + 1]
                else:
                    self.data[(index * 2) + 2]
        else:
            if self.data[(index * 2) + 1] is None or self.data[(index * 2) + 2] is None:
                return self.data[(index * 2) + 1]
            else:
                if self.data[(index * 2) + 1] < self.data[(index * 2 ) + 2]:
                    return self.data[(index * 2) + 1]
                else:
                    self.data[(index * 2) + 2]

    def removeTop(self):
        self.data[0] = self.data[self.size -1]
        self.data[self.size - 1] = None
        self.size -= 1
        self.move_down(0)

    def move_down(self, index):
        if (index*2) + 1 > self.size or self.data[(index*2)+2] is None and self.data[(index*2)+1] is None:
            return

        if self.data[(index*2)+2] is None:
            if self.data[(index*2)+1] > self.data[index]:
                self.data[(index * 2) + 2], self.data[index] = self.data[index], self.data[(index*2)+2]
        else:
            if max(self.data[(index*2)+2], self.data[(index*2)+1]) < self.data[index]:
                return
            else:
                if self.data[(index*2)+2] > self.data[(index*2)+1]:
                    self.data[(index * 2) + 2], self.data[index] = self.data[index], self.data[(index*2)+2]
                else:
                    self.data[(index * 2) + 1], self.data[index] = self.data[index], self.data[(index * 2) + 1]

        index = index * 2 + 1
        self.move_down(index)

    def move_up(self, index):
        if index <= 0:
            return
        if self.maxHeap:
            if self.data[ceil(index / 2) - 1] < self.data[index]:
                self.data[index], self.data[ceil(index / 2) - 1] = self.data[ceil(index / 2) - 1], self.data[index]

        else:
            if self.data[ceil(index / 2) - 1] > self.data[index]:
                self.data[index], self.data[ceil(index / 2) - 1] = self.data[ceil(index / 2) - 1], self.data[index]
        index = ceil(index/2)-1
        if index > 0:
            self.move_up(index)
        else:
            return


h = Heap()

h.addToHeap(70)
h.addToHeap(20)
h.addToHeap(30)
h.addToHeap(10)
h.addToHeap(5)
h.addToHeap(15)
h.addToHeap(58)
h.addToHeap(590)
print(h.data)
h.removeTop()
print("Removed element from heap")

print(h.data)

print("Best child of 5th element : {}".format(h.bestChild(5,10)))



