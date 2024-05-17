adim = "Ali"
soyadim = "Akpoyraz"
yasim = "21"
dogumtarihim = "25.02.2003" 
print("Benim Adim :" , adim)
print("Soyadim :" , soyadim)
print("Yasim :" , yasim)
print("Dogum Tarihim : " , dogumtarihim)
#######
topluMetin = ("Benim Adim %s , Soyadim %s , %s Tarihinde Dogdum , %s yasindayim" % (adim,soyadim,dogumtarihim,yasim))
print(topluMetin)
#######
topluMetin2 = "\nBenim Adim {0} , Soyadim {1} , {2} yasindayim , {3} Tarihinde Dogdum".format(adim,soyadim,yasim,dogumtarihim)
print(topluMetin2)

metin1 = "Adım %s" % adim
metin2 = "soyadim {}".format(soyadim)
print(metin1,metin2)



ad = "ali akpoyraz"
yil = 2024
gun = "sali"
ay = "ocak"
sure = 4
toplu = "Eğitim {0} gününde {1} ayında {2}'te oldu.".format(gun,ay,yil)
toplu2 = "Eğitmen {0} eğitimi verdi ve {1} gün sürdü.".format(ad,sure)
print(toplu,toplu2)
