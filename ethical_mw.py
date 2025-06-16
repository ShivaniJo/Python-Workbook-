import time
import logging
import requests
from urllib import robotparser

class EthicalScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "EthicalBot/1.0 (https://yourproject.org/contact)"
        }
        self.last_request_time = 0

    def before_request(self):
        self._respect_robots()
        self._rate_limit()

    def after_request(self):
        logging.info(f"Fetched: {self.url} at {time.time()}")

    def _rate_limit(self):
        now = time.time()
        delay = max(1.0 - (now - self.last_request_time), 0)
        if delay > 0:
            time.sleep(delay)
        self.last_request_time = time.time()

    def _respect_robots(self):
        parsed_url = requests.utils.urlparse(self.url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
        rp = robotparser.RobotFileParser()
        rp.set_url(robots_url)
        try:
            rp.read()
            if not rp.can_fetch(self.headers['User-Agent'], self.url):
                raise PermissionError(f"Access disallowed by robots.txt: {self.url}")
        except Exception:
            logging.warning("robots.txt not accessible or ignored.")

def ethical_delay():
    time.sleep(1.0)