def mukemmel(sayi):
    toplam=0
    for x in range(1,sayi):
        if sayi%x==0:
            print("Böleniniz:",x)
            toplam=toplam+x
    print("Toplamınız:",toplam)
    if toplam==sayi:
        sayim=True
    else:
        sayim=False
    return sayim

def mukemmelaralik(s1,s2):
    toplam=0
    for x in range(s1,s2):
        toplamsayi=0
        for y in range(1,x):
            if x%y==0:
                toplamsayi=toplamsayi+y
        if x==toplamsayi:
            sayim=True
        else:
            sayim=False
        if sayim==True:
            toplam=toplam+1
    print("Aralıktaki Mükemmel Sayılar:",toplam)

def sayigiris():
    sayi=int(input("Mükemmellik Kontrolü İçin Lütfen Bir Sayı Girimiz: "))
    return sayi

def main():
    print("Mükemmel Sayı Bulucu v1.0")
    sayi=sayigiris()
    tf=mukemmel(sayi)
    if tf==True:
        print("Sayınız Toplama Eşit. Sayınız Mükemmel Sayıdır...")
    else:
        print("Sayınız Toplama Eşit Değik. Sayınız Mükemmel Değildir...")

def main2():
    print("Mükemmel Sayı Bulucu v1.0")
    s1=int(input("İlk Sayı: "))
    s2=int(input("Son Sayı= "))
    mukemmelaralik(s1,s2)

main2()
