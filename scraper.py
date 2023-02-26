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
    html = soup.find_all('div', class_='Wrapper-sc-11673k2-0 eHVkAX')

    matches = []


    for job in html: 
        matches.append({'role': job.find('div', class_='sc-fzooss kBgtGS').text, 'company': job.find('div', class_='sc-fzoiQi kuzZTz').text, 'salary': job.find('dl', class_='sc-fzoJMP jpodhy').text})

    

    print(matches)
    



parse_data_articles(html)

