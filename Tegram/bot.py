from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from Search.my_token import my_token
from Search.searching import search
from Search.query_search import query
class telegram_bot:
    
    def __init__(self):
        self.My_Token_BOT = my_token.telegram_token()

    async def start(self, update: Update, context: CallbackContext):
        await update.message.reply_text("Hola como te puedo ayudar")
        
    async def search(self, update: Update, context: CallbackContext):
        await update.message.reply_text(search(query(context.args).query_format(), my_token.google_token(), my_token.google_search_engine()).format_request())
    
    async def help(self, update: Update, context: CallbackContext):
        await update.message.reply_text(f' /start\n/search\n')
    def main(self):
        app = Application.builder().token(self.My_Token_BOT).build()
            
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("search", self.search))
        app.add_handler(CommandHandler("help", self.help))
        app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    bot = telegram_bot()
    bot.main()