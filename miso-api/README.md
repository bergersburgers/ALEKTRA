# MISO API Project

This project pulls electricity market and load/generation/interchange data from the MISO ISO API.

## Structure
- `main.py` - FastAPI application entry
- `schemas/` - Data models for request/response validation
- `routers/` - API route files (pricing, LGI)
- `utils/` - Helper functions for API calls
- `requirements.txt` - Python dependencies

## How to Run
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
uvicorn main:app --reload
