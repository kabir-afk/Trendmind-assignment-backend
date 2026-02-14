# LinkedIn Post Creator — Backend

A small Django REST API that generates LinkedIn post drafts using Google's GenAI (`google.genai`). This project is an assignment backend implementing a single endpoint to create post content from simple parameters.

**Why this is useful**

- Quickly prototype AI-generated social posts for content strategies.
- Demonstrates integrating a generative AI client into a Django REST endpoint.
- Minimal, easy-to-run example suitable for learning and small experiments.

## Features

- Single REST endpoint to generate LinkedIn posts from: tone, target audience, topic, and length.

## Getting started

Prerequisites

- Python 3.10+ installed
- Git (to clone the repository)

Install dependencies

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# or, if no requirements file exists:
pip install Django djangorestframework python-dotenv django-environ google-genai
```

Environment variables

- The app requires a `GEMINI_API_KEY` to call the Google GenAI client. Place it in a `.env` file at the project root.

```
GEMINI_API_KEY=your_api_key_here
```

Run migrations and start the dev server

```bash
python manage.py migrate
python manage.py runserver
```

The API base is available at `http://localhost:8000/api/v1/`.

## Usage

Endpoint: `POST /api/v1/generate`

Request JSON (example):

```json
{
  "tone": "professional",
  "targetAudience": "startup founders",
  "topic": "fundraising tips",
  "length": "short"
}
```

cURL example

```bash
curl -X POST http://localhost:8000/api/v1/generate \
  -H "Content-Type: application/json" \
  -d '{"tone":"professional","targetAudience":"founders","topic":"pitching","length":"short"}'
```

Python example (requests)

```python
import requests

payload = {
    "tone": "professional",
    "targetAudience": "startup founders",
    "topic": "fundraising tips",
    "length": "short"
}

resp = requests.post('http://localhost:8000/api/v1/generate', json=payload)
print(resp.status_code, resp.text)
```

## Important notes

- Do NOT commit `.env` or your API key to the repository. Add `.env` to your `.gitignore`.
- The example view loads the API key from Django settings — see [backend/settings.py](backend/settings.py) for details.
- The API route is defined in [api/urls.py](api/urls.py) and implemented in [api/views.py](api/views.py).
