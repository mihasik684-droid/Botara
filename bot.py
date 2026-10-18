import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
MY_ID = 123456789
TOKEN = os.environ["BOT_TOKEN"]
async def nuke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_ID:
        return
    if len(context.args) < 2:
        await update.message.reply_text("Пример: /nuke Привет 10")
        return
    try:
        count = int(context.args[-1])
    except ValueError:
        await update.message.reply_text("Последним аргументом укажи число.")
        return
    message = " ".join(context.args[:-1])
    count = max(1, min(count, 20))
    for _ in range(count):
        await update.message.reply_text(message)
        await asyncio.sleep(1)
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("nuke", nuke))
    app.run_polling()
if __name__ == "__main__":
    main()
