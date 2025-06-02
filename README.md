Đầu tiên chọn folder bạn muốn lưu dự án này.
mở git bash: nhập git clone https://github.com/anhquyenVKU123/Weather-Forecast-MachineLearning.git,
hoặc git clone git@github.com:anhquyenVKU123/Weather-Forecast-MachineLearning.git (khuyến khích cách này nếu có đã có ssh key),
hoặc download thẳng file zip rồi giải nén cũng được :vv.

Hiện tại, sau khi clone về bạn sẽ ở nhánh main chưa có gì cả, mở git bash tại folder mới clone về
dùng lệnh git switch ten-nhanh mà bạn muốn chuyển. Git sẽ tự làm phần việc còn lại :>>.

Hướng dẫn nếu bạn ở nhánh demo_train_models.

Đầu tiên, chạy lệnh pip install -r requirements.txt để download các thư viện.

Ở các file có đường dẫn "d:\Học Máy\Weather-Forecast-MachineLearning" đổi lại theo đúng với 
máy tính bạn là được.

Chạy file train_model.py ở app/model để train model.
Lưu ý: joblib.dump(model, os.path.join(model_dir, "knn_model_07_with_n_equal_21.pkl")) 
ở dòng code phía trên bạn có thể đặt lại tên, sao cho dễ nhớ, tách biệt với các model đã train là được.
Vì knn nên bạn có thể đặt n bằng số lẻ bất kì để train.

Tiếp theo, run file evaluate_model.py đánh giá hình mà bạn đã train.
Lưu ý:
Nhớ đổi lại tên model model_path = r"D:\Học Máy\Weather-Forecast-MachineLearning\models\knn_model_07_with_n_equal_21.pkl".
Lưu ý các thông số của model, confusion_matrix ở folder classification_reports cà và cầu nguyện cho Accuracy cao :'>>.

Để chạy web dự đoán thời tiết.
Chạy file run.py nhấp vào link http://127.0.0.1:5000/ sẽ đưa bạn tới web dự đoán thời tiết.
Nhập các thông số yêu cầu. 
Bấm dự đoán để xem kết quả.

Chúc bạn thành công hehe.

1. File WeatherData.py : Lấy dữ liệu https://archive-api.open-meteo.com/v1/archive?
2. File QuangNam_Weather_Data.csv : Dữ liệu chưa xử lí
3. File PreprocessingData.py : Xử lí dữ liệu
4. File weather_data_processed.csv : Dữ liệu sạch
