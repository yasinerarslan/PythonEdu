def menu():
    print("Not Girişi İçin '1'")
    print("Not Eklemek İçin '2'")
    print("Not Tespiti İçin '3'")
    secim = input("Seçiminiz Nedir?: ")
    if secim == "1" or secim == "2" or secim == "3":
        return secim
    else:
        print("Lütfen Sadece Menüdeki Değerleri Tuşlayınız...")
        menu()

def isim():
    oisim=input("Öğrenci İsmi Nedir?: ")
    return oisim

def notlar():
    onot=input("Aldığı Not Nedir?: ")
    return onot

def notgirisi():
    dosya_isim=open(r"/home/mustachedocto/Belgeler/isimler.txt","w")
    dosya_not=open(r"/home/mustachedocto/Belgeler/notlar.txt","w")
    oisim=isim()
    onot=notlar()
    dosya_isim.write(oisim+"\n")
    dosya_not.write(onot+"\n")
    dosya_isim.close()
    dosya_not.close()
    print("Not Girişi Tamamlandı...")

def yeninotgirisi():
    dosya_isim=open(r"/home/mustachedocto/Belgeler/isimler.txt","a")
    dosya_not=open(r"/home/mustachedocto/Belgeler/notlar.txt","a")
    oisim=isim()
    onot=notlar()
    dosya_isim.write(oisim+"\n")
    dosya_not.write(onot+"\n")
    dosya_isim.close()
    dosya_not.close()
    print("Yeni Not Girişi Tamamlandı...")

def notogren():
    dosya_isim=open(r"/home/mustachedocto/Belgeler/isimler.txt","r")
    dosya_not=open(r"/home/mustachedocto/Belgeler/notlar.txt","r")
    oisim=isim()
    sayac=0
    for ogrenciadi in dosya_isim:
        sayac=sayac+1
        ogrenciadi=ogrenciadi.rstrip()
        if ogrenciadi==oisim:
            for ogrencinot in range(1,sayac+1):
                satir=dosya_not.readline()
                satir=satir.rstrip()
                if ogrencinot==sayac:
                    print("Öğrencinin Aldığı Not:",satir)

def main():
    secim=menu()
    if secim=="1":
        notgirisi()
    elif secim=="2":
        yeninotgirisi()
    elif secim=="3":
        notogren()

main()