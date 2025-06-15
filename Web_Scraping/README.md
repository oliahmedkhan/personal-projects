# 🕸️ Book Web Scraper (Freelance Automation Project)

This Python script scrapes book data (Title, Price, Link) from all pages of [books.toscrape.com](https://books.toscrape.com/), a test website for web scraping practice.

## 🔧 Features

- Extracts book titles, prices, and links
- Handles all 50 pages using pagination
- Saves data into a clean CSV format (Excel compatible)

## 📂 Output

- File: `all_books_data.csv`
- Columns: Title | Price | Link
- Rows: ~1000+

## 🚀 How to Run

```bash
pip install requests beautifulsoup4 pandas
python book_scraper.py
```
