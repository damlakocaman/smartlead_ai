from config import Config
from groq import Groq  # Resmi Groq kütüphanesini kullanıyoruz

class AIService:

    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.model = "openai/gpt-oss-20b" 
        
        # 2. Groq istemcisini (client) resmi kütüphane ile başlatıyoruz
        self.client = None
        if self.api_key:
            self.client = Groq(api_key=self.api_key)

    def get_business_context(self):
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):
        if gecmis is None:
            gecmis = []

        if not self.client:
            return "Demo modu: Groq API anahtarı bulunamadı veya istemci başlatılamadı."

        # Sistem mesajını (Business Context) ekle
        messages = [
            {
                "role": "system",
                "content": self.get_business_context()
            }
        ]

        # Varsa geçmiş chat mesajlarını ekle
        messages.extend(gecmis)
 
        # Kullanıcının son mesajını ekle
        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        try:
            # requests yerine resmi Groq SDK çağrısını yapıyoruz
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
                timeout=30.0  # Zaman aşımı süresi
            )

            # Yapay zekanın ürettiği cevabı geri döndür
            return completion.choices[0].message.content

        except Exception as e:
            # Olası bir API hatasında uygulamanın 503/500 çökmesini engellemek için hata fırlatıyoruz
            raise AIServiceError(
                f"Groq servisine bağlanılamadı veya hata oluştu: {e}"
            )


class AIServiceError(Exception):
    pass


# Dışarıdan doğrudan çağrılabilmesi için nesneyi oluşturuyoruz
ai_service = AIService()
