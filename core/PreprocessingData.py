import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class WeatherPreprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("\nDữ liệu đã được nạp thành công.")

    def parse_datetime(self):
        # Đảm bảo cột Date là string, Time là HH:mm
        self.df['Date'] = self.df['Date'].astype(str)
        self.df['Time'] = self.df['Time'].astype(str)
        print("Đã chuẩn hóa cột Date và Time.")

    def extract_time_features(self):
        print("📅 Đang trích xuất đặc trưng thời gian từ Date và Time...")

        # Gộp Date + Time thành datetime
        self.df['Datetime'] = pd.to_datetime(self.df['Date'] + ' ' + self.df['Time'], errors='coerce')

        # Trích xuất các cột thời gian
        self.df['Year'] = self.df['Datetime'].dt.year
        self.df['Month'] = self.df['Datetime'].dt.month
        self.df['Day'] = self.df['Datetime'].dt.day
        self.df['Hour'] = self.df['Datetime'].dt.hour

        # Xóa cột gốc
        self.df.drop(columns=['Date', 'Time', 'Datetime'], inplace=True)

        # Đưa các cột thời gian lên đầu
        time_cols = ['Day', 'Month', 'Year', 'Hour']
        other_cols = [col for col in self.df.columns if col not in time_cols]
        self.df = self.df[time_cols + other_cols]

        print("✅ Đã trích xuất và đưa các cột thời gian (Day, Month, Year, Hour) lên đầu DataFrame.")

    def convert_types(self):
        numeric_cols = [
            'Temp_C', 'Humidity_pct', 'Precipitation_mm', 'WindSpeed_kmh',
            'CloudCover_pct', 'AtmosPressure_hPa', 'WeatherCondition'
        ]
        for col in numeric_cols:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        print("Đã chuyển đổi các cột số về đúng kiểu dữ liệu.")

    def handle_missing_values(self):
        before = self.df.isnull().sum()
        # Chỉ nội suy các cột số
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        self.df[numeric_cols] = self.df[numeric_cols].interpolate(method='linear', limit_direction='both')
        after = self.df.isnull().sum()
        print("🧹 Đã xử lý missing values bằng nội suy tuyến tính.")
        print("\nMissing value trước:")
        print(before[before > 0])
        print("\nMissing value sau:")
        print(after[after > 0])

    def detect_outliers_iqr(self):
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        outlier_summary = {}
        bounds_summary = {}
        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((self.df[col] < lower_bound) | (self.df[col] > upper_bound)).sum()
            outlier_summary[col] = outliers
            bounds_summary[col] = (round(lower_bound, 2), round(upper_bound, 2))

        print("Tổng số outliers (theo IQR):")
        print({k: v for k, v in outlier_summary.items() if v > 0})
        print("\nNgưỡng IQR (lower & upper bounds):")
        for col, bounds in bounds_summary.items():
            if outlier_summary[col] > 0:
                print(f"{col}: {bounds}")

    def handle_outliers_minmax(self):
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_cols:
            if col in ['Precipitation_mm', 'WindSpeed_kmh']:
                continue  # Giữ nguyên outliers cho các cột này
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Lấy min/max từ vùng an toàn
            safe_values = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)][col]
            min_safe = safe_values.min()
            max_safe = safe_values.max()

            # Clamp giá trị nằm ngoài về min/max của vùng an toàn
            self.df[col] = self.df[col].clip(lower=min_safe, upper=max_safe)
        print("Đã xử lý outliers (trừ Precipitation_mm và WindSpeed_kmh) bằng cách clamp về min/max của vùng an toàn theo IQR.")

    def remove_duplicates(self):
        before = len(self.df)
        self.df.drop_duplicates(inplace=True)
        after = len(self.df)
        print(f"Đã loại bỏ {before - after} dòng trùng nhau.")

    def export_cleaned(self, out_file):
        self.df.to_csv(out_file, index=False)
        print(f"\nDữ liệu sạch đã được lưu vào {out_file}")

    def data_overview(self):
        print("\nTổng quan dữ liệu:")
        print(f"Số dòng: {self.df.shape[0]}")
        print(f"Số cột: {self.df.shape[1]}\n")

        print("Kiểu dữ liệu các cột:")
        print(self.df.dtypes, "\n")

        print("Số ô trống (null) từng cột:")
        print(self.df.isnull().sum(), "\n")

        print("Thống kê mô tả các cột số:")
        print(self.df.describe().T[['count', 'mean', 'min', 'max', 'std']], "\n")

        dup_count = self.df.duplicated().sum()
        print(f"Số dòng trùng nhau: {dup_count}")
        print(f"Số dòng duy nhất: {self.df.shape[0] - dup_count}\n")

        print("Số lượng giá trị hợp lệ (non-null) trong mỗi cột:")
        print(self.df.nunique(), "\n")

pre = WeatherPreprocessor("../data/QuangNam_Weather_Data.csv")
pre.load_data()
pre.parse_datetime()
pre.convert_types()
pre.extract_time_features()
pre.data_overview()
pre.handle_missing_values()
pre.detect_outliers_iqr()
pre.handle_outliers_minmax()
pre.remove_duplicates()
pre.export_cleaned("../data/weather_data_processed.csv")
pre.data_overview()

pre_test = WeatherPreprocessor("../data/QuangNam_Weather_Data_Test.csv")
pre_test.load_data()
pre_test.parse_datetime()
pre_test.convert_types()
pre_test.extract_time_features()
pre_test.handle_missing_values()
pre_test.detect_outliers_iqr()
pre_test.handle_outliers_minmax()
pre_test.remove_duplicates()
pre_test.export_cleaned("../data/weather_data_test_processed.csv")