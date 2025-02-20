import pandas as pd
from sklearn.preprocessing import StandardScaler
import boto3

s3_client = boto3.client('s3')

def process_data():
    df = pd.read_csv("s3://mlops-project/raw-data/pima.csv")
    
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df.iloc[:, :-1]), columns=df.columns[:-1])
    df_scaled["Outcome"] = df["Outcome"]
    
    df_scaled.to_csv("processed_data.csv", index=False)
    s3_client.upload_file("processed_data.csv", "mlops-project", "processed-data/pima_processed.csv")

if __name__ == "__main__":
    process_data()
