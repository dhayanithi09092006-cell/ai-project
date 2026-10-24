# AI Project Builder
Configured for: **Federated Learning Framework for Privacy-Preserving Medical Image Analysis**.

## Run
Backend: Python 3.11+, `cd backend`, create a venv, `pip install -r requirements.txt`, copy `.env.example` to `.env`, fill AI/GitHub credentials, then `uvicorn app.main:app --reload --port 8000`.
Frontend: `cd frontend`, `npm install`, `npm run dev`, open http://localhost:5173.

Create a GitHub OAuth App with homepage `http://localhost:5173` and callback `http://localhost:8000/api/github/callback`. Add credentials only to backend `.env`.

Features: spec text/upload, server-side AI code generation, file tree/preview, ZIP download, GitHub OAuth/repository listing/creation/commit publishing. PDF/DOCX/TXT extraction works; image OCR requires an OCR provider. Generated code is never executed. The in-memory project store is for development. Signed session cookies are not encrypted; replace with server-side sessions and durable storage before production. Use de-identified licensed medical data; no clinical validity is implied.
