import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Veri_seti.xlsx")
print(df)

for column in df.columns:
    plt.figure()
    plt.boxplot(df[column])
    plt.title(f"{column} Boxplot")
    plt.ylabel(column)
    plt.show()

sutunlar = ["YAŞ", "BOY", "KİLO", "Ç_Saati"]


Temiz_Veriler = {}
Aykiri_Degerler = []

for sutun in sutunlar:
    dizi = []
    n = 0
    for eleman in df[sutun]:
        dizi.append(eleman)
        n += 1
    
    for i in range(n):
        for j in range(0, n-i-1):
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
   
    if n % 2 != 0:
        orta = (n-1)//2
        medyan = dizi[orta]
    else:
        medyan = (dizi[n//2 - 1] + dizi[n//2])/2
    
    if n % 2 != 0:
        alt = dizi[:orta]
        ust = dizi[orta+1:]
    else:
        alt = dizi[:n//2]
        ust = dizi[n//2:]
    n_alt = 0
    for _ in alt: n_alt += 1
    if n_alt % 2 != 0:
        med_alt = alt[n_alt//2]
    else:
        med_alt = (alt[n_alt//2 - 1] + alt[n_alt//2])/2
    n_ust = 0
    for _ in ust: n_ust += 1
    if n_ust % 2 != 0:
        med_ust = ust[n_ust//2]
    else:
        med_ust = (ust[n_ust//2 - 1] + ust[n_ust//2])/2
    aciklik = med_ust - med_alt
    alt_sinir = med_alt - 1.5 * aciklik
    ust_sinir = med_ust + 1.5 * aciklik


    temiz_sutun = []
    aykiri = []
    for deger in dizi:
        if deger < alt_sinir or deger > ust_sinir:
            aykiri.append(deger)
        else:
            temiz_sutun.append(deger)
    Temiz_Veriler[sutun] = temiz_sutun
    Aykiri_Degerler.append(aykiri)


with open("istatistik_sonuclari.txt", "w", encoding="utf-8") as dosya:

    print("\n--- Aritmetik ortalama ---")
    for sutun in sutunlar:
        toplam = 0.0
        gozlem = 0
        for eleman in Temiz_Veriler[sutun]:
            toplam += eleman
            gozlem += 1
        ortalama = toplam/gozlem
        print(f"{sutun} Aritmetik ortalama: {ortalama}")
        dosya.write(f"{sutun} Aritmetik ortalama: {ortalama}\n")
    dosya.write("\n")
    
    print("\n--- Medyan ---")
    for sutun in sutunlar:
        dizi = []
        gozlem = 0
        for eleman in Temiz_Veriler[sutun]:
            dizi.append(eleman)
            gozlem += 1
      
        for i in range(gozlem):
            for j in range(0, gozlem-i-1):
                if dizi[j] > dizi[j+1]:
                    dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
        if gozlem % 2 != 0:
            orta_indeks = (gozlem-1)//2
            medyan = dizi[orta_indeks]
        else:
            medyan = (dizi[gozlem//2 - 1] + dizi[gozlem//2])/2
        print(f"{sutun} Medyan: {medyan}")
        dosya.write(f"{sutun} Medyan: {medyan}\n")
    dosya.write("\n")

    print("\n--- Mod ---")
    for sutun in sutunlar:
        sayac = {}
        for eleman in Temiz_Veriler[sutun]:
            if eleman in sayac:
                sayac[eleman] += 1
            else:
                sayac[eleman] = 1
        mod = None
        maks_tekrar = 0
        for key in sayac:
            if sayac[key] > maks_tekrar:
                maks_tekrar = sayac[key]
                mod = key
        print(f"{sutun} Mod: {mod}")
        dosya.write(f"{sutun} Mod: {mod}\n")
    dosya.write("\n")

    
    print("\n--- Değişim Aralığı ---")
    for sutun in sutunlar:
        min_deger = Temiz_Veriler[sutun][0]
        max_deger = Temiz_Veriler[sutun][0]
        for eleman in Temiz_Veriler[sutun]:
            if eleman < min_deger:
                min_deger = eleman
            if eleman > max_deger:
                max_deger = eleman
        Degisim_araligi = max_deger - min_deger
        print(f"{sutun} Değişim aralığı: {Degisim_araligi}")
        dosya.write(f"{sutun} Değişim aralığı: {Degisim_araligi}\n")
    dosya.write("\n")


    print("\n--- Ortalama Mutlak Sapma ---")
    for sutun in sutunlar:
        toplam = 0.0
        gozlem = 0
        for eleman in Temiz_Veriler[sutun]:
            toplam += eleman
            gozlem += 1
        ortalama = toplam/gozlem
        mutlak_farklar = []
        for eleman in Temiz_Veriler[sutun]:
            mutlak_farklar.append(abs(eleman - ortalama))
        toplam = 0.0
        gozlem = 0
        for eleman in mutlak_farklar:
            toplam += eleman
            gozlem += 1
        ortalama = toplam/gozlem
        print(f"{sutun} Ortalama Mutlak Sapma: {ortalama}")
        dosya.write(f"{sutun} Ortalama Mutlak Sapma: {ortalama}\n")
    dosya.write("\n")

    print("\n--- Varyans ---")
    StandartSapmalar = []
    Degisim_Katsayilari = []
    for sutun in sutunlar:
        dizi=[]
        toplam=0.0
        gozlem=0
        for eleman in Temiz_Veriler[sutun]:
            toplam += eleman
            gozlem += 1
        ortalama = toplam/gozlem
        toplam_kare = 0.0
        for eleman in Temiz_Veriler[sutun]:
            fark = eleman - ortalama
            toplam_kare += fark*fark
        varyans = toplam_kare / (gozlem-1)
        StandartSapma = varyans**0.5
        StandartSapmalar.append(StandartSapma)
        Degisim_Katsayisi = (StandartSapma / ortalama) * 100
        Degisim_Katsayilari.append(Degisim_Katsayisi)
        print(f"{sutun} Varyans: {varyans}")
        dosya.write(f"{sutun} Varyans: {varyans}\n")
    dosya.write("\n")

    print("\n--- Standart Sapmalar ---")
    sayac = 0
    for sutun in sutunlar:
        sapma = StandartSapmalar[sayac]
        print(f"{sutun} Standart Sapma: {sapma}")
        dosya.write(f"{sutun} Standart Sapma: {sapma}\n")
        sayac += 1
    dosya.write("\n")
    
    print("\n--- Değişim Katsayıları ---")
    sayac = 0
    for sutun in sutunlar:
        Dkatsayisi = Degisim_Katsayilari[sayac]
        print(f"{sutun} Değişim Katsayısı: {Dkatsayisi}%")
        dosya.write(f"{sutun} Değişim Katsayısı: {Dkatsayisi}%\n")
        sayac += 1
    dosya.write("\n")
    
    StandartSapmalar=[]
    Degisim_Katsayilari=[]
    print("\n--- Varyans ---")    
    for sutun in sutunlar:
        dizi=[]
        toplam=0.0
        gozlem=0
        for eleman in Temiz_Veriler[sutun]:
            toplam+=eleman
            gozlem+=1
        ortalama=toplam/gozlem
        toplam_kare=0.0
        for eleman in Temiz_Veriler[sutun]:
            fark=eleman-ortalama
            kare=fark*fark
            toplam_kare+=kare
        varyans=toplam_kare/(gozlem-1)
        StandartSapma=varyans**0.5
        StandartSapmalar.append(StandartSapma)
        Degisim_Katsayisi=(StandartSapma/ortalama)*100
        Degisim_Katsayilari.append(Degisim_Katsayisi)
        print(f"{sutun} Varyans:{varyans}")
        dosya.write(f"{sutun} Varyans: {varyans}\n")
    dosya.write("\n")
        
    
    print("\n--- Standart Sapmalar ---")
    sayac = 0
    for sutun in sutunlar:
        sapma = StandartSapmalar[sayac]
        print(f"{sutun} Standart Sapma: {sapma}")
        dosya.write(f"{sutun} Standart Sapma: {sapma}\n")
        sayac += 1
    dosya.write("\n")
    
    
    print("\n--- Degisim Katsayıları ---")
    sayac=0
    for sutun in sutunlar:
        Dkatsayisi=Degisim_Katsayilari[sayac]
        print(f"{sutun} Degisşim Katsayisi: {Dkatsayisi}%")
        dosya.write(f"{sutun} Degisim Katsayisi: {Dkatsayisi}%\n")
        sayac += 1
    dosya.write("\n")

 
    print("\n--- Çeyrekler Açıklığı ---")
    Ceyrekler_Acikligi = []
    for sutun in sutunlar:
        dizi = []
        n = 0
        for eleman in Temiz_Veriler[sutun]:
            dizi.append(eleman)
            n += 1
        for i in range(n):
            for j in range(0, n-i-1):
                if dizi[j] > dizi[j+1]:
                    dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
        if n % 2 != 0:
            orta = (n-1)//2
            medyan = dizi[orta]
        else:
            medyan = (dizi[n//2 - 1] + dizi[n//2])/2
        if n % 2 != 0:
            alt = dizi[:orta]
            ust = dizi[orta+1:]
        else:
            alt = dizi[:n//2]
            ust = dizi[n//2:]
        n_alt = 0
        for _ in alt: n_alt += 1
        if n_alt % 2 != 0:
            med_alt = alt[n_alt//2]
        else:
            med_alt = (alt[n_alt//2 - 1] + alt[n_alt//2])/2
        n_ust = 0
        for _ in ust: n_ust += 1
        if n_ust % 2 != 0:
            med_ust = ust[n_ust//2]
        else:
            med_ust = (ust[n_ust//2 - 1] + ust[n_ust//2])/2
        aciklik = med_ust - med_alt
        Ceyrekler_Acikligi.append(aciklik)
        print(f"{sutun} Çeyrekler Açıklığı: {aciklik}")
        dosya.write(f"{sutun} Çeyrekler Açıklığı: {aciklik}\n")
    dosya.write("\n")
    
    print("\n--- Aykırı Değerler ---")
    sayac = 0
    for sutun in sutunlar:
        print(f"{sutun}: {Aykiri_Degerler[sayac]}")
        dosya.write(f"{sutun} Aykırı Değerler: {Aykiri_Degerler[sayac]}\n")
        sayac += 1
    
       
