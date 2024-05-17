from random import randint

x = randint(0, 20)
sayac = 0
kontrol = True
print(x)

while kontrol and sayac < 5:
    y = int(input("Sayı Tahmin Etme Oyunu \n[0-20] Bir Tahminde Bulun: "))
    if x == y:
        kontrol = False
        print("Doğru Tahmin!")
    elif x < y:
        print("Girdiğiniz Değer Belirlenen Sayıdan Küçüktür.")
    elif x > y:
        print("Girdiğiniz Değer Belirlenen Sayıdan Büyüktür.")
    
    sayac += 1

if sayac == 5 and kontrol:
    print("Tahmin Hakkınız Doldu!")
