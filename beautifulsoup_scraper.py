import requests
from bs4 import BeautifulSoup
import time
from ethical_mw import EthicalScraper

class StaticScraper(EthicalScraper):
    def __init__(self, url):
        super().__init__(url)

    def scrape(self):
        self.before_request()
        response = requests.get(self.url, headers=self.headers)
        self.after_request()

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = [tag.text for tag in soup.find_all('h1')]
            print("Scraped H1 Tags:", titles)
        else:
            print("Failed to fetch page", response.status_code)

if __name__ == "__main__":
    scraper = StaticScraper("https://example.com")
    scraper.scrape()