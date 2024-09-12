# Notice
### A telegram bot that fetches latest notices and latest news from my college website Maharaja Surajmal Insitute of Technology
### website - https://www.msit.in/

## How did I get the latest ?

### The problem with my college website was that with notices and news it did not provide me with timestamps
### Therefore for getting the latest I had to take some measures

### but not drastic ones 😂

### I just simply used a database in mycase mongodb
### with which I was comparing previous set of notices with latest ones
### and if there were any new ones I was sending them 

### Don't worry I was not storing all the Notices, was just storing the ones which had the new tag with them on the college website but as we know the new tag can be there for a while and I don't want the same notice again and again.

### The bot is scheduled to search for new notice for every 8 hours using APScheduler

## Setup

### Just get API_KEY for the bot from BotFather
### Get The mongoURI by creating a database in MongoDB 
### create collections with name notice and news
### get your chat_id so that the bot can send you messages
### install the required packages using pip install -r requirements.txt

### add these to .env file with proper names

### run the bot using flask --app deploy run   

### thats all you got your NoticeBot !! Enjoy!!

### Thanks for dropping by !!

