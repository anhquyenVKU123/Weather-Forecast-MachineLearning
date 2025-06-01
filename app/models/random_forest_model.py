# app/models/random_forest_model.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle


class RFWeatherModel:
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        print("Random Forest Model Accuracy:", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))

    def save(self, path='../saved_models/rf_weather_model.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)
        print(f"Random Forest model saved to {path}")

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'rb') as f:
            model = pickle.load(f)
        obj = cls()
        obj.model = model
        print(f"Model Random Forest đã được load từ {filepath}")
        return obj