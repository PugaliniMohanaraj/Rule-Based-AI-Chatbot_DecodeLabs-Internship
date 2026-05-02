# Rule-Based AI Chatbot

A small web chat UI backed by a **Flask** API. The bot uses a fixed dictionary of phrases (no ML). The frontend is a single-page interface served from the same app.

## Features

- Chat UI with dark/light theme (stored in the browser)
- `POST /api/chat` returns JSON replies from predefined intents
- Sending `exit` ends the session until the user clicks **Clear**

## Requirements

- Python 3.10+ (recommended)
- Dependencies listed in `requirements.txt`

## Local setup

From the project root (this folder):

```bash
python -m venv .venv
```

Activate the virtual environment (Windows PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

### Production-style run (optional)

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```


## Deploy on Render

1. Push this repository to GitHub (or another Git provider Render supports).
2. Create a **Web Service**, environment **Python**.
3. **Build command:** `pip install -r requirements.txt`
4. **Start command:** `gunicorn --bind 0.0.0.0:$PORT app:app`

Ensure `app.py` and `index.html` stay at the **repository root** (or set Render’s root directory to match). On the free tier, the service may spin down when idle; the first request after idle can be slow.

## Project layout

```
.
├── app.py            # Flask app and rule-based responses
├── index.html        # Chat UI (styles may be inline in this file)
├── requirements.txt  # flask, gunicorn
└── README.md
```

## License

Add a license if you publish this project publicly.
