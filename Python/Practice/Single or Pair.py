def tekciftbul(b,s):
    # Toplam Değerleri ve Sayaç Değerleri 0'a eşitlendi.
    toplamc = 0
    toplamt = 0
    sayacc = 0
    sayact = 0

    # Oluşturulan Fonksiyon bir koşula bağlandı. (Koşul Başlangıç ve Son Değerlerinin Birbirine Göre Durumları İle İlgilidir.)
    if baslangic<=son:
        # For Sayesinde B ve S değerleri arasındaki her sayı tek tek mod hesaplama işlemi yapılıyor.
        for x in range(baslangic,son+1):
            mod=x%2
            # Elde edilen mod değeri bir koşula bağlandı. (Mod Değerinin 0 veya Farklı Olması İle İlgilidir.)
            if mod==0:
                sayacc=sayacc+1
                toplamc=toplamc+x
            else:
                toplamt=toplamt+x
                sayact=sayact+1
        # Tek ve Çift Sayıların Art. Ort. alımdı.
        tekort=toplamt//sayact
        ciftort=toplamc//sayacc
        print("\n**********Tek Sayılar**********")
        print("Tek Sayıların Sayısı: ",sayact)
        print("Tek Sayıların Toplamı: ",toplamt)
        print("Tek Sayıların Aritmetik Ortalaması: ",tekort)
        print("\n*********Çift Sayılar**********")
        print("Çift Sayıların Sayısı: ",sayacc)
        print("Çift Sayıların Toplamı: ",toplamc)
        print("Çift Sayıların Aritmetik Ortalaması: ",ciftort)
    else:
        # For Sayesinde B ve S değerleri arasındaki her sayı tek tek mod hesaplama işlemi yapılıyor.
        for x in range(son,baslangic+1):
            mod=x%2
            # Elde edilen mod değeri bir koşula bağlandı. (Mod Değerinin 0 veya Farklı Olması İle İlgilidir.)
            if mod==0:
                sayacc=sayacc+1
                toplamc=toplamc+x
            else:
                toplamt=toplamt+x
                sayact=sayact+1
        # Tek ve Çift Sayıların Art. Ort. alımdı.
        tekort=toplamt//sayact
        ciftort=toplamc//sayacc
        print("\n**********Tek Sayılar**********")
        print("Tek Sayıların Sayısı: ",sayact)
        print("Tek Sayıların Toplamı: ",toplamt)
        print("Tek Sayıların Aritmetik Ortalaması: ",tekort)
        print("\n*********Çift Sayılar**********")
        print("Çift Sayıların Sayısı: ",sayacc)
        print("Çift Sayıların Toplamı: ",toplamc)
        print("Çift Sayıların Aritmetik Ortalaması: ",ciftort)

tekrar="t"
while tekrar=="t" or tekrar=="T":
    while True:
        try:
            baslangic=int(input("Aralığın Başlangıç Sayısını Giriniz: "))
            son=int(input("Aralığın Son Sayısını Giriniz: "))
            tekciftbul(baslangic, son)
            break
        except:
            print("Sadece Tam Sayı Girişi Yapılabilir...")
    tekrar=input("\nTekrar İçin 't', Çıkış İçin Herhangi Bir Karakter Tuşlayınız: ")