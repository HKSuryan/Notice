from telegram.ext import *
import const as keys
import responses as R
import scraping as scrap
from bs4 import BeautifulSoup
import requests
print("bot started")




def start_command(update, context):
    update.message.reply_text('Type something random to get started !')


def help_command(update, context):
    update.message.reply_text('If you nedd help')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_reponse(text)
    if(type(response) == type(list())):
        count = 0 
        for link in response :
            if(count == 5):
                break
            count +=1
            update.message.reply_text(link)
    else:
        update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
