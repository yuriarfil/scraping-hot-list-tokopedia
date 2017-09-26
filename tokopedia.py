#Hot list tokopedia.com
import csv
import urllib
from bs4 import BeautifulSoup

with open("Hot_List_tokopedia.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["link","desc","price"])
    for page in range(5):
        url = "https://www.tokopedia.com/hot?page={}".format(page)
        html = urllib.urlopen(url)
        soup = BeautifulSoup(html,"lxml")
        List = soup.find_all("div", {"class":"span4 box p-10 box-white"})
        
        for i in List:
            try:
                link = i.find("a", {"class": "clearfix display-block hotlist-url"})['href']
                desc = i.find("div", {"class": "mt-5 fs-12 ellipsis"}).get_text()
                price = i.find("span", {"class": "red fs-14"}).get_text()
                
                print(link, desc, price)

                writer = csv.writer(f)
                writer.writerow([link,desc,price])
            except: AttributeError
