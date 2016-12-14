import os

def main():
    print("Kahve Miktar Tutucu v1.0")
    tekrar="t"
    while tekrar=="t":
        print("-> Yeni Girdi İçin '1'")
        print("-> Girdi Eklemek İçin '2'")
        print("-> Girdi Okumak İçin '3'")
        print("-> Kahve Miktarı Öğrenmek İçin '4'")
        print("-> Kahve Miktarı Güncellemek İçin '5'")
        print("-> Kahve Silmek İçin '6'")
        secim=input("Seçiminiz Nedir?: ")

        if secim=="1":
            dosyaadi = input("Oluşturulacak Dosya Adı Nedir?: ")
            dosya = open(r"/home/mustachedocto/Belgeler/%s.txt" %dosyaadi,"w")
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

        elif secim=="4":
            dosyaadi=input("Varolan Dosya Adı Nedir?: ")
            dosya=open(r"/home/mustachedocto/Belgeler/%s.txt" %dosyaadi,"r")
            arama=input("Aranacak Kahve Adı Nedir?: ")
            bulundu=False
            kahveadi=dosya.readline().rstrip()
            while kahveadi!="":
                miktar=dosya.readline().rstrip()
                if arama==kahveadi:
                    print("Kahve Adı:",kahveadi)
                    print("Kahve Miktarı:",miktar)
                    bulundu=True
                    break
                else:
                    kahveadi=dosya.readline().rstrip()

        elif secim=="5":
            dosyaadi=input("Varolan Dosya Adı Nedir?: ")
            dosya=open(r"/home/mustachedocto/Belgeler/%s.txt" %dosyaadi,"r")
            gecicidosya=open(r"/home/mustachedocto/Belgeler/gecici.txt","w")
            arama=input("Güncellenecek Kahve Adı Nedir?: ")
            yenimiktar=input("Kahvenin Yeni Miktarını Girin: ")
            bulundu=False
            kahveadi=dosya.readline().rstrip()
            while kahveadi!="":
                miktar=dosya.readline().rstrip()
                if arama==kahveadi:
                    gecicidosya.write(kahveadi+"\n")
                    gecicidosya.write(yenimiktar+"\n")
                    bulundu=True
                    break
                else:
                    gecicidosya.write(kahveadi+"\n")
                    gecicidosya.write(miktar+"\n")
            os.remove("%s.txt" %dosyaadi)
            os.remove("gecici.txt","%s.txt" %dosyaadi)
            if bulundu:
                print("Dosyanız Güncellendi...")
            else:
                print("Bu Kahve Türü Bulunamadı Eklemek İçin Ana Menü'ye Dönünüz.")

        elif secim=="6":
            dosyaadi=input("Varolan Dosya Adı Nedir?: ")
            dosya=open(r"/home/mustachedocto/Belgeler/%s.txt" %dosyaadi,"r")
            gecicidosya=open(r"/home/mustachedocto/Belgeler/gecici.txt","w")
            arama=input("Silinecek Kahve Adı Nedir?: ")
            bulundu=False
            kahveadi=dosya.readline().rstrip()
            while kahveadi!="":
                miktar=dosya.readline().rstrip()
                if arama==kahveadi:
                    kahveadi=dosya.readline()
                    miktar=dosya.readline()
                    bulundu=True
                    break
                else:
                    gecicidosya.write(kahveadi+"\n")
                    gecicidosya.write(miktar+"\n")
            os.remove("%s.txt" %dosyaadi)
            os.remove("gecici.txt","%s.txt" %dosyaadi)
            if bulundu:
                print("Dosyanız Güncellendi...")
            else:
                print("Bu Kahve Türü Zaten Yok.")

        else:
            main()
        tekrar=input("Tekrar Seçim İçin 't', Çıkış İçin Herhangibir Karakter Tuşlayınız: ")

main()