class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

for i in range(5):
    print("Adding item to queue: {}".format(i))
    q.enqueue(i)

print("\nIs queue empty ? {}".format(q.isEmpty()))
print("Size of queue: {}\n".format(q.size()))

for i in range(q.size()):
    print("Removing item from queue: {}".format(i))
q.dequeue()
