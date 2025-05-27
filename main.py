import os
import logging
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

RESPOSTAS = {
    "ansiedade": "Lance sobre Ele toda a sua ansiedade, porque Ele tem cuidado de vocês. (1 Pedro 5:7)",
    "medo": "Não temas, porque eu sou contigo; não te assombres, porque eu sou o teu Deus. (Isaías 41:10)",
    "fé": "Ora, a fé é o firme fundamento das coisas que se esperam. (Hebreus 11:1)",
    "tristeza": "O choro pode durar uma noite, mas a alegria vem pela manhã. (Salmos 30:5)",
    "culpa": "Portanto, agora nenhuma condenação há para os que estão em Cristo Jesus. (Romanos 8:1)"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie uma palavra (ex: ansiedade, medo, fé) e receba uma mensagem bíblica.")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    resposta = RESPOSTAS.get(texto, "Ainda não tenho uma resposta para isso, mas estou aprendendo!")
    await update.message.reply_text(resposta)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

# Para manter vivo no Render
from flask import Flask
app = Flask(__name__)

@app.route('/')
def keep_alive():
    return 'ConexãoViva Bot está rodando!'

if __name__ == '__main__':
    threading.Thread(target=main).start()
    app.run(host='0.0.0.0', port=10000)
if __name__ == '__main__':
    import threading
    threading.Thread(target=main).start()

    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def keep_alive():
        return 'ConexãoViva Bot está rodando!'

    app.run(host='0.0.0.0', port=10000)
