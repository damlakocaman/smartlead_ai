import os
from flask import Flask
from flask_cors import CORS

from config import configs
from app.database import init_db
from app.routes import api, pages


def create_app():
    app = Flask(__name__)

    # 1. DÜZENLEME: Canlı sunucu (Render) veya lokal ortama göre konfigürasyonu otomatik seçer
    # Eğer sistemde FLASK_ENV=production tanımlıysa production ayarlarını yükler, yoksa development ile başlar.
    env = os.environ.get("FLASK_ENV", "development")
    app.config.from_object(configs[env])

    # 2. DÜZENLEME: Wix gibi dış platformlardan gelen tüm tarayıcı metotlarına (GET, POST, OPTIONS) 
    # ve başlıklarına (Headers) kesin olarak izin veren gelişmiş CORS yapılandırması.
    CORS(app, resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    with app.app_context():
        init_db(app)

    # Rotalarınız (Blueprint yapılarınız)
    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")

    @app.route("/health")
    def health():
        return {
            "status": "ok"
        }, 200

    return app
