# Medical AI Assistant

AI-powered medical assistant chatbot built with LangChain and OpenAI for healthcare consultation support.

## 📋 Proje Açıklaması

Bu projede kullanıcıların sağlık ile ilgili sorularını anlayan ve yanıtlayan GPT tabanlı bir doktor asistanı chatbot'u geliştirilmektedir. Sistem kullanıcının yaşını ve adını dikkate alarak kişiselleştirilmiş cevaplar üretir ve mesaj geçmişini hatırlayarak diyaloğu sürdürür.

## 🎯 Proje Hedefleri

- **Kişiselleştirilmiş Sağlık Danışmanlığı**: Kullanıcının yaş ve isim bilgilerine göre özelleştirilmiş tavsiyeler
- **Konuşma Hafızası**: Geçmiş mesajları hatırlayan akıllı diyalog sistemi
- **Gerçek Zamanlı AI**: OpenAI GPT-3.5 Turbo ile anlık sağlık önerileri
- **Aşamalı Geliştirme**: Terminal → Web Servisi → Client Uygulaması

## 🏗️ Proje Aşamaları

### ✅ Aşama 1: Terminal Uygulaması (Tamamlandı)
Komut satırından çalışan temel chatbot

### ✅ Aşama 2: Web Servisi (Tamamlandı)
FastAPI tabanlı REST API servisi

### ✅ Aşama 3: Client Uygulaması (Tamamlandı)
Web arayüzü ile kullanıcı dostu interface

### 📱 Aşama 4: Web Arayüzü (Planlanan)
HTML/CSS/JavaScript ile kullanıcı dostu web interface

## 🛠️ Teknolojiler

- **LangChain**: LLM kütüphanesi, prompt yönetimi ve memory sistemi
- **OpenAI GPT-3.5 Turbo**: Ana dil modeli
- **Python-dotenv**: Çevre değişkenleri yönetimi
- **FastAPI**: Web API framework 
- **Uvicorn**: ASGI server 
    
## 📦 Kurulum

### Gereksinimler
```bash
pip install langchain
pip install langchain-openai
pip install openai
pip install python-dotenv
pip install fastapi
pip install uvicorn
```

### Çevre Değişkenleri
`.env` dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Kullanım

### Terminal  Uygulaması
```bash
python doctor_assistant_terminal.py
```

Program başladığında:
1. Adınızı girin
2. Yaşınızı girin
3. Sağlık sorularınızı sorun
4. Çıkmak için `quit` yazın

### Örnek Kullanım
```
Adiniz: Ahmet
Yasiniz: 35

Merhaba ben bir doktor asistanıyım, size nasıl yardımcı olabilirim.

Ahmet: Baş ağrım var, ne yapmalıyım?
Doktor Asistanı: Merhaba Ahmet, 35 yaşında bir yetişkin olarak baş ağrınız için...
```

### FastAPI Web Servisi

```bash
uvicorn doctor_assistant_api:app --reload
```

Servis başladıktan sonra:

- API Documentation: http://127.0.0.1:8000/docs (Swagger UI)

### API Kullanım Örneği

Request:

```json
{
  "name": "Ahmet",
  "age": 35,
  "message": "Baş ağrım var, ne yapmalıyım?"
}
```

Response:

```json
{
  "response": "Merhaba Ahmet, 35 yaşında bir yetişkin olarak baş ağrınız için..."
}
```

### Terminal Client Uygulaması

```bash
# Terminal 1: API sunucusunu başlatın
uvicorn doctor_assistant_api:app --reload

# Terminal 2: Client'ı çalıştırın
python client_test.py
```

Program başladığında:

- Adınızı girin
- Yaşınızı girin
- API sunucusu ile sohbet edin
- Çıkmak için quit yazın

Not: Client çalıştırmadan önce FastAPI sunucusunun çalışıyor olması gerekir:



## 🧠 Sistem Özellikleri

### Memory Sistemi
- Konuşma geçmişini hatırlar
- Kullanıcı bilgilerini (isim, yaş) korur
- Bağlamsal cevaplar üretir
- Session bazlı hafıza yönetimi

### Kişiselleştirme
- Yaşa uygun tavsiyeler
- İsimle hitap etme
- Bireysel sağlık durumu dikkate alma

### API Özellikleri
RESTful API tasarımı
Pydantic ile veri validasyonu
Swagger UI dokümantasyonu
Asenkron request handling
Hata yönetimi ve HTTP status kodları

### Güvenlik
- Dikkatli ve nazik tavsiyeler
- Profesyonel sağlık yaklaşımı
- Uygun uyarılar ve yönlendirmeler

## 📁 Proje Yapısı

```
medical-ai-assistant/
├── doctor_assistant_terminal.py    # Standalone terminal uygulaması
├── doctor_assistant_api.py         # FastAPI web servisi
├── client_test.py                  # Terminal API client
├── .env                           # API anahtarları (git'e eklenmez)
├── .gitignore                     # Git ignore dosyası
├── README.md                      # Bu dosya
└── requirements.txt               # Python bağımlılıkları 
```

## ⚙️ Konfigürasyon

### LLM Ayarları
- **Model**: GPT-3.5 Turbo
- **Temperature**: 0.7 (yaratıcılık vs güvenilirlik dengesi)
- **Memory**: ConversationBufferMemory (tam konuşma geçmişi)

### FastAPI Ayarları

- Host: 127.0.0.1
- Port: 8000
- Reload: Geliştirme modunda otomatik yeniden yükleme

### Prompt Sistemi
```python
intro = (
    f"Sen bir doktor asistanısın. Hasta {name}, {age} yaşında. "
    "Sağlık konuları hakkında konuşmak istiyor. " 
    "Yaşına uygun dikkatli ve nazik tavsiyeler ver; ismiyle hitap et." 
)
```

## 🧪 Test

### Swagger UI ile Test

- `uvicorn doctor_assistant_api:app --reload` ile servisi başlatın
- http://127.0.0.1:8000/docs adresine gidin
- "Try it out" butonuna tıklayın
- Request body'yi doldurun ve "Execute" yapın


## 🔮 Gelecek Planları

- [ ] FastAPI web servisi geliştirme
- [ ] RESTful API endpoint'leri
- [ ] Web tabanlı kullanıcı arayüzü
- [ ] Veritabanı entegrasyonu
- [ ] Kullanıcı kimlik doğrulama
- [ ] Çoklu dil desteği

## ⚠️ Önemli Notlar

- Bu sistem gerçek tıbbi teşhis veya tedavi yerine geçmez
- Acil durumlarda mutlaka sağlık kuruluşuna başvurun
- AI tavsiyelerini bir sağlık profesyoneli ile doğrulayın

## 📄 Lisans

Bu proje MIT lisansı altında geliştirilmektedir.

## 🤝 Katkıda Bulunma

Proje henüz geliştirme aşamasındadır. 

---

**Not**: Bu proje eğitim amaçlı geliştirilmektedir ve gerçek tıbbi danışmanlık yerine geçmez.