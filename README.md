# E-commerce Web Crawler

## Overview
The `EcommerceCrawler` is a Python-based tool designed to discover and list all product URLs across multiple e-commerce websites. The tool supports scalability, robustness, and performance for large websites with deep hierarchies.

---

## Features

- **URL Discovery:** Automatically identifies product URLs using customizable URL patterns.
- **Scalability:** Uses multi-threading for concurrent crawling of multiple domains.
- **Dynamic Content Handling:** Extensible to support JavaScript-rendered pages via Selenium.
- **Efficiency:** Implements URL caching to avoid duplicate crawling.
- **Edge Case Management:** Handles common challenges like infinite scrolling and dynamic loading.
- **Configurable Settings:** Allows customization of maximum depth and parallel workers.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/singhviveka/ecommerce_crawler.git
   cd ecommerce-crawler
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   - Required libraries:
     - `requests`
     - `beautifulsoup4`
     - `concurrent.futures` (standard library in Python 3.2+)
---

## Usage

1. **Prepare the list of domains:**
   Create a Python list of domain names you want to crawl, for example:
   ```python
   domains = [
       "https://example1.com",
       "https://example2.com",
       "https://example3.com",
   ]
   ```

2. **Run the script:**
   Execute the `EcommerceCrawler` by running the main script:
   ```bash
   python ecommerce_crawler.py
   ```

3. **Output:**
   The script outputs the list of discovered product URLs in the terminal log. These can be saved to a file or database by extending the script.

---

## Configuration

### Parameters

- **`domains`**: List of e-commerce websites to crawl.
- **`max_depth`**: Maximum depth of links to crawl (default: 3).
- **`max_workers`**: Number of concurrent threads (default: 10).

### Customization

To modify the URL matching logic, update the `is_product_url` method with additional patterns:
```python
return re.search(r'/product/|/p/|/item/', url, re.IGNORECASE)
```

---

## Edge Case Handling

- **Infinite Scrolling/Dynamic Loading:**
  Extend the `fetch` method with Selenium for JavaScript-heavy pages.

- **Website Blocking:**
  - Use User-Agent rotation.
  - Integrate proxies to distribute requests across multiple IPs.

- **Large-Scale Domains:**
  - Persist intermediate results to a database or file system.

---

## Known Limitations

- May not detect all product URLs if the website employs unconventional URL structures.
- Requires customization for non-standard URL patterns or heavily AJAX-driven content.

---

## Future Enhancements

- **Metadata Extraction:** Fetch additional data like product names, prices, and categories.
- **Database Integration:** Save output to a database for further analysis.
- **Rate Limiting:** Add adjustable rate limits to manage API constraints or avoid bans.

---


