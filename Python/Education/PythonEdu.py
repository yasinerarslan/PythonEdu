# Neden Python dersek programlarının en büyük özelliklerinden birisi, C ve C++ gibi dillerin aksine, derlenmeye
# gerek olmadan çalıştırılabilmeleridir. Python’da derleme işlemi ortadan kaldırıldığı için, bu dille oldukça hızlı
# bir şekilde program geliştirilebilir.

# Tam Sayılar = 2, 3, 4, 11, 16... = Integer
# Ondalık Sayılar = 2.2, 3.5, 8.5... = Float
# İsimler... = Yasin, abc... = String

# Ekranda bir çıktı almak için "print" komutu kullanılabilir örneğin;

print("HelloWorld")

# Değer tipi sorgulamak için "type" komutu kullanılabilir örneğin;

type(2.2)
type(160255011)
type("HelloWorld")

# Değer Ayracı İçin "," kullanılabilir örneğin;

print("HelloWorld",2,6,2.2)

# !!! Değişken İsmi Sayı İle Başlamaz. Kullanıldığı Zaman "Syntax Error (İmla Hatası)" Olarak Çıktı Belirir. Örneğin;

1=6
    #SyntaxError: can't assign to literal

# !!! Değişken İsimlerinde Boşluk Kullanılamaz. Kullanıldığı Zaman "Syntax Error (İmla Hatası)" Olarak Çıktı Belirir. Örneğin;

Adı Soyadı="Yasin Erarslan"
    #SyntaxError: can't assign to literal
    # Adı_Soyadı="Yasin Erarslan" veya AdıSoyadı="Yasin Erarslan" olarak kullanmak daha doğrudur.

# Değişken Tanımlama Şu Şekilde Kullanılabilir;

pi=3.14
print(pi)
3.14
print("pi")
pi

# Operatörler (İşlemler) = + (Toplama), - (Çıkarma), * (Çarpma), ** (Üs Alma), % (Mod Öğrenme (Kalan Öğrenme))
# Python3 Arayüzü Bir Nevi Hesap Makinesi Olarak Kullanılabilir. Hatta Bunu Değişkenlerle Destekleyebiliriz. Örneğin;

10+15
25
x=15
y=10
z=x+y
z=25

# "/" İşlemi Sonucu Her Zaman "float" Olur. Örneğin;

15/2
7.5
10/2
5.0

# Eğer "/" İşlemi Sonucu "integer" İsteniyorsa "//" Kullanılması Gerekir. Örneğin;

15//2
7
10//2
5

# Python3 Üzerinde String Toplaması Yapılabilir. Örneğin;

x="10"
y="15"
print(x+y)
1015

# Python3 Üzerinde String Çarpması Yapılabilir. Örneğin;

x="Yasin"
print(x*3)
YasinYasinYasin

***********************************************************************************************************************

# Kullanıcı Tarafından Veri Sağlamak İçin "Input" Komutu Kullanılır. Örneğin;

x=input("Sayı Girin")

# String İçinde Satır Atlanmak İstenirse; "\n" Kullanılır. Örneğin;

print("HelloWorld\nYasin Erarslan")

# Python Üzerinde Yorum Satırı "#" Komutu İle Sağlanır.
# "eval" Fonksiyonu "input" Komutu İle Alınan Girdinin Türüne Dönüştürmeyi Sağlar. Örneğin;

x=eval(input("Int, Str, Float Değerlerinden Birini Girin:"))
    # Kullanılan Fonksiyon Türümüz (Type) girdiye bağlı olarak değişecektir.

# Python3 Üzerinde Koşullu İfadeler Kullanılabilir. Bu İfadelere "boolean" Denir. "boolean" Sonucu Doğru yada Yanlış'dır.
# Farklı Bir Sonuç Vermez. İki Değişkeni Kıyaslamak Amacı İle Kullanılır. Bu İfadeler Şunlardır;
   # x==y (Eşit Mi?)
   # x!=y (Eşit Değil Mi?)
   # x>y (x, y'den Büyük Mü?)
   # x<y (x, y'den Küçük Mü?)
   # x>=y (x, y'den Büyük Eşit Mi?)
   # x<=y (x, y'den Küçük Eşit Mi?)

# Python3 Üzerinde Mantık Operatörleri Kullanılabilir. Bu İfadeler "and, or, not" Olarak Söylenebilir.
# Koşullu İfadelere ve Mantık Operatörlerine Örnek Verecek Olursak;

sayi=eval(input("Bir Sayı Giriniz:\n"))
if sayi>0:
   print("Sayı Pozitiftir...")
elif sayi==0:
   print("Sayı Sıfırdır...")
else:
   print("Sayı Negatiftir...")

# İç İçe "if" Kullanmak Yerine Yukarıdaki Örnek Gibi "elif" Komutu Kullanılanilir. İç İçe Kullanıma Örnek Olarak;

sayi = eval(input("Bir Sayı Giriniz:\n"))
if sayi > 0:
   print("Sayı Pozitiftir...")
else:
   if: x<0:
      print("Sayı Negatiftir...")
   else:
      print("Sayı Sıfırdır...")

***********************************************************************************************************************

# "try-except" Kullanmak Kullanıcıya Hata Sebebini Söylemeye Yarar. Programın Yarım Kalmasını Engellemek Amaçtır. Program Devam Etmelidir.

try:
    sıcaklıkf = eval(input("Lütfen Fahrenheit Değerini Giriniz:\n"))
    sıcaklıkc = (sıcaklıkf - 32) * 5 / 9
    print("Sıcaklık Değeriniz Celcius Cinsinden:", sıcaklıkc)
except:
    print("Lütfen Sadece Sayı Değeri Girin...")

# Döngüler başlığına giriş yapacak olursak birkaç amaç için kullanılabilir. Örn: Program Tekrarlamak...
# İlk işleyeceğimiz döngü "while" döngüsüdür. "while" değişkene bağlı olarak çalışır. Örneğin:

x = 3
while x > 0:
    print("X Pozitiftir...")
    # Kullanım maalesef yanlıştır. Çünkü x bu girdiye göre her zaman bellekte 3 olarak kalacaktır. "while" döngüsü her an gerçekleşmektedir.
    # Önlemek amacı ile aşağıdaki örnek kullanılabilir.

x = eval(input("Bir Sayı Girininz:\n"))
while x > 0:
    print("X Pozitiftir...")
    x = eval(input("Bir Sayı Girininz:\n"))
    # Gördüğümüz gibi program bittiği an kullanıcıdan yeni bir girdi istenmekte. Yani kullanıcının girdiğine göre program çalışacak ve duracaktır.
    # Bir örnek daha verecek olursak;

n = 5
while n > 0
    print(n)
    n = n - 1
print("Bitti...")

# Peki ya "while" döngüsünü bir değişkene bağlı çalıştırmak istemezsek ne olacak? Örneğin;

while True:
    satır = input("Değer Giriniz: ")
    if satır == "Bitti":
        break
    print(satır)
print("İşlem Tamamlandı...")

# İkinci işleyeceğimiz döngü "for" döngüsüdür. "for" bir aralık arasında tanımlıdır.

for x in range(5)
# Anlatılmak isenen şudur "Döngü 6 Kere Tekrar Edecektir.". x'e bir değişken atamak gerekmiyor. Çünkü "range" x'i her seferinde 1 arttırarak atama yapar.

for x in range(1, 5)
# Yukarıdaki örnekten farkımız şudur. x atama işlemi 1 ile 5 arasında yapılacaktır. x 1'den atanmaya başlanılacak 4'de duracaktır.

for x in range(5, 0, -1)
# Bu örnekte ise x değeri azaltılmak isteniyorsa kullanılır. x atama işlemi 5'den başlar ve 0'a kadar -1 olarak azalır.

***********************************************************************************************************************

# Fonksiyonlar
# Python3 üzerindeki her fonksiyon 'def' ile başlar. Bu fonksiyonlar 'random.py' dosyası içinde tanımlıdır.

# Random Modülü
# Random Fonksiyonu 0.0 (Dahil) ile 1.0 (Hariç) Arasında Rastgele Ondalık Sayı Üretir.

import random
for x in range(10):
    y=random.random()
    print(y)
    # 'randint(baslangic.bitis):' Başlangıç ve Bitiş dahil olmak üzere iki sayı arasında rastgele sayı üretir.

import random
for x in range(10):
    print(random.randint(1,10))

# Math Modülü
# Math Fonksiyonu neredeyse Tüm Matematiksel İşlemleri içerir.

import math
x=math.sin(90)
print(x)

# Fonksiyon Nasıl Yazılır Dersel;

def mesaj1():
    print("Merhaba Dünya :)")

def mesaj2():
    print("Hello World :)")

print("Size Bir Mesajım Var...")
mesaj1()
print("You Have A Message...")
mesaj2()

***********************************************************************************************************************

# Format Operatörü; ('%') String düzenlemelerinde kullanılır. Örneğin;

kedi=int(input("Kedi Sayısını Girin"))
print("Bahçede %d Kedi Gördüm" %kedi)
print("Son %d İçinde, Bahçedeki %s Sayısı %g Arttı" %(3,"kedi",0.8))

# %d Decimal demektir. (10'luk Taban)
# %s String demektir. (Karakter Dizisi)
# %g Float demektir. (Ondalık Sayı)

# Büyük Küçük A Bulucu
a=input("Gir: ")
a1="a"
a2="A"
sayack=0
sayacb=0
for x in range(len(a)):
    if a[x] in a1:
        sayack=sayack+1
    elif a[x] in a2:
        sayacb=sayacb+1

print("Küçük:",sayack,"Büyük:",sayacb)

# ID Oluşturucu
def ad():
    ad=input("Adınız: ")
    return ad

def soyad():
    soyad=input("Soyadınız: ")
    return soyad

def kimlik():
    tc=input("Kimlik Numaranız: ")
    return tc

def ilkuc(ad,soyad,tc):
    ID=""
    if len(ad)>3:
        aduc=ad[:3]
    else:
        aduc=ad
    if len(soyad)>3:
        soyaduc=soyad[:3]
    else:
        soyaduc=soyad
    if len(tc)>3:
        tcuc=tc[-3:]
    else:
        tcuc=tc
    IDNew=aduc+soyaduc+tcuc
    print(IDNew)

def main():
    adi=ad()
    soyadi=soyad()
    tci=kimlik()
    ilkuc(adi,soyadi,tci)

main()

# 'isalpha()' String sadece alfabetik karakterler içeriyorsa True döndürür.

x="HelloWorld"
if x.isalpha():
    print("Evet")
else:
    print("Hayır")

# 'isalnum()! String sadece alfabetik ve sayısal karakterler içeriyorsa True döndürür.

x="HelloWorld123"
if x.isalnum():
    print("Evet")
else:
    print("Hayır")

# 'isdigit()' String sadece sayısal karakterler içeriyorsa True döndürür.

x="123456789"
if x.isdigit():
    print("Evet")
else:
    print("Hayır")

# 'islower()' Stringdeki tüm alfabetik karakterler küçükse True döndürür.

x="helloworld"
if x.islower():
    print("Evet")
else:
    print("Hayır")

# 'isupper()' Stirngdeki tüm alfabetik karakterler büyükse True döndürür.

x = "HELLOWORLD"
if x.islower():
    print("Evet")
else:
    print("Hayır")

# 'isspace()' Stirng sadece whitespace (\n,\t, ,) içeriyorsa True döndürür.

x="\n \t"
if x.isspace():
    print("Evet")
else:
    print("Hayır")

# 'lower()' Stringdeki tüm alfabetik karakterlerin hepsini küçük karakterlere dönüştürüp çıktı verir.

x="HelloWorld"
x=x.lower()

# 'upper()' Stringdeki tüm alfabetik karakterlerin hepsini büyük karakterlere dönüştürüp çıktı verir.

x="HelloWorld"
x=x.upper()

# 'lstrip()' String'in başındaki whitespace karakterlerini temizler.

x=" HelloWorld"
x=x.lstrip()

# 'lstrip(char)' Char içine verilen değerleri String'in başından temizler.

x="HelloWorld"
x=x.lstrip("Hello")

# 'rstrip()' String'in sonundaki whitespace karakterlerini temizler.

x="HelloWorld "
x=x.lstrip()

# 'rstrip(char)' Char içine verilen değerleri String'in sonundan temizler.

x="HelloWorld"
x=x.lstrip("World")

# 'strip()' String'in hem başındaki hemde sonundaki whitespace karakterleri temizler.

x=" HelloWorld "
x=x.lstrip()

# 'strip(char)' String'in hem başındaki hemde sonundaki Char içine verilen değerleri temizler.

x="WorldHelloWorld"
x=x.lstrip("World")

# 'endswith(substring)' String'in sonundaki Substring'e bakar. Var ise True döndürür.

dosyaadi="YasinErarslan.txt"
if dosyaadi.endswith("txt"):
    print("Evet")
else:
    print("Hayır")

# 'find(substring)' String'in içinde aranan karakter dizisine bakar. Var ise bulunan konumun index numarasını döndürür.
# Bulamazsa '-1' döner.

x="HelloWorld"
print(x.find("ll"))

# 'replace(old,new)' String'deki bir karakteri başka bir karaktere dönüştürmek için kullanılır.

x="asdasdasd"
x=x.replace("a","A")

# 'startswith(substring)' String'in başındaki Substring'e bakar. Var ise True döndürür.

x="YasinErarslan.txt"
if x.startswith("Yasin"):
    print("Evet")
else:
    print("Hayır")

***********************************************************************************************************************

# Dosyaları Python3 üzerine eklemek için 'open("dosya_adi.uzanti")' fonksiyonu kullanılır. '.py' uzantılı Python
# programı ile eklenecek dosya aynı klasör içinde olmalıdır. Örneğin;

file=open("Deneme.txt")

# Dosya içideki tutlan verileri yazdırmak için yapılan en genel hata şudur;

file=open("Deneme.txt")
print(file)

# Bu hatanını önüne şu şekilde geçilir;

file=open("Deneme.txt")
content=file.read()
print(content)
# Kullandığımız 'read()' fonksiyonu dosya içindeki her bölümü bir string'e atar ve yazdırır.
# Atadığımız 'content' bir string olduğu için stringle kullandığımız her fonksiyonu kullanabiliriz.

# 3 Adet dosya açma metodu vardır. Bunlar;
# 'r' (read): Dosyayı okuma modunda açar.
file=open("Deneme.txt","r")

# 'w' (write): Dosyayı yazma modunda açar. Dosya oluşturulmuş ve içinde bir girdi varsa her girdiyi siler. Eğer dosya
# yoksa yeni bir dosya oluşturur.
file=open("Deneme.txt","w")

# 'a' (append): Dosyayı ekleme modunda açar. Dosya oluşturulmuş ve içinde bir girdi varsa sonuna ekler. Eğer dosya
# yoksa yeni bir dosya oluşturur.
file=open("Deneme.txt","a")

# Dosya ile yazdığımız Python uygulamamız farklı çalışma alanlarında ise Python'un o dosyayı açması için open()
# fonksiyonuna tam bir adres (konum) vermelisiniz. Şu şekilde kullanabiliriz;

file=open(r"/home/mustachedocto/WorkSpace/Deneme.txt","r")
#         |
#        "r:raw string demektir."

# Eğer dosyaya veri yazdırmak istersek 'write()' komutu kullanılır. Örneğimiz ise şu şekilde olur;

file=open("Ünlüler.txt","w")
file.write("Zeki Müren\n")
file.write("Seda Sayan\n")
file.write("Ferdi Tayfur\n")
file.close()
#    ~~~~~~~
#       |
#    'close()', Dosyayı kapatmak için kullanılan bir fonksiyondur.

# 'readline()' fonksiyonu ile dosya içeriğini satır satır okumak için kullanılır.

file=open("Ünlüler.txt")
line1=file.readline()
print(line1.rstirp())
line2=file.readline()
print(line2.rstrip())
file.close()