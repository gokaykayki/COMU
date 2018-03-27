import sys

list1 = []
liste1_size = 10

for i in range(liste1_size):
    print("List: {}".format(list1))
    print("current size of object list: {}".format(sys.getsizeof(list1)))
    print("adding {}\n".format(i))
    list1.append(i)

print("List: {}".format(list1))
print("current size of object list: {} ".format(sys.getsizeof(list1)))
