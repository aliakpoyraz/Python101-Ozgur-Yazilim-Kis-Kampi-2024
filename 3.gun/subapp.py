import random

def defaultParolaOlusturma(adi, soyadi, ogrenciNu, telefonNu):
    son2Ad = adi[-2:]
    son2Soyisim = soyadi[-2:]
    son2OgrNu = ogrenciNu[0:2]
    son34TelNo = telefonNu[6:8]

    sondeger = [son2Ad, son2Soyisim, son2OgrNu, son34TelNo]
    aList = [0, 1, 2, 3]
    sonucParola = []

    for i in range(0,4):
        a = random.choice(aList)
        aList.remove(a)
        parolalist = sondeger[a]
        sonucParola.append(parolalist)

    parolaString = ""
    for i in sonucParola:
        parolaString += "{}".format(i)

    return parolaString


# generated_parola = defaultParolaOlusturma("Ali", "Akpoyraz", "7777", "5346577777")
# print("Parola Sonucu:", generated_parola)
