# Medical AI Assistant

AI-powered medical assistant chatbot built with LangChain and OpenAI for healthcare consultation support.

## 📋 Proje Açıklaması

Bu projede kullanıcıların sağlık ile ilgili sorularını anlayan ve yanıtlayan GPT tabanlı bir doktor asistanı chatbot'u geliştirilmektedir. Sistem kullanıcının yaşını ve adını dikkate alarak kişiselleştirilmiş cevaplar üretir ve mesaj geçmişini hatırlayarak diyalogu sürdürür.

## 🎯 Proje Hedefleri

- **Kişiselleştirilmiş Sağlık Danışmanlığı**: Kullanıcının yaş ve isim bilgilerine göre özelleştirilmiş tavsiyeler
- **Konuşma Hafızası**: Geçmiş mesajları hatırlayan akıllı diyalog sistemi
- **Gerçek Zamanlı AI**: OpenAI GPT-3.5 Turbo ile anlık sağlık önerileri
- **Aşamalı Geliştirme**: Terminal → Web Servisi → Client Uygulaması

## 🏗️ Proje Aşamaları

### ✅ Aşama 1: Terminal Uygulaması (Mevcut)
Komut satırından çalışan temel chatbot

### 🔄 Aşama 2: Web Servisi (Planlanan)
FastAPI tabanlı REST API servisi

### 📱 Aşama 3: Client Uygulaması (Planlanan)
Web arayüzü ile kullanıcı dostu interface

## 🛠️ Teknolojiler

- **LangChain**: LLM kütüphanesi, prompt yönetimi ve memory sistemi
- **OpenAI GPT-3.5 Turbo**: Ana dil modeli
- **Python-dotenv**: Çevre değişkenleri yönetimi
- **FastAPI**: Web API framework (gelecek aşamalar için)
- **Uvicorn**: ASGI server (gelecek aşamalar için)

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

### Terminal Uygulaması
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

## 🧠 Sistem Özellikleri

### Memory Sistemi
- Konuşma geçmişini hatırlar
- Kullanıcı bilgilerini (isim, yaş) korur
- Bağlamsal cevaplar üretir

### Kişiselleştirme
- Yaşa uygun tavsiyeler
- İsimle hitap etme
- Bireysel sağlık durumu dikkate alma

### Güvenlik
- Dikkatli ve nazik tavsiyeler
- Profesyonel sağlık yaklaşımı
- Uygun uyarılar ve yönlendirmeler

## 📁 Proje Yapısı

```
medical-ai-assistant/
├── doctor_assistant_terminal.py    # Ana terminal uygulaması
├── .env                           # API anahtarları (git'e eklenmez)
├── .gitignore                     # Git ignore dosyası
├── README.md                      # Bu dosya
└── requirements.txt               # Python bağımlılıkları (yakında)
```

## ⚙️ Konfigürasyon

### LLM Ayarları
- **Model**: GPT-3.5 Turbo
- **Temperature**: 0.7 (yaratıcılık vs güvenilirlik dengesi)
- **Memory**: ConversationBufferMemory (tam konuşma geçmişi)

### Prompt Sistemi
```python
intro = (
    f"Sen bir doktor asistanısın. Hasta {name}, {age} yaşında. "
    "Sağlık konuları hakkında konuşmak istiyor. " 
    "Yaşına uygun dikkatli ve nazik tavsiyeler ver; ismiyle hitap et." 
)
```

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