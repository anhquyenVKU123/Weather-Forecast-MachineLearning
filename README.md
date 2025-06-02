Nhánh master là nhánh bao gồm sản phẩm hoàn thành cuối cùng

Bước 1: Tạo thư mục mới có tên Weather_Direction ( hoặc tuỳ theo cá nhân )

Bước 2: Click chuột phải -> Open Gitbash here

Bước 3: Nhập lệnh : git clone https://github.com/anhquyenVKU123/Weather-Forecast-MachineLearning.git

Bước 4: Truy cập vào thư mục Weather_Direction/Weather-Forecast-MachineLearning. Hiện tại ở nhánh main bạn chỉ thấy file Slide_Hoc_may.pptx.

Bước 5: Tại thư mục Weather-ForeCast-MachineLearning. Click chuột phải -> Open Gitbash here -> Nhập lệnh git switch master. Vậy là nhánh master đã được tải về trong thư mục Weather-Forecast-MachineLearning.

Bước 6: Mở file app.py bằng IDE mà bạn đang sử dụng ( ở đây mình sử dụng PyCharm Community Edition 2024.3.3

<<<<<<< HEAD
Bước 7: Mở terminal của IDE lên :

    1. py -3.10 -m venv venv ( Để cài đặt python phiên bản 3.10, 3.13 quá mới nên có một số thư viện không hỗ trợ )
    
    2. venv\Scripts\activate ( Kích hoạt môi trường ảo cho dự án )
    
    3. python --version ( Kiểm tra lại phiên bản python. Nếu kết quả là 3.10.x thì OK )
    
    4. pip install -r requirements.txt ( để tải các thư viện , hơi lâu một tí )
    
    5. Trên dòng cảnh báo màu vàng có Config Python Interperter. Click vào và chọn phiên bản Python 3.10
=======
Bước 7: Mở terminal của IDE lên : 

        1. py -3.10 -m venv venv ( Để cài đặt python phiên bản 3.10, 3.13 quá mới nên có một số thư viện không hỗ trợ )
        
        2. venv\Scripts\activate ( Kích hoạt môi trường ảo cho dự án )
        
        3. python --version ( Kiểm tra lại phiên bản python. Nếu kết quả là 3.10.x thì OK )
        
        4. pip install -r requirements.txt ( để tải các thư viện , hơi lâu một tí )
        
        5. Trên dòng cảnh báo màu vàng có Config Python Interperter. Click vào và chọn phiên bản Python 3.10
        
>>>>>>> 5b6c769b575bf4ee607a1916a27eec62d1c30a57
Bước 8: Tại thư mục Weather-Forecast-MachineLearning. Tạo thư mục mới saved_models

Bước 9: Trong app/core :

<<<<<<< HEAD
    1. Chạy file PreprocessingData.py để xử lí dữ liệu
    
    2. Chạy file train.py để luyện mô hình
    
    3. Click chuột phải vào WeatherStatistic.py -> Open in Terminal -> Nhập lệnh streamlit run WeatherStatistic.py để xem trang thống kê dữ liệu
    
    4. Chạy file evaluation.py để xem các đánh giá mô hình
Bước 10: Trong app/ chạy file app.py rồi chọn đường link http://127.0.0.1:5000 để hiển thị trang web. Nhập các dữ liệu và chọn mô hình dự đoán.

File WeatherData.py : Lấy dữ liệu https://archive-api.open-meteo.com/v1/archive?
File QuangNam_Weather_Data.csv : Dữ liệu chưa xử lí
File PreprocessingData.py : Xử lí dữ liệu
File weather_data_processed.csv : Dữ liệu sạch
File WeatherStatistic.py : Buil trang web thống kê dữ liệu
Cài đặt thư viện streamlit, plotly, seaborn, ...
Vào Terminal : streamlit run WeatherStatistic.py
Không xoá phần code bị đánh dấu lại ( để sửa tiếp )
File WeatherRandomForestModel.py : Dùng model RandomForest để train ( File này chưa train được do dùng dữ liệu cũ )
=======
        1. Chạy file PreprocessingData.py để xử lí dữ liệu
        
        2. Chạy file train.py để luyện mô hình
        
        3. Click chuột phải vào WeatherStatistic.py -> Open in Terminal -> Nhập lệnh streamlit run WeatherStatistic.py để xem trang thống kê dữ liệu
        
        4. Chạy file evaluation.py để xem các đánh giá mô hình
        
Bước 10: Trong app/ chạy file app.py rồi chọn đường link http://127.0.0.1:5000 để hiển thị trang web. Nhập các dữ liệu và chọn mô hình dự đoán.


1. File WeatherData.py : Lấy dữ liệu https://archive-api.open-meteo.com/v1/archive?
2. File QuangNam_Weather_Data.csv : Dữ liệu chưa xử lí
3. File PreprocessingData.py : Xử lí dữ liệu
4. File weather_data_processed.csv : Dữ liệu sạch
5. File WeatherStatistic.py : Buil trang web thống kê dữ liệu
    - Cài đặt thư viện streamlit, plotly, seaborn, ...
    - Vào Terminal : streamlit run WeatherStatistic.py
    - Không xoá phần code bị đánh dấu lại ( để sửa tiếp )
6. File WeatherRandomForestModel.py : Dùng model RandomForest để train ( File này chưa train được do dùng dữ liệu cũ )
>>>>>>> 5b6c769b575bf4ee607a1916a27eec62d1c30a57
