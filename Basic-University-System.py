ogrenciler = []
dersler = []

def tireKoy():
    print("-------------------------")

def ogrenciMenusu():
    while True:
        tireKoy()
        print("1)OGRENCI MENUSU")
        tireKoy()
        print("1-) OGRENCI EKLE")
        print("2-) OGRENCILERI LISTELE")
        print("3-) OGRENCI SIL")
        print("g-) GERI DON")
        print("c-) CIKIS")
        ogrenciMenusuIslem = input("İşlem Seçiniz: ")
        if ogrenciMenusuIslem == "1":
            ogreciEkle()
            break
        elif ogrenciMenusuIslem == "2":
            ogreciListele()
            break
        elif ogrenciMenusuIslem == "3":
            ogrenciSil()
            break
        elif ogrenciMenusuIslem == "g":
            anaMenu()
            break
        elif ogrenciMenusuIslem == "c":
            break
        else:
            print("Hatalı Giriş. Tekrar Deneyiniz.")

def ogreciEkle():
    while True:
        tireKoy()
        print("1.1-)OGRENCI EKLE")
        tireKoy()
        ogrenciAdi = input("Ogrenci Adını Giriniz: ")
        if ogrenciAdi == "":
            print("Boş Geçilemez")
        else:
            ogrenciler.append(ogrenciAdi)
            ogrenciMenusu()
            break
        tireKoy()
    
def ogreciListele():
    while True:
        tireKoy()
        print("1.2-)OGRENCILERI LISTELE")
        tireKoy()
        numara = 1
        for ogrenci in ogrenciler:
            print( numara,"-)",ogrenci)
            numara+=1
        print("g-) GERI DON")
        print("c-) CIKIS")
        ogrenciListeleIslem = input("İşlem Seçiniz: ")
        if ogrenciListeleIslem =="":
            print("Boş geçilemez.")
        elif ogrenciListeleIslem == "g":
            ogrenciMenusu()
            break
        elif ogrenciListeleIslem == "c":
            break
        else:
            print("Hatalı Giriş. Tekrar Deneyiniz.")

def ogrenciSil():
    while True:
        tireKoy()
        print("1.3-)OGRENCI SIL")
        tireKoy()
        numara = 1
        for ogrenci in ogrenciler:
            print( numara,"-)",ogrenci)
            numara+=1
        print("g-) GERI DON")
        print("c-) CIKIS")
        try:
            ogrenciSilIslem = input("Silmek İsteddiğiniz Öğrenciyi Seçiniz: ")
            if ogrenciSilIslem == "":
                print("Bir seçim yapınız.")
            elif ogrenciSilIslem == "g":
                ogrenciMenusu()
                break
            elif ogrenciSilIslem == "c":
                break
            elif type(int(ogrenciSilIslem)) == int:
                ogrenciler.pop(int(ogrenciSilIslem)-1)
                print("Seçili öğrenci silindi")
            else:
                print("Hatalı Giriş. Tekrar Deneyiniz.")
        except:
            print("Hatalı Giriş. Tekrar Deneyiniz.")
        
def dersMenusu():
    while True:
        tireKoy()
        print("2)DERS MENUSU")
        tireKoy()
        print("1-) DERS EKLE")
        print("2-) DERSLERI LISTELE")
        print("3-) DERS SIL")
        print("g-) GERI DON")
        print("c-) CIKIS")
        dersMenusuIslem = input("İşlem Seçiniz: ")
        if dersMenusuIslem == "1":
            dersEkle()
            break
        elif dersMenusuIslem == "2":
            dersListele()
            break
        elif dersMenusuIslem == "3":
            dersSil()
            break
        elif dersMenusuIslem == "g":
            anaMenu()
            break
        elif dersMenusuIslem == "c":
            break
        else:
            print("Hatalı Giriş. Tekrar Deneyiniz.")

def dersEkle():
    while True:
        tireKoy()
        print("2.1-)DERS EKLE")
        tireKoy()
        dersAdi = input("Ders Adını Giriniz: ")
        if dersAdi == "":
            print("Boş Geçilemez")
        else:
            dersler.append(dersAdi)
            dersMenusu()
            break
        tireKoy()
    
def dersListele():
    while True:
        tireKoy()
        print("2.2-)DERSLERI LISTELE")
        tireKoy()
        numara = 1
        for ders in dersler:
            print( numara,"-)",ders)
            numara+=1
        print("g-) GERI DON")
        print("c-) CIKIS")
        dersListeleIslem = input("İşlem Seçiniz: ")
        if dersListeleIslem =="":
            print("Boş geçilemez.")
        elif dersListeleIslem == "g":
            dersMenusu()
            break
        elif dersListeleIslem == "c":
            break
        else:
            print("Hatalı Giriş. Tekrar Deneyiniz.")

def dersSil():
    while True:
        tireKoy()
        print("2.3-)DERS SIL")
        tireKoy()
        numara = 1
        for ders in dersler:
            print( numara,"-)",ders)
            numara+=1
        print("g-) GERI DON")
        print("c-) CIKIS")
        try:
            dersSilIslem = input("Silmek İsteddiğiniz Öğrenciyi Seçiniz: ")
            if dersSilIslem == "":
                print("Bir seçim yapınız.")
            elif dersSilIslem == "g":
                dersMenusu()
                break
            elif dersSilIslem == "c":
                break
            elif type(int(dersSilIslem)) == int:
                dersler.pop(int(dersSilIslem)-1)
                print("Seçili öğrenci silindi")
            else:
                print("Hatalı Giriş. Tekrar Deneyiniz.")
        except:
            print("Hatalı Giriş. Tekrar Deneyiniz.")
           
def hesaplamaMenusu():
    while True:
        tireKoy()
        print("2)HESAPLAMA MENUSU")
        tireKoy()
        print("1-) NOT HESABI")
        print("g-) GERI DON")
        print("c-) CIKIS")
        hesaplaMenusuIslem = input("İşlem Seçiniz: ")
        if hesaplaMenusuIslem == "1":
            notHesabi()
            break
        elif hesaplaMenusuIslem == "g":
            anaMenu()
            break
        elif hesaplaMenusuIslem == "c":
            break
        else:
            print("Hatalı Giriş. Tekrar Deneyiniz.")

def notHesabi():
    while True:
        tireKoy()
        print("3.1-)NOT HESABI")
        tireKoy()
        try:
            vize = int(input("Vize Notunuzu Giriniz: "))
            final = int(input("Final Notunuzu Giriniz: "))
            if vize == "" or final == "":
                print("Boş Geçilemez")
            elif type(vize) == int and type(final) == int:
                dersNotu = (vize*0.4) + (final*0.6)
                print("Ders Notu: ", dersNotu)
                if dersNotu >=95 and dersNotu <=100:
                    print("Dersi Geçti: A+")
                elif dersNotu >=90 and dersNotu <=94:
                    print("Dersi Geçti: A-")
                elif dersNotu >=85 and dersNotu <=89:
                    print("Dersi Geçti: B+")
                elif dersNotu >=80 and dersNotu <=84:
                    print("Dersi Geçti: B")
                elif dersNotu >=75 and dersNotu <=79:
                    print("Dersi Geçti: B-")
                elif dersNotu >=70 and dersNotu <=74:
                    print("Dersi Geçti: C+")
                elif dersNotu >=65 and dersNotu <=69:
                    print("Dersi Geçti: C")
                elif dersNotu >=60 and dersNotu <=64:
                    print("Dersi Geçti: C-")
                elif dersNotu >=0 and dersNotu <=59:
                    print("Dersi Geçemedi: F")
                hesaplamaMenusu()
                break
            
            else:
                print("Hatalı Giriş. Tekrar Deneyiniz.")
            tireKoy()
        except:
            print("Hatalı Giriş. Tekrar Deneyiniz.")

def anaMenu():
    while True:
        tireKoy()
        print("MEBIS CLI 2020")
        tireKoy()
        print("ANA MENU")
        tireKoy()
        print("1-) OGRENCI MENUSU")
        print("2-) DERSLER MENUSU")
        print("3-) HESAPLAMALAR")
        print("c-) CIKIS")
        anaMenuIslem = input("Islem Seciniz: ")
        if anaMenuIslem == "1":
            ogrenciMenusu()
            break
        elif anaMenuIslem == "2":
            dersMenusu()
            break
        elif anaMenuIslem == "3":
            hesaplamaMenusu()
            break
        elif anaMenuIslem == "c" or anaMenuIslem =="C":
            break
        else:
            print("Hatalı Giriş. Tekrar Deneyiniz.")

while True:
    anaMenu()
    break
    
print("Program Kapandı")