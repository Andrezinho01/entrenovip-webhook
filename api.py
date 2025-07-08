from fastapi import FastAPI, Request
import logging
from telegram import Bot

app = FastAPI()
bot_token = "8093834027:AAESSSVj8RooYhjfbWJbGlf72rnhCf1TeTg"
bot = Bot(token=bot_token)

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("📥 Webhook recebido:", data)

    try:
        if data.get("status") == "PAID_OUT":
            external_ref = data.get("externalreference", "")
            if "_" in external_ref:
                user_id = external_ref.split("_")[0]
                await bot.send_message(chat_id=user_id, text="✅ Pagamento confirmado com sucesso!\nClique aqui para acessar seu conteúdo VIP: https://t.me/entregas_entrenovip")
        return {"status": "ok"}
    except Exception as e:
        logging.exception("Erro ao processar webhook:")
        return {"status": "error", "message": str(e)}
