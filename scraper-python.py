# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup


def scrape():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    url = 'https://www.espn.com/nba/boxscore/_/gameId/401716947'
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print(title)
    print(text)
    print(link)

if __name__ == '__main__':
    scrape()

