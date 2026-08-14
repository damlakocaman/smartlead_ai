import os
from dotenv import load_dotenv

# .env dosyasını okunmalı
load_dotenv()


class DevelopmentConfig:
    DEBUG = True


class ProductionConfig:
    DEBUG = False


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "default.db"
    )

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY",
        "g9W5C6jmDWVCyozr0IAeWGdyb3FYcOuNlZk0BwIi4QabTT0IbEH5"
    )

    AI_PROVIDER = os.getenv(
        "AI_PROVIDER",
        "groq"
    )

    BUSINESS_CONTEXT = os.getenv(
        "BUSINESS_CONTEXT",
        "Sen INTEROCEANIC GLOBE markasının yapay zeka asistanısın. Müşterilere lojistik süreçleri boyunca yardımcı olacaksın.Mesafeli ve profesyonel bir tonda konuşacaksın. Partner firma bulmak, fiyatlandırma yapmak ve operasyon sürecinin uçtan uca takibini yapmak gibi süreçlere dahil olacaksın."
    )

    CORS_ORIGINS = os.getenv(
        "CORS_ORIGINS",
        "*"
    )


configs = { "development": DevelopmentConfig, "production": ProductionConfig}