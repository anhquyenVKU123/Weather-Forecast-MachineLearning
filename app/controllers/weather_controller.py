import pandas as pd
import os
from flask import request, render_template
from app.models.knn_model import KNNWeatherModel
from app.models.random_forest_model import RFWeatherModel

# --- Đường dẫn ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # app/
ROOT_DIR = os.path.dirname(BASE_DIR)  # project root

# --- Load dữ liệu mô tả thời tiết & gợi ý nông nghiệp ---
exp_path = os.path.join(BASE_DIR, "controllers", "Agriculture_Exp.csv")
exp_df = pd.read_csv(exp_path)

# Convert 'Code' về int nếu cần
exp_df["Code"] = exp_df["Code"].astype(int)

# Mapping để lấy mô tả
desc_map = dict(zip(exp_df["Code"], exp_df["Description"]))

# --- Load models ---
knn_model = KNNWeatherModel.load(os.path.join(ROOT_DIR, "saved_models", "knn_weather_model.pkl"))
rf_model = RFWeatherModel.load(os.path.join(ROOT_DIR, "saved_models", "rf_weather_model.pkl"))

# --- View chính: Dự đoán + Gợi ý ---
def predict_weather():
    if request.method == 'POST':
        # Lấy dữ liệu đầu vào từ form
        try:
            day = int(request.form['day'])
            month = int(request.form['month'])
            year = int(request.form['year'])
            hour = int(request.form['hour'])
            temp = float(request.form['Temp_C'])
            precipitation = float(request.form['Precipitation_mm'])
            humidity = float(request.form['Humidity_pct'])
            pressure = float(request.form['AtmosPressure_hPa'])
            wind_speed = float(request.form['WindSpeed_kmh'])
            cloud_cover = float(request.form['CloudCover_pct'])
            model_choice = request.form['model_select']
        except Exception as e:
            return render_template("index.html", error=f"Lỗi nhập liệu: {e}")

        # Tạo input cho model
        X_input = [[day, month, year, hour, temp, precipitation, humidity, pressure, wind_speed, cloud_cover]]

        # Dự đoán
        try:
            if model_choice == 'knn':
                pred_code = int(knn_model.predict(X_input)[0])
            else:
                pred_code = int(rf_model.predict(X_input)[0])
        except Exception as e:
            return render_template("index.html", error=f"Lỗi khi dự đoán: {e}")

        # Lấy mô tả + gợi ý nông nghiệp
        weather_desc = desc_map.get(pred_code, "Không xác định")

        crop_advice = {
            "Ngô": "",
            "Lúa gạo": "",
            "Bông": "",
            "Đậu tương": "",
            "Rau màu": ""
        }

        advice_row = exp_df[exp_df["Code"] == pred_code]
        if not advice_row.empty:
            advice_row = advice_row.iloc[0]
            for crop in crop_advice:
                crop_advice[crop] = advice_row.get(crop, "Không có gợi ý")

        return render_template("index.html",
                               prediction_code=pred_code,
                               prediction_desc=weather_desc,
                               crop_advice=crop_advice)

    return render_template("index.html")
