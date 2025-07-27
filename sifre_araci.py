import base64

def sifrele(metin):
    return base64.b64encode(metin.encode()).decode()

def coz(metin):
    return base64.b64decode(metin.encode()).decode()

print("🔐 1. Şifrele\n🔓 2. Çöz")
secim = input("Seçimin (1/2): ")

if secim == "1":
    veri = input("Şifrelenecek metni gir: ")
    print("Sonuç:", sifrele(veri))
elif secim == "2":
    veri = input("Çözülecek metni gir: ")
    try:
        print("Sonuç:", coz(veri))
    except:
        print("Hatalı veya geçersiz veri!")
else:
    print("Geçersiz seçim!")
