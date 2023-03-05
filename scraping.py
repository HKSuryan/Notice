from bs4 import BeautifulSoup
import requests
def main():
    url = 'https://www.msit.in/latest_news'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    circulars = soup.find_all('div', class_='tab-content')
    title = soup.title
    links = []
    table = soup.find('div',{'class':'tab-content'})
    anchor = table.find_all('a')
    i =0 
    for link in anchor:
            if(i != 5):
                if(link.get('href') != '#'):
                    linktext = ("https://www.msit.in/"+link.get('href'))
                    links.append(linktext)

            i +=1


    return links
def main1():
    url = 'https://www.msit.in/notices'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    circulars = soup.find_all('div', class_='tab-content')
    title = soup.title
    links = []
    table = soup.find('div',{'class':'tab-content'})
    anchor = table.find_all('a')
    i =0 
    for link in anchor:
            if(i != 5):
                if(link.get('href') != '#'):
                    linktext = ("https://www.msit.in/"+link.get('href'))
                    links.append(linktext)

            i +=1


    return links
