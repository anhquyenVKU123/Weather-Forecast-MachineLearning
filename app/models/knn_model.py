# app/models/knn_model.py

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

class KNNWeatherModel:
    def __init__(self, n_neighbors=5):
        self.model = KNeighborsClassifier(n_neighbors=n_neighbors)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        print("KNN Model Accuracy:", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))

    def save(self, path='../saved_models/knn_weather_model.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)
        print(f"KNN model saved to {path}")

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'rb') as f:
            model = pickle.load(f)
        obj = cls()
        obj.model = model
        print(f"Model KNN đã được load từ {filepath}")
        return obj