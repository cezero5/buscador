from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from Search.my_token import My_Token
from Search.searching import Search
from Search.query_search import Query
class telegram_bot:
    
    def __init__(self):
        self.My_Token_BOT = My_Token.telegram_token()

    async def start(self, update: Update, context: CallbackContext):
        await update.message.reply_text("Hola como te puedo ayudar")
        
    async def search(self, update: Update, context: CallbackContext):
        await update.message.reply_text(Search(Query(context.args).query_format(), My_Token.google_Token(), My_Token.google_search_engine()).format_request())
    
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