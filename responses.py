from datetime import datetime
import scraping as scrap
from bs4 import BeautifulSoup
import requests

def sample_reponse(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Hey! How its going ?"
    elif user_message in("Notice","Notices"):
        h = scrap.main()

        return h
