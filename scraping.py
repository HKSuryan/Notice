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



def notices():
    # Send a request to the website
    url = 'https://www.msit.in/notices'
    html_text = requests.get(url).text
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_text, 'lxml')

    tab_content_div = soup.find('div', {'class':'tab-content'})
    

    if tab_content_div:
        links_with_images = []
        li_tags = tab_content_div.find_all('li')
        for li in li_tags:
            if li.find('img'):
                a_tag = li.find('a')
                if(a_tag.get('href') != '#'):
                    linktext = ("https://www.msit.in/"+a_tag.get('href'))
                    links_with_images.append({"link":linktext})

        return links_with_images
    else:
        return []


def news():
    url = 'https://www.msit.in/latest_news'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    tab_content_div = soup.find('div', {'class':'tab-content'})
    

    if tab_content_div:
        links_with_images = []
        li_tags = tab_content_div.find_all('li')
        for li in li_tags:
            if li.find('img'):
                a_tag = li.find('a')
                if(a_tag.get('href') != '#'):
                    linktext = ("https://www.msit.in/"+a_tag.get('href'))
                    links_with_images.append({"link":linktext})

        return links_with_images
    else:
        return []