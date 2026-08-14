import requests

from config import Config


class AIService:

    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.model = "llama-3.1-8b-instant"

    def get_business_context(self):
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):

        if gecmis is None:
            gecmis = []

        if not self.api_key:
            return "Demo modu: Groq API anahtarı bulunamadı."

        messages = [
            {
                "role": "system",
                "content": self.get_business_context()
            }
        ]

        messages.extend(gecmis)
 
        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        try:

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": messages
                },
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]

        except requests.RequestException as e:

            raise AIServiceError(
                f"Yapay zeka servisine bağlanılamadı: {e}"
            )


class AIServiceError(Exception):
    pass


ai_service = AIService()