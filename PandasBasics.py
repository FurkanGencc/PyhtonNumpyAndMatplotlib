# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 19:46:09 2025

@author: Turkuaz
Pandas kütüphanesi
Veri işleme ve veri analizinde kullanılır.
Pandas çoğu işlemi arka tarafta numpy ile yapar.
İki temel veri yapısı vardır series,DataFrame
numpy matematik ve sayısal işlemler için
pandas Tablo verisi yönetimi ve analizi için kullanılır
dosya okuma da yapılır 
"""

import pandas as pd 

#Sözlük
dictionary={"isim" :["ali","furkan","enes","mehmet","ayşe","halil"],
            "yas"  :[23,25,26,27,30,33],
            "maas" :[100,230,400,500,300,500]}

veri=pd.DataFrame(dictionary)#Sözlüğü veriyapısına veri çercevesine çeviridk
print(veri,"\n")
#Her sözlükte ki her anahtar bir sütun oldu dataframe ile bu sözlük yapısını bir tabloya çevirdik

#Verinin ilk beş satırı için
print(veri.head())
#Verinin sütünlarını yazdır
print(veri.columns)
#Veri Bilgisi verinin temel bilgisini görmek için kullanılır ilk izlenim için kullanılır
print(veri.info())

"""
İnfo çıktısı

Index(['isim', 'yas', 'maas'], dtype='object')
<class 'pandas.core.frame.DataFrame'> --> Verimiz bir  pandas dataframe  
RangeIndex: 6 entries, 0 to 5    --> 6 tane  içerik ver ve 0 ile 5 le indekslenmiş
Data columns (total 3 columns): --> Üç adet sütünu vardır
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   isim    6 non-null      object
 1   yas     6 non-null      int64 
 2   maas    6 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 276.0+ bytes
None


"""

#İstatistiksel özellikleri
print(veri.describe(),"\n")
# yaş sütünun 
print(veri["yas"],"\n")

#Sütün ekleme
veri["sehir"]=["ankara","izmir","ankara","konya","kırıkkale","konya"]
print(veri)
#yaş sütunun 4 satırı
print(veri.loc[:3,"yas"]) #numpy ve listelerden farklı olarak 3 dahildir  exclusive(özel) değil inclusivedir(dahil).

#yaş dan şehire kadar şehir dahil 3 satır
print(veri.loc[:2,"yas":"sehir"]) #loc locaiton anlamında


# isim ve yaşı alıcaz 3 satır
print(veri.loc[:2,["yas","isim"]])
#satırları tersten yazdır
print(veri.loc[::-1,:])

#yaş sütununu iloc ile yazdırma yan indexinden

print(veri.iloc[:,1])#tüm satırları ve birinci index


#ilk üç satır ve yaş ve isim indexleri ile

print(veri.iloc[:3,[0,1]])#iloc da 3 dahil değil. loc da dahil ama 

#filtreleme 
# yaşa göre bir filtre

filtre1=veri.yas>25

filtrelenmis_Veri=veri[filtre1]
print(filtrelenmis_Veri)

#ortalama yaş
ort_yas=veri.yas.mean()


veri["YAŞ_GRUBU"]=["kucuk"if ort_yas>i else"buyuk"for i in veri.yas]
print(veri)


#iki adet veri setinin yatayda ve dikeyde birleştirmesi 

sozluk1={"isim" :["ali","furkan","enes"],
            "yas"  :[23,25,26,],
            "maas" :[100,230,400]}

veri1=pd.DataFrame(sozluk1)

sozluk2={"isim" :["veli","mehmet","kenan"],
            "yas"  :[24,15,16,],
            "maas" :[100,210,440]}

veri2=pd.DataFrame(sozluk2)
#dikeyde birleştirme
veri_dikey=pd.concat([veri1,veri2],axis=0)

#yatay birleştirme
veri_dikey=pd.concat([veri1,veri2],axis=1)

#%% Oğrenci not verisi
import pandas as pd
notlar={"İsim":["Furkan","Ahmet","Ayşe","Mehmet","Ali","Veli"],
        "Not":[45,70,30,85,43,80]
           }

veri=pd.DataFrame(notlar)
print(veri,"\n")
#verinin ilk üç satırı
print(veri.head(3),"\n")
#verinin sütunları
print(veri.columns,"\n")
#not sütunu
print(veri["Not"],"\n")
#sütun ekleme
veri["Ders"]=["Türkçe","Türkçe","Matematik","Matematik","Fizik","Kimya"]
print(veri,"\n")
#not sütunun ilk 5 satırı
print(veri.loc[:4,"Not"],"\n")#isimle erşim iloc indeksle erişim

#isim ve not sütünları beraber  3 satırı
print(veri.loc[:2,["İsim","Not"]])

#Sütunun indexi ile yazdırma iloc
print("\n",veri.iloc[:,2])

print("\n",veri.iloc[:2,[1,2]])#1. ve 2. indeksleri(sütun indeksleri) al ilk iki satırları 
filtre=veri.Not<50
print("\n",filtre)
filtrelenmis_veri=veri[filtre]
print("\n",filtrelenmis_veri)



