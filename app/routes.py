from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIService, AIServiceError
from groq import Groq 

# API için Blueprint
api = Blueprint("api", __name__, url_prefix="/api")

# Sayfalar için Blueprint
pages = Blueprint("pages", __name__)

# AI servisi
ai_service = AIService()

CORS(api)
# -------------------------
# SAYFA ENDPOINTLERİ
# -------------------------

@pages.route("/")
def home():
    return render_template("index.html")


@pages.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -------------------------
# AI ENDPOINT
# -------------------------

@api.route("/sohbet", methods=["POST"])
def sohbet():

    data = request.get_json()

    if not data or "mesaj" not in data:
        return jsonify({
            "message": "Mesaj alanı zorunludur."
        }), 400

    try:
        mesaj = data["mesaj"]

        cevap = ai_service.yanit_uret(mesaj, [])

        return jsonify({
            "cevap": cevap
        }), 200

    except AIServiceError:
        return jsonify({
            "message": "Yapay zeka servisine şu anda ulaşılamıyor."
        }), 503


# -------------------------
# LEAD EKLEME
# -------------------------

@api.route("/leads", methods=["POST"])
def create_lead():

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Veri gönderilmelidir."
        }), 400

    isim = data.get("isim")
    telefon = data.get("telefon")
    mesaj = data.get("mesaj")

    if not isim or not telefon:
        return jsonify({
            "message": "İsim ve telefon zorunludur."
        }), 400

    lead_ekle(isim, telefon, mesaj)

    return jsonify({
        "message": "Lead başarıyla eklendi."
    }), 201


# -------------------------
# LEADLERİ GETİR
# -------------------------

@api.route("/leads", methods=["GET"])
def get_leads():

    leads = tum_leadler()

    return jsonify(leads), 200
