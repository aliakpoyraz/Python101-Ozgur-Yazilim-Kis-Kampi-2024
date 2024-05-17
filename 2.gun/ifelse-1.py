#username = input("Kullanici Adinizi Giriniz: ")
#password = input("Şifrenizi Giriniz: ")
#if (username == "admin") & (password == "admin123."):
 #   print("Giris Yaptınız.")
#else:
 #   print("K.adi veya Sifreniz Yanlis.")

kGirdiKAdi = input("Kullanıcı Adınızı Giriniz: ")
kGirdiParola = input("Şifrenizi Giriniz: ")
kAdi = "admin"
kParola = "admin123"

if kGirdiKAdi == kAdi and kGirdiParola == kParola:
    print("Giriş Başarılı.")
elif kGirdiKAdi != kAdi and kGirdiParola == kParola:
    print("Kullanıcı Adınız Yanlış.")
elif kGirdiKAdi == kAdi and kGirdiParola != kParola:
    print("Parolanız Yanlış.")
else:
    print("Kullanıcı Adı ve Şifre Hatalı.")


