import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

def create_soup(url):
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Whale/2.9.115.7 Safari/537.36"}
    res = requests.get(url,  headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(idx, title, link):
        print(f"{idx+1}. {title}")
        print(f"    LINK : {link}")


def scrape_weather():
    print("\nTODAY'S WEATHER")
    url = "https://www.google.com/search?q=today+weather+north+york&sxsrf=ALeKk02VsfJ4bWZfq3PBqpFJzITNpcq-CQ%3A1616562923082&ei=68paYMrSBMG4tAba1ZfoCw&oq=today+weather+north+york&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjECcQnQIQRhCAAjIECAAQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46BwgAEEcQsANQlEZYlEZguFJoAnACeACAAZwCiAGDA5IBBTAuMS4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz&ved=0ahUKEwiK9KWWlsjvAhVBHM0KHdrqBb0Q4dUDCA0&uact=5"
    soup = create_soup(url)
    location = soup.find("div", attrs={"class":"wob_loc mfMhoc"}).get_text()
    high_temp = soup.find("div", attrs={"class":"vk_gy gNCp2e"}).find("span", attrs={"style":"display:inline"}).get_text()
    low_temp = soup.find("div", attrs={"class":"QrNVmd ZXCv8e"}).find("span", attrs={"style":"display:inline"}).get_text()
    precipitation = soup.find("span", attrs={"id":"wob_pp"}).get_text()
    wind = soup.find("span", attrs={"id":"wob_ws"}).get_text()

    print(f"Location is {location}")
    print(f"Temperature is {high_temp}/{low_temp}° and wind is {wind}")
    print(f"There's a {precipitation} percent chance of showers today.")


def scrape_CN_TS():
    print("\nCANADA TOP STORIES:")
    url = "https://www.cbc.ca/news"
    cbc = "https://www.cbc.ca"
    soup = create_soup(url)
    news_topstories = soup.find_all("a", attrs={"class":re.compile("^card cardListing rightImage sclt-featurednewscontentlistcard")}, limit=4)

    for idx, topstories in enumerate(news_topstories):
        title = topstories.find("h3").get_text().strip()

        link = cbc + topstories["href"]
        print_news(idx, title, link)


# def scrape_CV_TR():
#     url = "https://covid-19.ontario.ca/data"
#     soup = create_soup(url)
#     # covid_main = soup.find("div", attrs={"class":"cviz-label-value "}).find_all("div", attrs={"class":"cviz-label-value--value "})[0].get_text()
#     # covid_main = soup.find_all("div", attrs={"class":"ontario-row"})[1].get_text()
#     covid_main = soup.find_element_by_xpath("//*[@id='ontario-covid-viz']/div[2]/div[1]/ul/li[1]/div/div[3]/span")
#     # covid_main = covid1.get_text()

#     print(covid_main)


def scrape_CV_TS():
    print("\nCOVID-19 TOP STORIES:")
    url = "https://www.cbc.ca/news/covid-19"
    cbc = "https://www.cbc.ca"
    soup = create_soup(url)
    covid_topstories = soup.find_all("a", attrs={"class":"contentWrapper"}, limit=4)

    for idx, topstories in enumerate(covid_topstories):
        title = topstories.find("h3").get_text().strip()

        link = cbc + topstories["href"]
        print_news(idx, title, link)


def scrape_FB_TS():
    print("\nEUROPE FOOTBALL TOP STORIES:")
    url = "https://www.bbc.com/sport/football"
    bbc = "https://www.bbc.com/"
    soup = create_soup(url)
    football_link = soup.find("a", attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-double-pica-bold"})
    football_headline = football_link.find("h3").get_text()
    football_topstories = soup.find_all("a", attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-pica-bold"}, limit=3)


    link = bbc + football_link["href"]
    print(f"1. {football_headline}")
    print(f"    LINK : {link}")

    
    for idx, topstories in enumerate(football_topstories):
        title = topstories.find("h3").get_text().strip()

        link = bbc + topstories["href"]
        print(f"{idx+2}. {title}")
        print(f"    LINK : {link}")

 
# def scrape_gossip():
#     print("\nEUROPE FOOTBAL GOSSIP")
#     url ="https://www.bbc.com/sport/football/gossip"
#     soup = create_soup(url)
#     football_gossip = soup.find("p", attrs={"data-reactid":re.compile("^.27dy6ust42g.0.0.0.1.$paragraph")}).get_text()
#     print(football_gossip)

#     # for idx, topstories in enumerate(football_gossip):
#     #     title = topstories.find("span").get_text()
#     #     print_news(idx, title)



if __name__ == "__main__":
    scrape_weather()
    scrape_CN_TS()
    scrape_CV_TS()
    scrape_FB_TS()

