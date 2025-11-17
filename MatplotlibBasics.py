# -*- coding: utf-8 -*-
"""

@author: Turkuaz

-matpoltlib kütüphanesi veri görselleştirme için kullanılır
-numpy üzerine kurulmuş bir kütüphane
-numpy ile elde ettiğimiz sonuçlar görselleştirmek


"""

import matplotlib.pyplot as plt
import numpy as np


x=np.array([1,2,3,4])
y=np.array([5,6,7,8])

plt.figure(figsize=(6,4))# plt.figure bos bir alan oluşturur
#figsize(6,4) 6genişlik 4 yükseklik 

plt.plot(x,y,marker='o',linestyle="-",linewidth=2)
#plt.plot çizgi grafiği oluşturur
plt.title("Çizgi Grafiği")

plt.xlabel("X degeri")
plt.ylabel("Y degeri")

plt.grid(True)# tabloya kare çizgiler oluşturur
plt.legend(["y vs x"])# grafikteki çizgilerin hangi veriyi temsil ettiğini söyler

"""
plt.figure() kağıdı açar  figuru açma
plt.plot() çizimi yapar
plt.show() çizimi gösterir  figuru kapatma


"""
plt.show()

# İki farklı görüntüyü tek bir figure içinde çizme
#subplot yöntemi kullanılır birden fazla plotu tek bir figure de göstericez

fig, axes=plt.subplots(2,1, figsize=(10,10))# 2 satır(resim) 1 
fig.subplots_adjust(hspace=0.5)# grafikler arasında boşluk horizontal space

x=[1,2,3,4,5,6,7,8,9]
y=[10,11,12,13,14,15,16,17,18]

axes[0].scatter(x,y) #scatter her bir veriyi nokta olarak çizer
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].plot(x,y)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")

plt.show()


#random resim

plt.figure()
img=np.random.random((50,50))#2 boyutlu matis 0 ile 1 arasında rastgele oluşmuş sayılar
plt.imshow(img, cmap="gray")#cmap(colour map) gray 0 değerlerini siyaha yakın yap 1 değerlerini beyaza
#0.5 tam gri
plt.show

#oluşan pikseller her bir matrisin içindeki deger
#matrisin içindeki değerler 1 e yakınsa piksel beyaz 0 a yakınsa siyah bu değerler o pikselin genliği