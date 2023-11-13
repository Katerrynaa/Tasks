from telegram.ext import Updater, Update, CallbackContext, CommandHandler, MessageHandler, Filters

updater = Updater("6524720663:AAEXM5cc7ve0DN9gTDy7yKbyOjGQPXSTAc4", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Hello! Welcome to the Chat Bot. You got into the volunteers team who help ukrainian develop and bring our country closer to vicroty.'
    )