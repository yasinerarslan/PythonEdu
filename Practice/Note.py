""" Yapacağımız Programın Genel Mantığı Aşağıdaki Şekildedir:
1- Kullanıcıdan Vize ve Final Notu Girdisi Sağla (Not Girişi 100 İle Sınırlandırılacak)
2- Vize Notunun %40'ını Al
3- Final Notunun %60'ını Al
4- Vize ve Final Notunu Topla
5- Eğer Not Ortalaması 60'a Eşit veya Üzerinde İse Geçti Değilse Kaldığını Ekrana Yansıt """


print("'Vize ve Final' Ortalama Hesaplayıcı v1.0")
print("Lütfen Not Aralığını Aşmayınız. (En Az 0, En Çok 100)")
while True:
    vize=eval(input("Lütfen Vize Notunuzu Giriniz: "))
    # Vize Notu Girdisi Sağlandı
    if vize<=100:
        final=eval(input("Vize Notunuz Onaylandı. Lütfen Final Notunuzu Giriniz: "))
        # Final Notu Girdisi Sağlandı
        if final<=100:
            print("Final Notunuz Onaylandı.\nOrtalama Hesaplanıyor...")
            vizeort=vize*40/100
            # Vize Notunun %40'ı Alındı
            finalort=final*60/100
            # Final Notunun %60'ı Alındı
            ortalama=vizeort+finalort
            # Vize ve Final Notu Toplandı
            if ortalama>=60:
                print("Tebrikler... Dersi Geçtiniz.")
                print("Ortalamanız:",ortalama)
                break
            else:
                print("Şuan İçin Dersten Kaldınız...")
                print("Ortalamanız:",ortalama)
                but=eval(input("Lütfen Büt Notunuzu Giriniz: "))
                if but<=100:
                    butort=but*60/100
                    ortalama=vizeort+butort
                    if ortalama>=60:
                        print("Tebrikler... Dersten Kıl Payı Geçtiniz :)")
                        print("Ortalamanız:", ortalama)
                        break
                    else:
                        print("Üzgünüm... Dersi Geçemediniz. Seneye Yine Bekleriz :)")
                        print("Ortalamanız:", ortalama)
                        break
                else:
                    print("Lütfen Not Aralığında Bir Değer Giriniz... (En Az 0, En Çok 100)")
        else:
            print("Lütfen Not Aralığında Bir Değer Giriniz... (En Az 0, En Çok 100)")
    else:
        print("Lütfen Not Aralığında Bir Değer Giriniz... (En Az 0, En Çok 100)")

# "Yasin Erarslan" Tarafından Oluşturulmuştur
# 160255011
# Kırıkkle Üniversitesi - Bilgisayar Müh. (İkinci Öğretim)