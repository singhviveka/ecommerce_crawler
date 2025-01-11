import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import re
import logging

logging.basicConfig(level=logging.INFO)


class EcommerceCrawler:
    def __init__(self, domains, max_depth=3, max_workers=10):
        self.domains = domains
        self.visited = set()
        self.product_urls = []
        self.max_depth = max_depth
        self.max_workers = max_workers

    def fetch(self, url):
        try:
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                return response.text
        except requests.RequestException as e:
            logging.error(f"Request failed for {url}: {e}")
        return None

    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = urljoin(base_url, a_tag['href'])
            parsed_url = urlparse(href)
            if parsed_url.netloc in base_url:
                links.add(href)
        return links

    def is_product_url(self, url):
        return re.search(r'/product/|/p/|/item/', url, re.IGNORECASE)

    def crawl(self, url, depth):
        if depth > self.max_depth or url in self.visited:
            return
        self.visited.add(url)

        logging.info(f"Crawling: {url} at depth {depth}")

        html = self.fetch(url)
        if not html:
            return

        if self.is_product_url(url):
            self.product_urls.append(url)

        links = self.extract_links(html, url)
        for link in links:
            self.crawl(link, depth + 1)

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            tasks = [executor.submit(self.crawl, domain, 1) for domain in self.domains]
            for task in tasks:
                task.result()  # Wait for all tasks to complete
        return self.product_urls


if __name__ == "__main__":
    domains = [
        "https://www.amazon.com",
        "https://example2.com",
        "https://example3.com",
    ]

    crawler = EcommerceCrawler(domains=domains, max_depth=3)
    product_urls = crawler.run()

    logging.info(f"Discovered Product URLs: {product_urls}")
