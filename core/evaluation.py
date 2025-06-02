import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def tune_knn(X_train, y_train, k_values=range(1, 31), cv=5):
    print("Tuning K cho KNN...")
    cv_scores = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X_train, y_train, cv=cv, scoring='accuracy')
        mean_score = scores.mean()
        cv_scores.append(mean_score)
        print(f"k={k} => CV Accuracy: {mean_score:.4f}")

    best_k = k_values[np.argmax(cv_scores)]
    print(f"K tốt nhất: {best_k} với accuracy CV = {max(cv_scores):.4f}")

    # Plot kết quả
    plt.figure(figsize=(10,6))
    plt.plot(k_values, cv_scores, marker='o')
    plt.xlabel('Số lượng láng giềng k')
    plt.ylabel('Accuracy (CV)')
    plt.title('Tuning số lượng láng giềng K trong KNN')
    plt.grid(True)
    plt.show()
    return best_k

def evaluate_model(model, X_test, y_test, model_name="Model"):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nBáo cáo đánh giá cho {model_name}:")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))

def check_rf_overfitting(rf_model, X_train, y_train, X_test, y_test):
    train_acc = rf_model.score(X_train, y_train)
    test_acc = rf_model.score(X_test, y_test)
    print("\nKiểm tra Overfitting của Random Forest:")
    print(f"Accuracy trên tập huấn luyện: {train_acc:.4f}")
    print(f"Accuracy trên tập kiểm tra: {test_acc:.4f}")

    if train_acc - test_acc > 0.05:
        print("Có dấu hiệu Overfitting (chênh lệch > 5%)")
    else:
        print("Không có dấu hiệu overfitting rõ ràng")


def plot_learning_curve(estimator, X, y, title="Learning Curve", cv=5, scoring='accuracy'):

    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, scoring=scoring,
        train_sizes=np.linspace(0.1, 1.0, 10), n_jobs=-1, random_state=42
    )

    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.xlabel("Training examples")
    plt.ylabel(scoring)
    plt.grid(True)

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")

    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

    plt.legend(loc="best")
    plt.show()

def evaluate_model(model, X_test, y_test, model_name="Model"):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nBáo cáo đánh giá cho {model_name}:")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))

    # Plot confusion matrix
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    plt.figure(figsize=(8, 6))
    disp.plot(cmap='Blues', xticks_rotation=45, values_format='d')
    plt.title(f"Confusion Matrix - {model_name}")
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    # Load data
    df = pd.read_csv("../data/weather_data_processed.csv")

    # Giả sử bạn đã có các cột tách Day, Month, Year, Hour như đã nói
    # Tạo feature và label
    feature_cols = ['Day', 'Month', 'Year', 'Hour', 'Temp_C', 'Humidity_pct', 'Precipitation_mm', 'WindSpeed_kmh', 'CloudCover_pct', 'AtmosPressure_hPa']
    target_col = 'WeatherCondition'

    X = df[feature_cols]
    y = df[target_col]

    # Chia train-test (vd năm < 2024 là train, năm = 2024 là test)
    train_df = df[df['Year'] < 2024]
    test_df = df[df['Year'] == 2024]

    X_train = train_df[feature_cols]
    y_train = train_df[target_col]
    X_test = test_df[feature_cols]
    y_test = test_df[target_col]

    # --- Tune KNN ---
    best_k = tune_knn(X_train, y_train)

    # Train KNN với k tốt nhất
    knn = KNeighborsClassifier(n_neighbors=best_k)
    knn.fit(X_train, y_train)
    evaluate_model(knn, X_test, y_test, "KNN")

    # Train Random Forest với default (bạn có thể điều chỉnh params)
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    evaluate_model(rf, X_test, y_test, "Random Forest")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    plot_learning_curve(rf, X_train, y_train, title="Learning Curve - Random Forest")

    # Kiểm tra overfitting của RF
    check_rf_overfitting(rf, X_train, y_train, X_test, y_test)

    # Lưu model nếu muốn
    joblib.dump(knn, "../saved_models/knn_weather_model.pkl")
    joblib.dump(rf, "../saved_models/rf_weather_model.pkl")

    print("\nHoàn thành đánh giá và lưu model!")

    # --- Đánh giá trên tập test bên ngoài (QuangNam_Weather_test.csv) ---
    print("\n Đang đọc dữ liệu test bên ngoài từ file Data Test...")
    external_test_df = pd.read_csv("../data/weather_data_test_processed.csv")

    # Kiểm tra cột bắt buộc
    required_cols = feature_cols + [target_col]
    missing_cols = set(required_cols) - set(external_test_df.columns)
    if missing_cols:
        raise ValueError(f"Thiếu cột trong file test: {missing_cols}")

    X_external = external_test_df[feature_cols]
    y_external = external_test_df[target_col]
