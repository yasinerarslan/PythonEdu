def yazitura():
    import random
    secim=input("Yazı mı 'y', Tura mı 't'?: ")
    zeka=random.randint(0,1)
    if zeka==0:
        print("Yazı...")
    else:
        print("Tura...")
    if secim=="y" and zeka==0:
        print("Kazandınız...")
    elif secim=="t" and zeka==1:
        print("Kazandınız...")
    else:
        print("Kaybettiniz...")

tekrar="1"
while tekrar=="1":
    yazitura()
    tekrar=input("Tekrar Denemek İçin 1, Çıkış İçin Enter Tuşlayın: ")