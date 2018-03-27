import time
import matplotlib.pyplot as plt

x = []  ## grafik x ekseni
y = []  ## grafik y ekseni
def fiboRec(n):  ##  n. fibonacci sayısını buluyor
        if(n<2):
            return n
        else:
            return fibo(n-1)+fibo(n-2)
        
def loopForRec(n):    ## 0-n arasıdaki fibonacci elemanlarını sıra sıra buluyor
    for i in range(0,n):
        startTime = time.time() ## başlama zamanı
        fiboRec(i)
        finishTime = time.time() ## bitirme zamanı
        processTime = finishTime - startTime ## bulma süresi
        print (i+1, " için:\n ----------------------")
        print ("Başlama zamani: ", startTime)
        print ("Bitirme zamani: ", finishTime)
        print ("İşlem süresi: ", processTime, " saniye")
        x.append(i) ## grafik x eksenine fibonacci sayısının indeksini ekliyor
        y.append(processTime)  ## grafik y eksenine bulma süresini ekliyor
    plt.plot(x,y) ## grafik oluşturuyor
    plt.show() ## grafiği gösteriyor
    
    
def fiboLoop(n): ##  n. fibonacci sayısını buluyor
    a=0
    b=1
    c=a+b
    if(n<2):
        return n
    while(n>0):
        a=b
        b=c
        c=a+b
        n=n-1
    return c
def loopForLoop(n): ## 0-n arasıdaki fibonacci elemanlarını sıra sıra buluyor
    for i in range(n):
        startTime = time.time()
        print(fiboLoop(i))
        finishTime = time.time()
        processTime = finishTime - startTime
        print (i+1, " için:\n ----------------------")
        print ("Başlama zamani: ", startTime)
        print ("Bitirme zamani: ", finishTime)
        print ("İşlem süresi: ", processTime, " saniye")
        x.append(i)
        y.append(processTime)
    plt.plot(x,y) 
    plt.show()
    
n = 41  ## kaçıncı fibonacci elemanına kadar arayacağımızı giriyoruz

loopForRec(n)  ## recursive şekilde hesaplıyor
x = []  ## grafik eksenlerini sıfırlıyor
y = []
loopForLoop(n) ## lineer olarak hesaplıyor




