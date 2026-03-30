# URL Metadata Extractor

## Description
Extracts important metadata from a website by sending an HTTP request and parsing the HTML content.
This project helps understand how websites store information like titles, descriptions, and SEO data.

It extracts:
- Page title
- Meta description
- Meta keywords (if available)
- Open Graph data (og:title, og:description)
This is a basic step toward web scraping and SEO analysis.

## Modules Used
- `requests` – send HTTP requests
- `bs4 (BeautifulSoup)` – parse HTML content

## Output
```
Enter URL (or 'q' to quit): https://sabirhusseinbalal.github.io

------------------------------
Requested URL: https://sabirhusseinbalal.github.io
Status Code: 200
Title: My Game Hub | Sabir Hussain Balal
og:title: My Game Hub | Play Simple & Fun 2D Games
og:description: Enjoy free simple games like Dice, Rock–Paper–Scissors, and Guess Number — built by Sabir Hussain Balal.
------------------------------


Enter URL (or 'q' to quit):
```

## Features
- Accepts URL input from the user
- Automatically fixes URLs starting with www.
- Extracts page title safely
- Extracts important meta tags (SEO + OpenGraph)
- Skips empty or missing metadata
- Handles request errors and timeouts
- Loop until user exits
- Simple and beginner-friendly logic


## Project Structure
```
02_url_metadata_extractor/
├── main.py
└── README.md
```

## Notes
- Some websites may not have all metadata
- Keywords tag is often missing in modern websites
- Focus is on understanding HTML structure and parsing
