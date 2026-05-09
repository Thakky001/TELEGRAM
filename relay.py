from fastapi import FastAPI
import aiohttp
import os

app = FastAPI()

TELEGRAM_TOKEN   = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

@app.get("/ping")
@app.head("/ping")
async def ping():
    return {"status": "alive"}

@app.post("/notify")
async def notify(data: dict):
    msg = data.get("message", "")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text":    msg,
            "parse_mode": "HTML"
        }) as resp:
            return {"ok": resp.status == 200}