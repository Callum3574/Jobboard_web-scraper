import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.totaljobs.com/jobs/software-engineer?radius=10'


def get_html(url):
    if url:
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf_8")
        return html
    else:
        "unable to process", 400

html = get_html(url)


def parse_data_articles(html):
    soup = BeautifulSoup(html, "html.parser")
    html = soup.select(".sc-fzoiQi, h2")
    matches = []


    for job in html: 
        matches.append([job.text.strip()])

    

    print(matches)
    



parse_data_articles(html)

