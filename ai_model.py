import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

print("[*] Loading dataset from 'api_logs.csv'...")
df = pd.read_csv('api_logs.csv')
X = df[['path_length', 'special_chars']]

print("[*] Training Advanced Anomaly Detection Model on 1200 records...")
model = IsolationForest(contamination=0.16, random_state=42)
model.fit(X)
print("[+] Advanced Model trained successfully!")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("[+] Advanced AI Model saved as 'model.pkl'. Ready for action!")