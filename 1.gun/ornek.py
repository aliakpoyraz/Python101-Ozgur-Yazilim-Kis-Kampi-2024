fiyat = float (input("Ürün Fiyatını Giriniz: "))
masraf = fiyat*0.03 + fiyat*0.2 + fiyat*0.015
satis = (fiyat+masraf) + (fiyat+masraf)*0.2
print("Satış Fiyatı: " , satis)