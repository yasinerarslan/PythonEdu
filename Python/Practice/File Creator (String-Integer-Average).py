def filew(filename,entry):
    file=open(r"/home/mustachedocto/Belgeler/%s.txt" %filename,"w")
    file.write(entry)
    file.close()

def filer(filename):
    file=open(r"/home/mustachedocto/Belgeler/%s.txt" %filename,"r")
    content=file.read()
    print("Dosya İçeriği:\n",content)
    file.close()

def randomint(filename):
    import random
    file=open(r"/home/mustachedocto/Belgeler/%s.txt" %filename,"w")
    loop=int(input("Kaç Adet Sayı Üretmek İstiyorsunuz: "))
    for counter in range(loop+1):
        number=random.randint(1,100)
        file.write(str(number)+"\n")
    file.close()
    return loop

def integer():
    filename=input("Lütfen Oluşturulacak Dosya Adını Belirtin: ")
    loop=randomint(filename)
    filer(filename)
    return filename,loop

def string():
    filename=input("Lütfen Oluşturulacak Dosya Adını Belirtin: ")
    entry=""
    button="1"
    while button=="1":
        e=input("Lütfen Dosya İçine Ne Yazmak İstediğinizi Belirtin: ")
        button=input("Yeni Girdi İçin '1', Bitirmek İçin '2' Tuşlayınız: ")
        if button=="1":
            entry=entry+e+"\n"
        else:
            entry=entry+e
    filew(filename,entry)
    filer(filename)

def average(filename,loop):
    file=open(r"/home/mustachedocto/Belgeler/%s.txt" %filename,"r")
    count=0
    for counter in range(loop+1):
        number=file.readline()
        number=number.rstrip()
        number=int(number)
        count=count+number
    averagenumber=count/loop
    print("Ortalamanız:",averagenumber)

def menu():
    print("Rastgele Sayı Oluşturmak ve Ortalama Hesaplamak İçin '1', Girdi İçin '2' Tuşlayın...")
    operation=input("İşleminiz Nedir: ")
    return operation

def main():
    operation=menu()
    if operation=="1":
        filename,loop=integer()
        average(filename,loop)
    else:
        string()

main()