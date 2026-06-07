import pandas as pd
import random

print("[*] Generating realistic API traffic dataset...")

data = []

for _ in range(1000):
    data.append({
        'path_length': random.randint(5, 35),
        'special_chars': random.randint(0, 1),
        'is_threat': 0
    })
for _ in range(200):
    data.append({
        'path_length': random.randint(50, 150),
        'special_chars': random.randint(5, 20),
        'is_threat': 1
    })
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv('api_logs.csv', index=False)
print("[+] Dataset 'api_logs.csv' successfully created with 1200 records!")