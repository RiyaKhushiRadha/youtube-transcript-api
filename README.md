# 🎥 YouTube Transcript API

A production-ready FastAPI backend service that extracts transcripts from YouTube videos using the `youtube-transcript-api` library.

The project provides a clean REST API, interactive Swagger documentation, automated testing, and continuous integration using GitHub Actions.

---

## 🚀 Live Demo

- **API Base URL:** https://youtube-transcript-api-098o.onrender.com
- **Swagger UI:** https://youtube-transcript-api-098o.onrender.com/docs
- **ReDoc:** https://youtube-transcript-api-098o.onrender.com/redoc

---

## 📌 Project Status

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Pytest](https://img.shields.io/badge/Tests-Passing-brightgreen)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# ✨ Features

- 🎥 Extract transcripts from YouTube videos
- 🔗 Supports multiple YouTube URL formats
- ⚡ Fast REST API built with FastAPI
- 📖 Interactive Swagger UI documentation
- 📚 ReDoc API documentation
- 🛡️ Custom exception handling
- ✅ Automated unit testing with Pytest
- 🚀 Continuous Integration using GitHub Actions
- 🌐 Public deployment on Render
- 📦 Clean and modular project architecture

---

# 📡 API Overview

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint with API information |
| GET | `/health` | Health check endpoint |
| POST | `/transcript` | Extract transcript from a YouTube video |

---

# 📥 Request Example

```json
{
  "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
```

---

# 📤 Successful Response

```json
{
  "language": "en",
  "transcript": [
    {
      "text": "Hello everyone",
      "start": 0.0,
      "duration": 2.5
    }
  ]
}
```

---

# ❌ Possible Error Responses

| Status Code | Description |
|--------------|-------------|
| 400 | Invalid YouTube URL or Video ID |
| 403 | Transcript is disabled |
| 404 | Transcript not available |
| 500 | Internal Server Error |

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| Backend Framework | FastAPI |
| ASGI Server | Uvicorn |
| Validation | Pydantic |
| Transcript Library | youtube-transcript-api |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Deployment | Render |
| API Documentation | Swagger UI & ReDoc |
| Version Control | Git & GitHub |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/RiyaKhushiRadha/youtube-transcript-api.git
```

Move into the project directory:

```bash
cd youtube-transcript-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

Interactive API documentation will be available via Swagger UI.

ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

---

# 🧪 Running Tests

Execute all unit tests:

```bash
pytest
```

Expected output:

```
========================
7 passed
========================
```

All tests are also executed automatically using GitHub Actions whenever changes are pushed to the `main` branch.

---

# 📂 Project Structure

```
youtube-transcript-api/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── src/
│   ├── api/
│   ├── exceptions/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📜 License

This project is licensed under the MIT License.

See the LICENSE file for more information.

---

# 👩‍💻 Author

**Riya**

- GitHub: https://github.com/RiyaKhushiRadha
- LinkedIn: https://www.linkedin.com/in/riya-5a137932a/

If you found this project useful, consider giving it a ⭐ on GitHub.
