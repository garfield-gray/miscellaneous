from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes 

TOKEN: Final = '7398227576:AAE82xkaOeFd7kqgatpGsthNyp5dmH18tRU'

USERNAME: Final = '@LinearAlgebraUTbot'

PROXY = {
    'scheme': 'socks5',
    'hostname': '127.0.0.1',
    'port': 2080
}


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Greetings!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('in case you need help just help')

async def tobenamed_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Greetings!')
    

# Responses

def handle_response(Text: str) -> str:
    text: str= Text.lower()
    
    if 'hello' in text:
        return 'hey to you'

    return 'I dont get you'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'{message_type} and says{text}')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    print(f'{update} and says{context.error}')

if __name__ == '__main__':
    
    app = Application.builder().token(TOKEN).proxy_url(PROXY).build()
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('tobenamed', tobenamed_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot

    app.run_polling(poll_interval=3)





