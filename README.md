Ethical Web Scraping Project (Python)

📌 Overview
This project demonstrates three types of ethical Python web scrapers:
- Static scraping** using `BeautifulSoup`
- Scalable scraping** using `Scrapy`
- Dynamic JS scraping** using `Playwright`

All scripts are designed with built-in middleware to respect ethical and legal constraints, including robots.txt, User-Agent transparency, and rate limiting.

📁 Project Structure

web_scraping_project/
├── beautifulsoup_scraper.py      # Static HTML scraper
├── scrapy_spider.py              # Asynchronous crawler with Scrapy
├── playwright_scraper.py         # Dynamic scraper with Playwright
├── ethical_mw.py                 # Middleware enforcing ethical rules
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation

⚙️ Setup Instructions
1. Clone or download this repository.
2. Install required packages:

bash
pip install -r requirements.txt
playwright install  # Needed for browser automation

For Jupyter Notebook users:
python
import nest_asyncio
nest_asyncio.apply()

🚀 Running the Scrapers
-BeautifulSoup Scraper:python beautifulsoup_scraper.py
-Scrapy Spider:scrapy runspider scrapy_spider.py
- Playwright Scraper:python playwright_scraper.py

✅ Ethical Middleware Highlights (`ethical_mw.py`)
- Respects `robots.txt` (via `urllib.robotparser`)
- Delays requests (rate limit = 1/sec)
- Custom `User-Agent`: identifies scraper with contact URL/email
- Logs scraping actions (can be extended to database or file)

📚 Research Context
This project supports the academic paper:
“Advanced Web Scraping with Python: Ethical, Legal, and Technical Challenges”
It benchmarks popular scraping tools and proposes best practices for responsible automation.

👤 Author
Shivani Joisar  
Master’s Student in Computer Science 
IU International University of Applied Sciences


### 🪪 License
MIT License — for educational and research purposes only.

---

### 🛑 Disclaimer
This project is intended for **ethical research and educational use only**. Do not scrape websites without explicit permission or in violation of their terms of service.
