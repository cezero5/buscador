from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

My_Token_BOT = '8368261990:AAE9uMj4yNqQJVGSR1PQEdDHAyrCiahRSwQ'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hola como te puedo ayudar")

def main():
    app = Application.builder().My_Token(My_Token_BOT).build()
        
    app.add_handler(CommandHandler("start", start))
    
    app.run_polling()

if __name__ == '__main__':
    main()