maas = float ( input("Maaşınızı Giriniz: "))
medeni = str (input("\nBekar iseniz B veya b Evliyseniz E veya e Giriniz: "))
if medeni == 'E' or 'e':
    medenimaas = maas*0.07
    print("\nEvli Olduğunuz İçin %7 Zam Aldınız.")
elif medeni == 'B' or 'b':
    medenimaas = maas*0.04
    print("\nBekar Olduğunuz İçin %4 Zam Aldınız.")

cocuksayisi = float ( input("\nÇocuk sayısını giriniz: ") ) 
if cocuksayisi == 0 :
    cocukmaas = maas*0.02
    print("\nÇocuğunuz Olmadığı İçin %2 Zam Aldınız.")
elif cocuksayisi == 1:
    cocukmaas = maas*0.05
    print("\n1 Çocuğunuz olduğu İçin %5 Zam Aldınız.")
elif cocuksayisi == 2 or cocuksayisi == 3:
    cocukmaas = maas*0.08
    print("\n2 veya 3 Çocuğunuz olduğu İçin %8 Zam Aldınız.")
elif cocuksayisi > 3:
    cocukmaas = maas*0.1
    print("\n3 Den  Çocuğunuz olduğu İçin %10 Zam Aldınız.")

calismasuresi = int ( input("\nÇalışma Sürenizi Giriniz (AY OLARAK): ") )
if calismasuresi <= 12:
    calismamaas = maas*0.05
    print("\n12 Ay İçin %5 Zam Aldınız.")
elif calismasuresi <= 36:
    calismamaas = maas*0.1
    print("\n12+ Ay İçin %10 Zam Aldınız.")
elif calismasuresi <= 72:
    calismamaas = maas*0.15
    print("\n36+ Ay İçin %15 Zam Aldınız.")
elif calismasuresi > 72:
    calismamaas = maas*0.2
    print("\n72+ Ay İçin %20 Zam Aldınız.")
yenimaas = maas + medenimaas + cocukmaas + calismamaas
print("\n\n\nYeni Maaşınız: " , yenimaas)



