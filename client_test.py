"""
terminal uzerinden fastapi ile surekli sohbet (post olarak)
api endpoint: /chat
"""

import requests   # http istekleri yapmak icin kullanilan kutuphane

# api adresi 
API_URL = "http://127.0.0.1:8000/chat" # fast api sunucumuzun calistigi adres ve endpoint

# kullanici bilgilerini al isim ve yas
while True:
    name = input("Adınız: ").strip()
    if len(name) >= 2 and name.replace(" ", "").isalpha():
        break
    print("En az 2 harfli geçerli bir ad girin!")


while True:
    try:
        age = int(input("Yaşınız: ").strip())
        if 1 <= age <= 120:
          break
        else:
          print("Yaş 1-120 arasında olmalıdır!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")


print("\n Sohbet basladi. Cikmak için quit yazın")


# Bir dongu olustur, kullanicidan mesaj al ve sunucuya gonder. 
while True: 
  user_msg = input(f"{name}: ").strip()
  if not user_msg:
    print("Lütfen bir mesaj yazın.")
    continue

  if user_msg.lower() in ["quit", "exit", "çık"] : # konusmayi sonlandir. 
    print("Sana yardımcı olabildiysem ne mutlu bana, görüşmek üzere")
    break

  # API' ya gonderilecek veri paketi json 
  payload = {
    "name": name, 
    "age": age,
    "message": user_msg
  }

  try:
    # fastapi sunucusuna post istegi atalim. 30 saniye bekleyelim.
    res = requests.post(API_URL, json=payload, timeout=30)

    # eger istek basarili ise (200), yanit icinde responce kodu yazdirilir. 
    if res.status_code == 200:
      print(f"Doktor Asistanı: {res.json()["response"]}")
    else:
      print("hata", res.status_code, res.text)
  except requests.exceptions.RequestException as e: 
    print("baglanti hatasi: ", e)







