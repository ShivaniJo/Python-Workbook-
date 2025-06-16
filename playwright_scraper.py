import asyncio
from playwright.async_api import async_playwright
from ethical_mw import EthicalScraper

class DynamicScraper(EthicalScraper):
    async def scrape(self):
        self.before_request()
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(user_agent=self.headers['User-Agent'])
            page = await context.new_page()
            await page.goto(self.url)
            titles = await page.locator("h1").all_text_contents()
            print("Playwright H1 Titles:", titles)
            await browser.close()
        self.after_request()

if __name__ == "__main__":
    scraper = DynamicScraper("https://example.com")
    asyncio.run(scraper.scrape())
