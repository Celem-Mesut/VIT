sani = input("Sureyi saniye olcu biriminde girin:")
saniye = int(sani)
dakika = saniye // 60
saat = dakika // 60
gun = saat // 24
print("{} gun,{}saat,{}dakika,{}saniye".format(gun,saat,dakika,saniye))