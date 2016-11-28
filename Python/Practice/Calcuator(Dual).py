def gorev(s1,s2,oprt):
    if oprt=="+":
        sonuc=toplama(s1,s2)
    elif oprt=="-":
        sonuc=cikarma(s1,s2)
    elif oprt=="/":
        sonuc=bolme(s1,s2)
    else:
        sonuc=carpma(s1,s2)
    return sonuc

def menu():
    print("Toplama İşlemi İçin '+'\nÇıkarma İşlemi İçin '-'\nÇarpma İşlemi İçin '*'\nBölme İşlemi İçin '/'")
    oprt=input("Yapılmak İstenen İşlemi Giriniz: ")
    return oprt

def toplama(s1,s2):
    sonuc=s1+s2
    return sonuc

def cikarma(s1,s2):
    sonuc=s1-s2
    return sonuc

def bolme(s1,s2):
    sonuc=s1/s2
    return sonuc

def carpma(s1,s2):
    sonuc=s1*s2
    return sonuc

def main():
    print("İki Sayılı Hesap Maiknesi v1.0")
    tekrar="t"
    while tekrar=="t" or tekrar=="T":
        try:
            oprt=menu()
            s1=int(input("İlk Sayıyı Giriniz: "))
            s2=int(input("İkinci Sayıyı Giriniz: "))
            print("Sonuç:",gorev(s1, s2, oprt))
            tekrar=input("Tekrar için 't', Çıkış için herhangibir tuşa basın: ")
        except:
            print("Lütfen Sadece Tam Sayı Değeri Giriniz...")

main()
