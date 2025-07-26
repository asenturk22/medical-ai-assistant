"""
İlk yapilacak asistan terminalden calistirilacak. Sonrasinda servise çevirilecek. 

Problem tanimi : 
    - Kullanicinin saglikla ilgili sorularini anlayan ve yanitlayan GPT tabanli bir doktor assistani bir chatbot'u dur. 
    - Kullanicinin "yasini" ve "adini" dikkate alan cevaplar uretsin
    - mesaj gecmisini hatirlayarak dialogu ona gore surdurmeli.  "memory"
    - Langchain ve OPENAI GPT
    - İlk olarak terminalde calisan bir versiyon ardindan FastAPI tabanli bir web servisi olusturulacak. 
    - client tarafini yazip test edelim. 

veri seti : 
    - Veri seti yok, onun yerine hazir GPT modelini kullanarak prompt ayarlamasini yapalim. 

model tanimi : 
    - GPT ile olusturulan modeli kullanalim. 
    - gpt 3.5 turba
    - API uzerinden iletisim kurarak gercek zamanli saglik onerilerini alalim. 

Lengchain : 
    - LLM kutuphanesi 
    - prompt yonetimi 
    - memory
    - tool entegrasyonu : ai agents icin tool kullanimi 
    - chain yapimi 

API tanimlama : 
    - 

plan/program

install libraries
    - fastapi: web api gelistirmek icin bir framework (asenkron)
    - uvicorn: fastapi calistirmak icin gereken bir sunucu
    - langchain 
    - openai
    - python-dotenv: .env dosyasindan api anahtarini almak icin kullanilacak. 

import libraries 

"""

# import libraries 
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory  # Bu langchain'de kalıyor
from langchain.chains import ConversationChain  # Bu da langchain'de kalıyor

# Debug modunda göster
DEBUG = False  # veya input ile sor

# ortam degiskenlerini tanimlama (openai api key tanimla) 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("OPENAI_API_KEY bulunamadı!")
    exit(1)

# LLM + memory
# Büyük Dil Modeli
llm = ChatOpenAI(
    model = "gpt-3.5-turbo", # hangi gpt'yi kullandigimiz
    temperature = 0.7,  # 0-1, 0 a yakinsa garanti cevap verir, 1 e yakinsa dusunerek cevap verir. 1 e yaklastikca halusinasyon riski artar. 
    openai_api_key = api_key
)

# Hafiza özelligi ekleyelim. 
memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(llm = llm, memory = memory, verbose=True)

# kullanici bilgilerini al isim ve yas
while True:
    name = input("Adınız: ").strip()
    if len(name) >= 2 and name.replace(" ", "").isalpha():
        break
    print("En az 2 harfli geçerli bir ad girin!")


while True:
    try:
        age = input("Yaşınız: ").strip()
        if 1 <= age <= 120:
                break
            else:
                print("Yaş 1-120 arasında olmalıdır!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")

intro = (
    f"Sen bir doktor asistanısın. Hasta {name}, {age} yaşında. "
    "Sağlık konuları hakkında konuşmak istiyor. " 
    "Yaşına uygun dikkatli ve nazik tavsiyeler ver; ismiyle hitap et." 
)

memory.chat_memory.add_ai_message(intro)
print("Merhaba ben bir doktor asistanıyım, size nasıl yardımcı olabilirim. ")

# chatbot dongusu tanimlama. 
try:     
    while (True):
        # hasta soru sordu
        user_msg = input(f"{name}: ").strip()
        if not user_msg:
            print("Lütfen bir mesaj yazın.")
            continue
        if user_msg.lower() in ["quit", "exit", "çık"] : # konusmayi sonlandir. 
            print("Sana yardımcı olabildiysem ne mutlu bana, görüşmek üzere")
            break

        # doktor asistani cevap verdi ve hafizaya atildi. 
        reply = conversation.predict(input = user_msg) # llm cevabi
        print(f"Doktor Asistanı: {reply}")

        # verilen cevaplari memory' e  kaydet. 
        # Debug modunda hafızayı göster
        if DEBUG:
            print("\nHafiza:")
            for idx, m in enumerate(memory.chat_memory.messages, start = 1):
                print(f"{idx:02d}. {m.type.upper()}: {m.content}")

            print("-"*30 + "\n")

        
except Exception as e:
    print(f"Hata : {e}")
