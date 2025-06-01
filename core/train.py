from utils.data_loader import load_processed_data
from app.models.knn_model import KNNWeatherModel
from app.models.random_forest_model import RFWeatherModel


def main():
    print("🚀 Loading data...")
    X_train, X_test, y_train, y_test = load_processed_data()

    print("🔧 Training KNN Model...")
    knn_model = KNNWeatherModel(n_neighbors=21)
    knn_model.train(X_train, y_train)
    knn_model.evaluate(X_test, y_test)
    knn_model.save()

    print("\n🌲 Training Random Forest Model...")
    rf_model = RFWeatherModel(n_estimators=100, random_state=42)
    rf_model.train(X_train, y_train)
    rf_model.evaluate(X_test, y_test)
    rf_model.save()


if __name__ == "__main__":
    main()
