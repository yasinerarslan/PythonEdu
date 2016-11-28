def satis():
    satis = int(input("Lütfen Aylık Satış Miktarınızı Girin: "))
    return satis

def avans():
    while True:
        avans=int(input("Lütfen Avans Miktarınızı Girin: "))
        if avans > 2000:
            print("Lütfen Avans Miktarınız 2000'den Büyük Olmasın...")
        else:
            break
    return avans

def komisyon(satis):
    if satis<10000:
        kom=satis*0.10
    elif satis>=10000 and satis<15000:
        kom=satis*0.12
    elif satis>=15000 and satis<18000:
        kom=satis*0.14
    elif satis>=18000 and satis<22000:
        kom=satis*0.16
    else:
        kom=satis*0.18
    return kom

def sonuc(kom,avans):
    sonuc=kom-avans
    print("Bu Ay Komisyon Miktarınız:", sonuc)
    if sonuc < 0:
        print("Lütfen Borcunuzu Firmaya Ödeyiniz...")
    else:
        print("Tebrikler Gelir Sağladınız...")

tekrar="t"
while tekrar=="t":
    a=avans()
    s=satis()
    k=komisyon(s)
    sonuc(k,a)
    tekrar=input("Tekrar Hesap İçin 't', Çıkış İçin 'Enter': ")