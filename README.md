# Apartment Rental Telegram Bot

This project is a Krasnodar daily apartment rental platform with a Telegram channel catalog, Telegram bot concierge, FastAPI backend for webhooks, and admin panel, and Deploy-F deployment support.

## Deployment Instructions for Deploy-F
1. Clone the repository.
2. Set up your environment variables in a `.env` file based on `.env.example`.
3. Run the FastAPI application using your preferred method (Gunicorn, Uvicorn, etc.).
4. Deploy using Deploy-F following their specific instructions.
5. Ensure to manage webhooks for Telegram bot properly.

## Requirements
- FastAPI
- SQLAlchemy
- Alembic
- python-telegram-bot
- (list other dependencies)