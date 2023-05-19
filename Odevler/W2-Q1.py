#Kullanicidan ad,soyad ve ogrenci numarasi istendi.
ad = input("Adiniz:")
soyad = input("Soyadiniz:")
numara = input("Ogrenci numaraniz:")


#Kullanicidan dort farkli dersin adi ve bu derslerin vize ve final notlari istendi.
#Ders1
ders1 = input("Birinci dersin adi:")
vize1 = int(input("Birinci dersin vie notu:"))
final1 = int(input("Birinci dersin final notu:"))

#Ders2
ders2 = input("Ikinci dersin adi:")
vize2 = int(input("Ikinci dersin vize notu:"))
final2 = int(input("Ikinci dersin final notu:"))

#Ders3
ders3 = input("Ucuncu dersin adi:")
vize3 = int(input("Ucuncu dersin vize notu:"))
final3 = int(input("Ucuncu dersin final notu:"))

#Ders4
ders4 = input("Dorduncu dersin adi:")
vize4 = int(input("Dorduncu dersin vize notu:"))
final4 = int(input("Dorduncu dersin final notu:"))

#Ders notlarinin ortalamasi hesaplandi.
total1 = (vize1 * 0.4) + (final1 * 0.6)
total2 = (vize2 * 0.4) + (final2 * 0.6)
total3 = (vize3 * 0.4) + (final3 * 0.6)
total4 = (vize4 * 0.4) + (final4 * 0.6)

#Ders sonuclarinin aciklanmasi
#Ders1
if total1 >= 50:
    print("{} dersinden gectiniz. Puaniniz:{}".format(ders1,total1))
elif total < 50:
    print("{} dersinden kaldiniz. Puaniniz:{}".format(ders1,total1))

#Ders2
if total2 >= 50:
    print("{} dersinden gectiniz. Puaniniz:{}".format(ders2,total2))
elif total < 50:
    print("{} dersinden kaldiniz. Puaniniz:{}".format(ders2,total2))

#Ders3
if total3 >= 50:
    print("{} dersinden gectiniz. Puaniniz:{}".format(ders3,total3))
elif total < 50:
    print("{} dersinden kaldiniz. Puaniniz:{}".format(ders3,total3))

#Ders4
if total4 >= 50:
    print("{} dersinden gectiniz. Puaniniz:{}".format(ders4,total4))
elif total < 50:
    print("{} dersinden kaldiniz. Puaniniz:{}".format(ders4,total4))