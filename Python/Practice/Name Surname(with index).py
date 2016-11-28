def isimsoyisim():
    isim=input("Lütfen Adınızı Giriniz:")
    soyisim=input("Lütfen Soyadınızı Giriniz:")
    isim=isim.upper()
    soyisim=soyisim.upper()
    basharfler=""
    basharfler=isim[0]+"."+soyisim[0]+"."
    print(basharfler)

def main():
    isimsoyisim()

main()
