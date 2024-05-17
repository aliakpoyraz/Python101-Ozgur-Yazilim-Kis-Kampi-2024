#Adınız Sevdiğiniz bir hayvan okulunuz ve bir doğru bir yanlışınızı yazınız


ad = input("Adiniz: ")
hayvan = input("Sevdiginiz bir hayvan: " )
okul = input("Okulunuz: " )
dogru = input("Bir Dogrunuz: ")
yanlis = input("Bir Yanlisiniz: ")

toplu = ("Adiniz: %s \n Sevdiğiniz Hayvan:  %s \n Okulunuz:  %s \n Doğrunuz: %s \n Yanlisiniz: %s" % (ad,hayvan,okul,dogru,yanlis) ) 
print(toplu)