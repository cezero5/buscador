from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from Search.my_token import my_token
from Search.searching import search
from Search.query_search import query
import logging
 
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
class telegram_bot:
    
    def __init__(self):
        self.My_Token_BOT = my_token.telegram_token()

    async def start(self, update: Update, context: CallbackContext):
        await update.effective_message.reply_text("Hola como te puedo ayudar")
        
    async def search(self, update: Update, context: CallbackContext):
        if not context.args:
            await update.effective_message.reply_text("Uso: /search palabra_clave -d=dominio.com .......")
            return
        try:
            q = query(context.args).query_format()
            result = search(q, my_token.google_token(), my_token.google_search_engine()).format_request()
            await update.effective_message.reply_text(result)
        except Exception as e:
            await update.effective_message.reply_text("No pude completar la busqueda ahora mismo. Intentar mas tarde")
            print(f"[ERROR search]: {e}")
    
    async def help(self, update: Update, context: CallbackContext):
        texto = (
            "*Comandos disponibles*\n\n"
            "/start - Inicia el bot\n"
            "/search <consulta> - Busca en Google\n"
            "/help - Muestra esta ayuda\n\n"
            "*Filtros para /search*\n"
            "Puedes combinar varios en la misma búsqueda, separados por espacio.\n\n"
            "`-d=dominio.com` - Busca solo dentro de un sitio\n"
            "   ej: `/search python -d=stackoverflow.com`\n\n"
            "`-ft=pdf` - Busca solo un tipo de archivo\n"
            "   ej: `/search manual -ft=pdf`\n\n"
            "`-it=palabra` - La palabra debe estar en el título\n"
            "   ej: `/search -it=tutorial python`\n\n"
            "`-we=\"frase exacta\"` - Busca la frase exacta\n"
            "   ej: `/search -we=inteligencia artificial`\n\n"
            "`-e=palabra` - Excluye una palabra de los resultados\n"
            "   ej: `/search python -e=django`\n\n"
            "`-or=palabra1,palabra2` - Busca cualquiera de estas palabras\n"
            "   ej: `/search -or=gato,perro fotos`\n\n"
            "También puedes combinar varios valores separados por coma en un mismo filtro:\n"
            "`/search -d=linkedin.com,facebook.com nombre`"
        )
        await update.effective_message.reply_text(texto, parse_mode="Markdown")
 
    async def error_handler(self, update: object, context: CallbackContext):
        logging.error("Excepción no manejada:", exc_info=context.error)

    def main(self):
        app = Application.builder().token(self.My_Token_BOT).build()
            
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("search", self.search))
        app.add_handler(CommandHandler("help", self.help))
        app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    bot = telegram_bot()
    bot.main()