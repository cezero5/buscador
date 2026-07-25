import os
import subprocess
import signal
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
# Clave secreta para proteger los endpoints. Configúrala como variable
# de entorno CONTROL_KEY en Railway (o donde despliegues este controlador).
CONTROL_KEY = os.getenv("CONTROL_KEY", "cambia-esta-clave")
 
# Ruta al script del bot. Ajusta si tu estructura de carpetas cambia.
BOT_PATH = os.getenv("BOT_PATH", "Tegram/bot.py")
 
# Guardamos la referencia al proceso en memoria.
bot_process: subprocess.Popen | None = None
 
 
def check_auth(req) -> bool:
    key = req.headers.get("X-Control-Key") or req.args.get("key")
    return key == CONTROL_KEY
 
 
@app.route("/status", methods=["GET"])
def status():
    global bot_process
    activo = bot_process is not None and bot_process.poll() is None
    return jsonify({"activo": activo})
 
 
@app.route("/start", methods=["POST"])
def start_bot():
    global bot_process
 
    if not check_auth(request):
        return jsonify({"error": "No autorizado"}), 401
 
    # Si ya hay un proceso vivo, no lanzamos otro.
    if bot_process is not None and bot_process.poll() is None:
        return jsonify({"mensaje": "El bot ya está activo", "activo": True})
 
    try:
        bot_process = subprocess.Popen(
            ["python", BOT_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return jsonify({"mensaje": "Bot iniciado", "activo": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
 
@app.route("/stop", methods=["POST"])
def stop_bot():
    global bot_process
 
    if not check_auth(request):
        return jsonify({"error": "No autorizado"}), 401
 
    if bot_process is None or bot_process.poll() is not None:
        bot_process = None
        return jsonify({"mensaje": "El bot ya estaba detenido", "activo": False})
 
    try:
        # Intentamos apagar limpio primero.
        bot_process.send_signal(signal.SIGTERM)
        bot_process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        # Si no cierra a tiempo, lo forzamos.
        bot_process.kill()
    finally:
        bot_process = None
 
    return jsonify({"mensaje": "Bot detenido", "activo": False})
 
 
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
 