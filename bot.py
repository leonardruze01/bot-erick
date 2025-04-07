import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TOKEN")  # Tomado de variable de entorno en Render

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Ir a curso de PostgreSQL", callback_data='postgres')],
        [InlineKeyboardButton("Ir a curso de Desarrollo de Virus Informático", callback_data='virus')],
        [InlineKeyboardButton("Ir a Tumblr", callback_data='tumblr')],
        [InlineKeyboardButton("Descargar vídeo de codificación", callback_data='codificacion')],
        [InlineKeyboardButton("Decodificación del bot datapan", callback_data='decodificacion')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Cursos de Eric Leonardo Ruiz Sánchez", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = {
        'postgres': "Aquí tienes el curso de PostgreSQL: [Enlace al curso](https://www.udemy.com/course/curso-completo-de-postgres-y-pg-admin-iii/)",
        'virus': "Curso de Desarrollo de Virus Informático: [Enlace al curso](https://www.udemy.com/course/curso-de-desarrollo-de-virus-en-diferentes-lenguajes-de-prog/)",
        'tumblr': "Visita el Tumblr de Eric: [https://eric.tumblr.com](https://www.tumblr.com/erlerusa?source=share)",
        'codificacion': "Descarga el vídeo de codificación: [Descargar](https://ejemplo.com/codificacion.mp4)",
        'decodificacion': "Video de decodificación del bot datapan: [Ver video](https://ejemplo.com/decodificacion)",
    }

    response = data.get(query.data, "Opción no válida.")
    await query.edit_message_text(text=response, parse_mode='Markdown')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()
