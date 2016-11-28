def indirimhesap(urun,indirim):
    ind=indirim/100
    hesap=urun*ind
    sonuc=urun-hesap
    return sonuc

urun=eval(input("Lütfen Ürün Fiyatını Giriniz: "))
indirim=eval(input("Lütfen İndirim Oranını Giriniz: "))
s=indirimhesap(urun,indirim)
print("İndirimli Fiyat:",s)