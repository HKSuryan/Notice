from bs4 import BeautifulSoup
import requests
def main():
    url = 'https://www.msit.in/latest_news'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    circulars = soup.find_all('div', class_='tab-content')
    title = soup.title
    #anchors = soup.find_all('a')# anchor tags
    #Getting links from the tags
    all_links = set()
    links = []
    table = soup.find('div',{'class':'tab-content'})
    anchor = table.find_all('a')
    i =0 
    for link in anchor:
            if(i != 5):
                if(link.get('href') != '#'):
                    #print(link.get('href'))
                    linktext = ("https://www.msit.in/"+link.get('href'))
                    all_links.add(link)
                    links.append(linktext)

            i +=1


    return links
#print(circulars)
