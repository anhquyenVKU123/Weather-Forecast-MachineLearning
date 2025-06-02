import pandas as pd

# Đọc dữ liệu từ file csv
df = pd.read_csv(r'd:\Học Máy\Weather-Forecast-MachineLearning\data\processed\weather_data_processed.csv')

# Đếm số lượng mỗi giá trị trong cột WeatherCondition
weather_condition_counts = df['WeatherCondition'].value_counts().reset_index()

print(weather_condition_counts)
