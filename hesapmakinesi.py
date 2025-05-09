print("🧮Hesap Makinesi 🧮")

# Kullanıcıdan sayıları al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlem seçimi
print("\nYapmak istediğiniz işlemi seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminiz (1/2/3/4): ")

# Hesaplama kısmı
if secim == '1':
    print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
elif secim == '2':
    print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
elif secim == '3':
    print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")
elif secim == '4':
    if sayi2 != 0:
        print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Hata: Bir sayıyı 0'a bölemezsiniz!")
else:
    print("Geçersiz seçim yaptınız.")
