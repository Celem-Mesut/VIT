while True:
    try:
        ilk_sayi = int(input("Birinci sayiyi girin:"))
        ikinci_sayi = int(input("Ikinci sayiyi girin:"))
    except ValueError:
        print("Hatali Giris. Lutfen bir sayi girin!")
        continue
    toplam = 0
    for i in range(ilk_sayi,ikinci_sayi+1):
        if i % 2 != 0:
            toplam = toplam + i

    print(toplam)
    break