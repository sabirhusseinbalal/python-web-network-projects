# News API Aggregator

## Description
Fetches news data from a public API based on a topic and shows the most relevant results.

This project helps understand how to:
- Work with real-world APIs
- Handle large JSON data
- Extract only useful information

It shows:
- Top news titles
- Related URLs
- Clean and limited output (first 5 results)

**YouTube Video:**
[[News API Aggregator | Web, Network & API Automation (Project 10)](https://youtu.be/oD-blCPlETg/)]

## Modules Used
- `requests` – send HTTP requests
- `json` – handle API response data

## Output
```
Enter Topic Name (or 'q' to quit): Sabir Hussain Balal

------------------------------
Requested URL: https://hn.algolia.com/api/v1/search?query=Sabir Hussain Balal
Final Status: 200

Top Results:

Title: None
URL: None
------------------------------
------------------------------


Enter Topic Name (or 'q' to quit): Python Coding

------------------------------
Requested URL: https://hn.algolia.com/api/v1/search?query=Python Coding
Final Status: 200

Top Results:

Title: Python coding interview challenges
URL: https://github.com/donnemartin/coding-challenges
------------------------------
Title: Python coding interview challenges
URL: https://github.com/donnemartin/interactive-coding-challenges
------------------------------
Title: Ask HN: Advanced Python Coding Books
URL: None
------------------------------
Title: CodingBat: Python
URL: http://codingbat.com/python
------------------------------
Title: Properly setting Vim up for Python coding
URL: http://blog.sontek.net/2008/05/11/python-with-a-modular-ide-vim/
------------------------------
------------------------------


Enter Topic Name (or 'q' to quit):
```

## Features
- Accepts topic input
- Fetches news from API
- Displays top results
- Handles errors and timeouts
- Loop until exit



## Project Structure
```
10_news_api_aggregator/
├── main.py
└── README.md
```

## Notes
- Some results may not have title or URL
- API returns large data, but we only extract useful parts
- Focus is on filtering and understanding JSON structure
