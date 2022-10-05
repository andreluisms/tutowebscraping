# from attr import attr
import requests
import re
from bs4 import BeautifulSoup

def webscrapingFlyerhistory():
    URL = 'http://www.flyershistory.com/cgi-bin/ml-poffs.cgi'
    pagecontent = requests.get(URL)
    newSoup = BeautifulSoup(pagecontent.content,'lxml')
    dataset = [['Temporada', 'data do jogo', 'time1', 
                'placarTime1', 'time2', 'placarTime2']]
    for tr in newSoup.find_all("tr"):
        if(tr.find("font", attrs={'size':'+2'})):
            season = tr.text.strip()
        game = tr.find("td", text = re.compile("[1-9][0-9]?\-[A-Z]"))
        if(game != None):
            list = [season]
            cont = 1
            for td in game.parent.find_all("td"):
                if (cont > 6):
                    break
                if (td.text!= 'at'):
                    list.append(td.text.strip())
                cont+=1
            dataset.append(list)
    return dataset

# print (webscrapingFlyerhistory())
