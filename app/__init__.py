from flask import Flask
from flask_cors import CORS

from config import configs
from app.database import init_db
from app.routes import api, pages


def create_app():
    app = Flask(__name__)

    # 1. Ayarları yükle
    app.config.from_object(configs["development"])

    # 2. CORS'u aç
    CORS(app)

    # 3. Veritabanını başlat
    with app.app_context():
        init_db(app)

    # 4. Blueprint'leri kaydet
    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")

     # 5. Health endpoint
    @app.route("/health")
    def health():
        return {
            "status": "ok"
        }, 200

    return app