from lxml import html
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup
import concurrent.futures

#
# get all synopsis
#

destination_directory = "./text_data/raw_data/"

def get_single_synopsis(context):
    print("get single synopsis invoked")
    url = context['url']
    title = context['title']
    page = requests.get(url)
    tree = html.fromstring(page.content)

    syno = tree.xpath('//ul[@id="plot-synopsis-content"]/li')
    string = html.tostring(syno[0]).decode('utf-8')
    string = BeautifulSoup(string, 'lxml').get_text()
    

    summaries = tree.xpath('//ul[@id="plot-summaries-content"]/li/p')
    string2 = ""

    for tag in summaries:
        tmp =html.tostring(tag).decode('utf-8')
        tmp = BeautifulSoup(tmp, 'lxml').get_text()
        string2 += tmp
 
    if "It looks like we don't have a Synopsis for this title yet." in string:
        string = ""
    string += string2
    with open(destination_directory+url.split("/")[-2]+".txt", "w", encoding='utf-8') as f:
        f.write(title+"\n")
        f.write(string)
    print("pobrano")



def get_all_synopsis(context_list):
    print("get all synopsis invoked")
    with concurrent.futures.ProcessPoolExecutor() as e:
        e.map(get_single_synopsis,context_list)


#
#  get movie titles and urls
#
def get_titles_and_urls():
    retList = []
    page = requests.get("https://www.imdb.com/chart/top/")
    tree = html.fromstring(page.content)

    syno = tree.xpath('//td[@class="titleColumn"]/a')

    for i in syno:
        tmp = {}
        tmp['title'] = i.text
        tmp['url'] ="https://www.imdb.com"+i.get("href").split("?")[0]+"plotsummary"
        retList.append(tmp)

    
    return retList



if __name__ == '__main__':
    li = get_titles_and_urls()
    get_all_synopsis(li)
    