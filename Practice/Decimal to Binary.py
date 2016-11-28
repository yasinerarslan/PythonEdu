""" 10'luk tabandaki bir sayıyı 2'lik tabana çevirip geri döndüren bir fonksiyon yazınız.
Fonksiyon 10'luk tabandaki sayıyı parametre alacak ikili sayıyı geri döndürecektir.
Bu soruda quizde yazdığımız fonksyionu kullanmamız gerekmektedir... """

def terscevirkisa(binary):
    # 'terscevir()' fonksiyonunda yazdığımız işlemi yapan kod satırımız.
    binarysonuc=binary[::-1]
    return binarysonuc

def binary(sayi):
    # Boş bir 'string' satırı oluşturuldu. Çünkü çıkacak sonuç bir 'string' olarak çıktısı sağlanacak.
    binary=""
    # Sayi büyüklüğü kontrolu. İkilik tabana çevirme işlemi 'kalan ve bölen'e' bağlı şekilde yapılıyor.
    while sayi>=2:
        # Kalan hesaplanıp boş string'e ekleniyor.
        kalan=sayi%2
        if kalan==1:
            binary=binary+"1"
        else:
            binary=binary+"0"
        # Bölüm hesap edilip varsayılan 'sayi' yerine geçiyor. While döngüsü burada işimize yarayacak.
        bolum=sayi//2
        sayi=bolum
    # En son çıkan 'bolum' değeri koşula başlı olarak '0 veya 1' eklenmesini sağlıyor.
    if bolum==1:
        binary=binary+"1"
    else:
        binary=binary+"0"
    return binary

def sayigirisi():
    try:
        # Sayı girişi kullanıcı tarafından sağlanıyor ve değer 'main()' fonksiyonuna döndürülüyor.
        sayi=int(input("Lütfen İkilik Tabana Çevrilmesini İstediğiniz Sayıyı Giriniz: "))
        return sayi
    except:
        print("Lütfen Sadece 'Tam Sayı' Girişi Yapınız...")

def main(s):
    if s==True:
        tekrar = "t"
        while tekrar == "t" or tekrar == "T":
            sayi=sayigirisi()
            if sayi==1 or sayi==0:
                print(sayi)
            else:
                binarysayi=binary(sayi)
                sonuc=terscevirkisa(binarysayi)
                print(sonuc)
            tekrar = input("Tekrar hesaplamak için 't', Çıkış yapmak için herhangi bir karakter tuşlayınız: ")
    else:
        pass

def menu():
    print('''İkilik 'Binary' Tabana Dönüşüm v1.0\n
    **************************
    ***** Yasin Erarslan *****
    *** KKU Bilgisayar Müh.***
    *** Öğr. No: 160255011 ***
    **************************\n''')
    print("1 - Onluk Tabandan İkilik Tabana Dönüşüm")
    print("2 - Çıkış")
    secim=input("Lütfen Yapmak İstediğiniz İşlemi Tuşlayınız: ")
    if secim=="1":
        s=True
    else:
        s=False

    return s

s=menu()
main(s)

# "Yasin Erarslan" Tarafından Oluşturulmuştur
# 160255011
# Kırıkkle Üniversitesi - Bilgisayar Müh. (İkinci Öğretim)
