from fastapi import FastAPI, Request, HTTPException
import uvicorn
import pickle
import re

app = FastAPI(title="AI-Driven API Security Firewall")

print("[*] Loading AI Model...")
with open('model.pkl', 'rb') as f:
    ai_model = pickle.load(f)
print("[+] AI Model loaded successfully!")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def firewall_proxy(request: Request, path: str):
    client_ip = request.client.host
    method = request.method
    
    path_length = len(path)
    special_chars = len(re.findall(r'[^a-zA-Z0-9/]', path))
    
    print(f"[*] Analyzing traffic | Path: /{path} | Length: {path_length} | Special Chars: {special_chars}")
    
    prediction = ai_model.predict([[path_length, special_chars]])
    
    is_malicious = True if prediction[0] == -1 else False
    
    if is_malicious:
        print(f"[!] 🚨 Threat detected from {client_ip}. Blocking request.")
        raise HTTPException(status_code=403, detail="Access Denied: Malicious traffic detected by AI")

    print("[+] Request is safe.")
    return {
        "status": "success",
        "message": "Request passed the firewall",
        "path_analyzed": f"/{path}"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)