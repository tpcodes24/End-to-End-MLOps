import mlflow
import boto3
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

s3_client = boto3.client('s3')

def train_model():
    df = pd.read_csv("s3://mlops-project/processed-data/pima_processed.csv")
    X, y = df.iloc[:, :-1], df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    mlflow.set_experiment("diabetes-classification")
    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        
        accuracy = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)

        model_file = "model.pkl"
        with open(model_file, "wb") as f:
            pickle.dump(model, f)
        s3_client.upload_file(model_file, "mlops-project", "models/random_forest.pkl")

if __name__ == "__main__":
    train_model()
