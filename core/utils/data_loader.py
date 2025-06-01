# utils/data_loader.py

import pandas as pd
from sklearn.model_selection import train_test_split


def load_processed_data(test_size=0.2, random_state=42):
    # Đọc file đã được xử lý sẵn (đảm bảo file này tồn tại và đúng chuẩn)
    df = pd.read_csv("../data/weather_data_processed.csv")

    # Chuyển cột Date sang datetime để lọc theo năm
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])

    # Lọc train và test theo năm
    train_df = df[df['Date'].dt.year < 2024]
    test_df = df[df['Date'].dt.year == 2024]

    # Drop các cột không cần thiết
    drop_cols = ['Date']

    X_train = train_df.drop(columns=drop_cols + ['WeatherCondition'])
    y_train = train_df['WeatherCondition']

    X_test = test_df.drop(columns=drop_cols + ['WeatherCondition'])
    y_test = test_df['WeatherCondition']

    return X_train, X_test, y_train, y_test
