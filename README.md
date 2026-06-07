# 🛡️ AI-Driven API Firewall

An intelligent, machine-learning-powered API Gateway designed to detect and block malicious web traffic in real-time. Unlike traditional rule-based firewalls, this system uses unsupervised learning to identify anomalies and zero-day attacks before they reach the backend server.

## ✨ Features
* **Real-Time Threat Detection:** Analyzes incoming HTTP requests in milliseconds.
* **Unsupervised Machine Learning:** Uses the `Isolation Forest` algorithm to detect anomalies (e.g., extremely long paths, excessive special characters) without needing explicit attack signatures.
* **Automated Data Pipeline:** Includes scripts to generate realistic synthetic API logs and train the AI model on the fly.
* **Lightweight Proxy:** Built with `FastAPI` to serve as a fast and reliable reverse proxy.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** FastAPI, Uvicorn (ASGI server)
* **Machine Learning:** Scikit-Learn, Pandas, Numpy

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Wadan3/ai-api-firewall.git
cd ai-api-firewall
