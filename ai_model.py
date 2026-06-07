import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

data = {
    'path_length': [10, 15, 8, 12, 20, 120, 150, 110],  
    'special_chars': [0, 1, 0, 0, 1, 10, 15, 12],      
    'is_threat': [0, 0, 0, 0, 0, 1, 1, 1]              
}

df = pd.DataFrame(data)

X = df[['path_length', 'special_chars']]

print("[*] Training AI Anomaly Detection Model...")
model = IsolationForest(contamination=0.3, random_state=42)
model.fit(X)
print("[+] Model trained successfully!")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("[+] Model saved locally as 'model.pkl'. Ready for integration!")