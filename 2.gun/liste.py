sayilar = [1,42,67,86,88,44,42,2,67]
yunikSayilar = []
aynidegerolanlar = list()
for i in sayilar:
    
    if i not in yunikSayilar:
        yunikSayilar.append(i)
    else:
        aynidegerolanlar.append(i)
        yunikSayilar.remove(i)
print("Yunik Değerler: ", yunikSayilar)
print("Aynı Değer Olanlar", aynidegerolanlar)

 
    