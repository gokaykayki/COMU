
# coding: utf-8

# In[ ]:

#####  1-) Naive Bayes Classifier nedir? Ne amaçla kullanılır?
### Yapay zeka algoritması....
#####  2-)Naive Bayes Classifier & Cluster arasındaki fark nedir?
### Classifier'da data set var data + label. Cluster'da labellar yok. Labeller olmadan veriyi analiz etme işi cluster ile.
#####  3-) Linkteki(https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/) python kodundaki bütün fonksiyonların input-output şeklinde blok şeması olarak gösterip kısaca amacını yazınız.
#####  4-) Dataset'teki  bir listenin formunu(biçim, şekil) kısaca açıklayın.
### img1.reshape(1,img1.shape[0]*,img1.shape[1]) img1.appeng('label') // Cevap değil
#####  5-) Kaç tane mean değeri vardır?
### 0-9 -> 10 tane
#####  6-) trainSet, testSet nedir? Dataset üzerinden hangi oranlarda elde edilir?
### dataset ikiye ayrılır. train set elde edeceğimiz fonksiyon için kullanacağımız veri. testset'i de bunu kontrol için kullanılır. testset yaklaşık %20 olur.
#####  7-) Prediction nedir? Hatası nasıl ölçülür?
### testset setten veriyi teker teker test edip yüzde değer çıkarma. Hatası da label kıyası ile ölçülür.
#####  8-) Kendinizin oluşturduğu bir testverisi ile bu algoritmayı çalıştırınız
#####  9-) [123] kaç tane rakam olduğunu bulan bir fonksiyon yazınız.
### BW çevir. Sınırı 0 olan objeleri saydır.
#####  10-) 9'da elde edilen sayı kadar resim return eden bir fonksiyon yazınız.
### Xmin Ymix, Xmax Ymax a göre resmi cropla(?)
#####  11-) Elde edilen herbir resmi linkteki kod ile çalıştırıp sonucu yazdırınız.

