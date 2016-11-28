def aralik(a, b):
    toplam = 1
    if a < b:
        for x in range(a, b + 1):
            toplam = toplam * x
        print(toplam)
    else:
        for x in range(b, a+1):
            toplam = toplam * x
        print(toplam)
def faktoriyel(sayi):
    toplam=1
    for x in range(1,sayi+1):
        toplam=toplam*x
    print(toplam)

tekrar="t"
while tekrar=="t":
    secim = int(input("Aralık Faktöriyel Hesabı İçin 1, Sayı Faktöriyel Hesabı İçin 2: "))
    if secim == 1:
        a = int(input("Lütfen Başlangıcı Giriniz: "))
        b = int(input("Lütfen Sonu Giriniz: "))
        aralik(a, b)
    else:
        sayi = int(input("Lütfen Faktöriyeli Hesaplanacak Sayıyı Giriniz: "))
        faktoriyel(sayi)
    tekrar=input("Tekrar için 't', Çıkış için 'Enter':")