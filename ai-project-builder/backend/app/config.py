import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1]/".env")
SESSION_SECRET=os.getenv("SESSION_SECRET","dev-only-change-me")
FRONTEND_ORIGIN=os.getenv("FRONTEND_ORIGIN","http://localhost:5173")
AI_API_KEY=os.getenv("AI_API_KEY","")
AI_BASE_URL=os.getenv("AI_BASE_URL","https://api.openai.com/v1").rstrip("/")
AI_MODEL=os.getenv("AI_MODEL","gpt-4.1-mini")
GITHUB_CLIENT_ID=os.getenv("GITHUB_CLIENT_ID","")
GITHUB_CLIENT_SECRET=os.getenv("GITHUB_CLIENT_SECRET","")
GITHUB_CALLBACK_URL=os.getenv("GITHUB_CALLBACK_URL","http://localhost:8000/api/github/callback")
MAX_UPLOAD_MB=int(os.getenv("MAX_UPLOAD_MB","10"))
