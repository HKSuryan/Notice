from bs4 import BeautifulSoup
import requests
def main():
    url = 'https://www.msit.in/latest_news'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    title = soup.title
    anchors = soup.find_all('a')# anchor tags
    #Getting links from the tags
    all_links = set()
    links = set()
    for link in anchors:
        try:
            if(link.get('href') != '#'):
                #print(link.get('href'))
                linktext = ("https://www.msit.in/"+link.get('href'))
                all_links.add(link)
                links.add(linktext)
    
        except TypeError:
            pass
    return links
#print(circulars)