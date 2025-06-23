# 📚 BookScraper - Paginated Web Scraper for Books to Scrape

A professional Python web scraping project that extracts book data from [Books to Scrape](http://books.toscrape.com), including pagination handling. Built using `requests`, `BeautifulSoup`, and `pandas`. Exports results to both CSV and Excel formats.

---

## 🔍 Features

- Scrapes book data from multiple pages (pagination support)
- Extracts:
  - ⭐ Book Rating
  - 🔗 Product Link
  - 💰 Price
  - 📦 Stock Availability
- Saves data in:
  - `books.csv`
  - `books.xlsx`
- Console logs for monitoring scraping progress

---

## 🛠️ Technologies Used

- Python 3.x
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
- [Pandas](https://pypi.org/project/pandas/)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zainchodry/pagination-scraper.git
   cd pagination-scraper


2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies
pip install -r requirements.txt


4. How to Run
python3 scraping.py
