from flask import Flask
from app.controllers import weather_controller

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return weather_controller.predict_weather()

@app.route("/predict", methods=["POST"])
def predict():
    return weather_controller.predict_weather()
