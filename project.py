import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Whale/2.9.115.7 Safari/537.36"}
    res = requests.get(url,  headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(idx, title, link):
        print(f"{idx+1}. {title}")
        print(f"     (링크 : {link})")

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=havr1lprvN8sse01ZiGssssssA0-071191"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    crt_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    morning_rainfall = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rainfall = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()


    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm20 = dust.find_all("dd")[1].get_text()


    print(cast)
    print(f"현재 {crt_temp} (최저 {min_temp} / 최고 {max_temp})")
    print(f"오전 {morning_rainfall} / 오후 {afternoon_rainfall}")
    print(f"미세먼지 {pm10}")
    print(f"초미세먼지 {pm20}")

def scrape_news():
    print("\n[뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)

    for idx, headline in enumerate(news_list):
        title = headline.find("a").get_text().strip()
        link = url + headline.find("a")["href"]
        print_news(idx, title, link)

def scrape_IT():
    print("\n[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)

    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(idx, title, link)

def scrape_english():
    print("\n[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("\n(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())

    print("\n(한글 지문)")   
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())





if __name__ == "__main__":
    scrape_weather()
    scrape_news()
    scrape_IT()
    scrape_english()