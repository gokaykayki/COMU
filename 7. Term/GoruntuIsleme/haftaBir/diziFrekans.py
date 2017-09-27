from random import randint
from scipy.stats import itemfreq

array = []

length = input("Eleman sayısını giriniz: ")
minimum = input("En düşük değeri giriniz: ")
maximum = input("En yüksek değeri giriniz: ")

for i in range(0, int(length)):
	array.append(randint(int(minimum), int(maximum)))

array.sort()
print("Oluşturulan dizi(sıralı)\n-----------------")
print(array)
print("Frekans\n-----------------")
print(itemfreq(array))
