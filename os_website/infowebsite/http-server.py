from http.server import SimpleHTTPRequestHandler, HTTPServer
from socketserver import TCPServer



# Belirlediğiniz port numarası
port = 8000
handler = SimpleHTTPRequestHandler
directory = "/home/pi/python101/app"
handler.directory = directory# HTTP sunucu başlat
with TCPServer(("", port), handler) as httpd:
    print(f"Sunucu {port} portunda çalışıyor...")
    SimpleHTTPRequestHandler.directory = directory

    try:
        # İstemcileri bekleyerek sunucuyu çalışır durumda tut
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Ctrl+C ile kesilirse sunucuyu kapat
        print("\nSunucu kapatılıyor.")
        httpd.shutdown()
