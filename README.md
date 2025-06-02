Nhánh master là nhánh bao gồm sản phẩm hoàn thành cuối cùng

Bước 1: Tạo thư mục mới có tên Weather_Direction ( hoặc tuỳ theo cá nhân )

Bước 2: Click chuột phải -> Open Gitbash here

Bước 3: Nhập lệnh : git clone https://github.com/anhquyenVKU123/Weather-Forecast-MachineLearning.git

Bước 4: Truy cập vào thư mục Weather_Direction/Weather-Forecast-MachineLearning. Hiện tại ở nhánh main bạn chỉ thấy file Slide_Hoc_may.pptx.

Bước 5: Tại thư mục Weather-ForeCast-MachineLearning. Click chuột phải -> Open Gitbash here -> Nhập lệnh git switch master. Vậy là nhánh master đã được tải về trong thư mục Weather-Forecast-MachineLearning.

Bước 6: Mở file app.py bằng IDE mà bạn đang sử dụng ( ở đây mình sử dụng PyCharm Community Edition 2024.3.3

Bước 7: Mở terminal của IDE lên : 

        1. rm -r venv ( để xoá môi trường cũ trong repo )
        
        2. Trên dòng cảnh báo màu vàng có Configure Python Interpreter. Click vào chọn Add new Interpreter -> Add Local Interpreter -> Chọn thư mục chứa Python310\python.exe

        3. Cài các thư viện cần thiết trên dòng cảnh báo màu vàng

        4. Cài đặt package flask, scikit-learn
        
Bước 8: Trong app/core :
    
    1. Click chuột phải vào WeatherStatistic.py -> Open in Terminal -> Nhập lệnh streamlit run WeatherStatistic.py để xem trang thống kê dữ liệu
    
    2. Chạy file evaluation.py để xem các đánh giá mô hình
    
Bước 9: Trong app/ chạy file app.py rồi chọn đường link http://127.0.0.1:5000 để hiển thị trang web. Nhập các dữ liệu và chọn mô hình dự đoán.
