# OML Writing Assistant API 🚀

An AI-powered writing assistant for the Old Money Luxury (OML) YouTube channel, built with FastAPI, OpenAI GPT, Redis caching, MySQL, and YouTube analytics integration.

## 📌 Features
- **AI-Powered Writing** – Structured Old Money Luxury (OML) articles.
- **Fact-Checking** – AI-assisted verification with reliable sources.
- **Multimedia Adaptation** – Convert articles into audio and video.
- **YouTube Insights** – Fetch competitor analytics and content trends.
- **User Authentication** – Secure login with OAuth2/JWT.
- **FastAPI & Redis** – High-performance backend with caching.
- **CI/CD Deployment** – Automated GitHub Actions & Hostinger deployment.

## 📂 Project Structure
/OML-Writing-Assistant │── /src/ (API Source Code) │── /frontend/ (Web UI) │── /config/ (Configurations) │── /deploy/ (CI/CD & Deployment Scripts) │── README.md │── .gitignore │── .env (Environment Variables) │── Dockerfile │── docker-compose.yml
bash
CopyEdit


## 🔹 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AreefChowdhury/OML-Writing-Assistant.git
   cd OML-Writing-Assistant

Install dependencies:
bash
CopyEdit
pip install -r config/requirements.txt


Start the server:
bash
CopyEdit
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload


Run with Docker:
bash
CopyEdit
docker-compose up --build


yaml
CopyEdit


✅ **Why?**  
- Provides **clear setup & usage instructions**.  
- Includes **project structure & deployment commands**.  

---

## **📜 `.gitignore` (Ignore Unnecessary Files)**
```plaintext
# Ignore Python cache files
__pycache__/
*.pyc
*.pyo

# Ignore environment variables
.env

# Ignore virtual environments
venv/
*.venv/

# Ignore logs and temporary files
logs/
*.log
