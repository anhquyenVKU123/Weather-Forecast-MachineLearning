from flask import Flask
from app.controllers.weather_controller import predict_weather

app = Flask(__name__, template_folder="app/templates")
app.secret_key = 'super_secret_key_123'  # Cần thiết để dùng session lưu dữ liệu dự đoán

# Route dự đoán thời tiết (GET/POST)
@app.route("/", methods=["GET", "POST"])
def home():
    return predict_weather()

if __name__ == "__main__":
    app.run(debug=True)
