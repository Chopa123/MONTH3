import datetime
import requests
from bs4 import BeautifulSoup

URL = "https://oc.kg/#"
HEADERS = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
            "avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "UserAgent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
def get_html(url):
    response=requests.get(url=url, headers=HEADERS)
    return response

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    fields = soup.find_all(
        "div",
        class_= ("item"),
        limit = 6
    )
    parsers_data = []
    for item in fields:
        parsers_data.append({
            "title": item.find("a", class_="item").string.replace("\n", ""),
            "subTitle": item.find("a", class_="subtitle").string.replace("\n"),
            "url": item.find("a", class_="title").get("href"),
            "image": item.find("img").get("src")
        })

    return parsers_data



