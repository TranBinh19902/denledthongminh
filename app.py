from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ESP32_IP = "http://192.168.86.101
"  # Thay bằng địa chỉ IP của ESP32

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/effect/<int:effect_id>")
def trigger_effect(effect_id):
    try:
        url = f"{ESP32_IP}/effect{effect_id}"
        response = requests.get(url, timeout=2)
        return f"Sent effect {effect_id}: {response.text}"
    except Exception as e:
        return f"Failed to connect to ESP32: {e}"

if __name__ == "__main__":
    app.run(debug=True)
