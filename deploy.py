from flask import Flask,render_template
import telegram
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import os
import scraping as scrap
from dotenv import load_dotenv
load_dotenv()
import  main as main
import certifi
from pymongo import MongoClient

mongoURI = os.getenv("mongoURI")
client = MongoClient(mongoURI, tlsCAFile=certifi.where())
db = client["NoticeBot"]
noticeCollection = db["notice"]
newsCollections = db["news"]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

def replace_collection_data(collection, new_data):

    existing_links = {item['link'] for item in collection.find({}, {'_id': 0, 'link': 1})}

    new_links = {item['link'] for item in new_data}
    links_to_add = new_links - existing_links
    new_links_not_in_db = new_links - existing_links

    if new_links_not_in_db:

        # collection.delete_many({})
        new_entries = [item for item in new_data if item['link'] in links_to_add]
        collection.insert_many(new_entries)

        # print({
        #     'message': f"Replaced old entries with {len(new_data)} new entries.",
        #     'new_links': list(new_links_not_in_db)
        # })
        return list(new_links_not_in_db)
    else:
        # print({
        #     'message': "No new entries found.",
        #     'new_links': []
        # })
        return []



API_KEY=os.getenv("API_KEY")
bot = telegram.Bot(token=API_KEY)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(), bot)
    chat_id = update.message.chat.id 

    bot.sendMessage(chat_id=chat_id, text="Hello! This is your chat ID.")
    return 'OK', 200

def handle_message(update):
    chat_id = update.message.chat.id
    latest_notice = scrap.notices()
    for i in latest_notice:
        bot.sendMessage(chat_id=chat_id, text=i)

def send_notices_periodically():
    latest_notice = scrap.notices()
    latest_news = scrap.news()
    chat_id = os.getenv("chatId")

    newLatestNotice = replace_collection_data(noticeCollection,latest_notice)
    newLatestNews = replace_collection_data(newsCollections,latest_news)



    s = "latest notices Total Count"+str(len(newLatestNotice))
    t = "latest new Total Count"+str(len(newLatestNews))

    if(len(newLatestNotice) != 0):
        bot.sendMessage(chat_id=chat_id,text="-----------------------------------------------------------------")
        bot.sendMessage(chat_id=chat_id,text=s)
        bot.sendMessage(chat_id=chat_id,text="-----------------------------------------------------------------")
        for i in newLatestNotice:
            bot.sendMessage(chat_id=chat_id, text=i)
        bot.sendMessage(chat_id=chat_id,text="-----------------------------------------------------------------")
    
    if(len(newLatestNews) != 0):
        bot.sendMessage(chat_id=chat_id,text="-----------------------------------------------------------------")
        bot.sendMessage(chat_id=chat_id,text=t)
        bot.sendMessage(chat_id=chat_id,text="-----------------------------------------------------------------")
        for i in newLatestNews:
            bot.sendMessage(chat_id=chat_id, text=i)
        bot.sendMessage(chat_id=chat_id,text="-----------------------------------------------------------------")


scheduler = BackgroundScheduler()
scheduler.add_job(send_notices_periodically, 'interval', minutes=480)
scheduler.start()

if __name__ == "__main__":
    app.run(debug = True)

