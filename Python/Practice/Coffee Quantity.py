def main():
    print("Kahve Miktar Tutucu v1.0")
    tekrar="t"
    while tekrar=="t":
        print("-> Yeni Girdi İçin 1")
        print("-> Girdi Eklemek İçin 2")
        print("-> Girdi Okumak İçin 3")
        secim=input("Seçiminiz Nedir?: ")
        if secim=="1":
            dosyaadi = input("Oluşturulacak Dosya Adı Nedir?: ")
            dosya = open(r"/home/mustachedocto/Belgeler/%s.txt" % dosyaadi, "w")
            secim=int(input("Kaç Adet Kahve Bulunuyor?: "))
            for sayac in range(1,secim+1):
                kahveadi=input("Girilecek Kahve Adı Nedir?: ")
                miktar=input("Depoda Ne Kadar Bulunuyor?: ")
                dosya.write(kahveadi+"\n")
                dosya.write(miktar+"\n")
            dosya.close()
        elif secim=="2":
            dosyaadi=input("Varolan Dosya Adı Nedir?: ")
            dosya=open(r"/home/mustachedocto/Belgeler/%s.txt" %dosyaadi,"a")
            kahveadi=input("Girilecek Kahve Adı Nedir?: ")
            miktar=input("Depoda Ne Kadar Bulunuyor?: ")
            dosya.write(kahveadi+"\n")
            dosya.write(miktar+"\n")
            dosya.close()
        elif secim=="3":
            dosyaadi=input("Varolan Dosya Adı Nedir?: ")
            dosya=open(r"/home/mustachedocto/Belgeler/%s.txt" %dosyaadi,"r")
            for satir in dosya:
                satir=satir.rstrip()
                print("Kahve Adı:",satir)
                satir=dosya.readline().rstrip()
                print("Kahve Miktarı:",satir)
        else:
            main()
        tekrar=input("Tekrar Seçim İçin 't', Çıkış İçin Herhangibir Karakter Tuşlayınız: ")

main()