import requests
from bs4 import BeautifulSoup
import pprint

urls = ['https://news.ycombinator.com/news?p=' + str(page) for page in range(1,5)]

mega_links = []
mega_subtext = []

for url in urls:
    res = requests.get(url, timeout=30)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')
    
    mega_links.extend(links)
    mega_subtext.extend(subtext)
    
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText() 
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points}) 
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
