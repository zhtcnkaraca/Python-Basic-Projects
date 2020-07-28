import datetime
def Topla(x, y):
   return x + y
 
def Cikar(x, y):
   return x - y
 
def Carp(x, y):
   return x * y
 
def Bol(x, y):
   return x / y

def hesapmakinesi():
   print("Yapılacak İşlemi Seçin.")
   print("=======================")
   print("1.Toplama")
   print("2.Çıkarma")
   print("3.Çarpma")
   print("4.Bölme")
   secim = input("Seçiminiz (1/2/3/4):")
   sayi1 = int(input("1. Sayı: "))
   sayi2 = int(input("2. Sayı: "))
   if secim == '1':
      print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
      mainmenu()
   elif secim == '2':
      print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))
      mainmenu()
   elif secim == '3':
      print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2))
      mainmenu()
   elif secim == '4':
      print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
      mainmenu()
   else:
      print("Geçersiz Giriş")
      mainmenu()

def burcogrenme():
   print("=======================")
   a=int(input('Doğdugunuz günü giriniz: '))
   b=int(input('Doğdugunuz ayı sayı olarak giriniz: '))

   if ((a>20) & (b==3)) or ((a<21) & (b==4)):
      y='Koç'
   elif ((a>20) & (b==4)) or ((a<21) & (b==5)):
      y='Boğa'
   elif ((a>20) & (b==5)) or ((a<22) & (b==6)):
      y='İkizler'
   elif ((a>21) & (b==6)) or ((a<23) & (b==7)):
      y='Yengeç'
   elif ((a>22) & (b==7)) or ((a<23) & (b==8)):
      y='Aslan'
   elif ((a>22) & (b==8)) or ((a<23) & (b==9)):
      y='Başak'
   elif ((a>22) & (b==9)) or ((a<24) & (b==10)):
      y='Terazi'
   elif ((a>23) & (b==10)) or ((a<23) & (b==11)):
      y='Akrep'
   elif ((a>22) & (b==11)) or ((a<22) & (b==12)):
      y='Yay'
   elif ((a>21) & (b==12)) or ((a<21) & (b==1)):
      y='Oğlak'
   elif ((a>20) & (b==1)) or ((a<19) & (b==2)):
      y='Kova'
   elif ((a>18) & (b==2)) or ((a<21) & (b==3)):
      y='Balık'

   print('Burcunuz: {}'.format(y))
   mainmenu()


def uninothesaplama():
   print("=======================")
   vize = input('Vize Notunuz : ')
   final = input('Final Notunuz : ')
   ortalama=(float(vize)*0.4)+(float(final)*0.6)
   print("Ortalama :{0} ".format(ortalama))
   mainmenu()




def lisenothesaplama():
   y1 = input('1. Yazılı : ')
   y2 = input('2. Yazılı : ')
   y3 = input('3. Yazılı : ')
   ortalama=(float(y1)+float(y2)+float(y3))/3
   print("Ortalama :{0} ".format(ortalama))
   mainmenu()


def mainmenu():
   print("Yapmak istediğiniz işlemi seçiniz")
   print("1) Burç Ogrenme")
   print("2) Hesap Makinesi")
   print("3) Universite Not Hesaplama")
   print("4) Lise Not Hesaplama")
   secim = input("Islem: ")
   if secim =='1':
      burcogrenme()
   elif secim =='2':
      hesapmakinesi()
   elif secim == '3':
      uninothesaplama()
   elif secim == '4':
      lisenothesaplama()
   else:
      print("Geçersiz giriş!")

mainmenu()