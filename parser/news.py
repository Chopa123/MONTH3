import datetime
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
            "avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "UserAgent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def date_url(year, month, day, ordering):
    url = f"https://www.securitylab.r" \
          f"{year}-{month}-{day}" \
          f"&order={ordering}"
    return url
def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    fields = soup.find_all("div", class_= ("article-card-details"), limit =6)
    parsers_data = []
    for item in fields:
        parsers_data.append({
            "title": item.find("a", class_="article-card-title").getText("\n", ""),
            "url": item.find("a", class_="article-card-title").get("href"),
            "time": item.find("div", class_="article-card-details").getText().strip()


        })

    return parsers_data

def parser():
    current_date = datetime.datetime.now()
    url = date_url(current_date.year, current_date.month, current_date.day, "time")
    html = get_html(url)
    parsers_data = get_data(html.text)
    return parsers_data



