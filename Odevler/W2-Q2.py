sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]

#Toplam isimli degisken olusturup "0" degeri atandi.
toplam = 0

# for dongusuyle her bir indexdeki sayi toplam degiskeni uzerinden toplandi.
for i in sayilar:
    toplam += i

#Ortlama isimli bir degisken ile listedeki sayilarin ortalamasi alindi.
ortalama = toplam / len(sayilar)
print(ortalama)

#"yuksek" ve "dusuk" isimli iki degisken olusturup, 
# listedeki degerlerin ortalama ile kiyaslandi.  
yuksek = 0
dusuk = 0

for x in sayilar:
    if x > ortalama:
        print("YUKSEK")
        yuksek += 1

    elif x < ortalama:
        print("DUSUK")
        dusuk += 1

#Her bir grubun toplam degerleri ekrana yazdirildi.
print("Yuksek:{} \nDusuk:{}".format(yuksek,dusuk))