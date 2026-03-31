# Async Web Scraper (aiohttp)

## Description
Fetches multiple websites at the same time using async programming.
This project helps understand how to run multiple network requests together instead of one by one.

It extracts:
- Status code
- Page title
This is faster than normal requests and introduces async concepts.


## Modules Used
- `aiohttp` – async HTTP requests
- `asyncio` – run tasks together
- `bs4 (BeautifulSoup)` – parse HTML

## Output
```
Enter up to 5 URLs (or 'q' to quit):
1: https://sabirhussainbalal.github.io
2: https://sabirhusseinbalal.github.io 
3: www.facebook/sabirhusseinbalal
4: https://www.youtube.com/@sabirhusseinbalal
5: https://steamcommunity.com/id/sabirhusseinbalal/

------------------------------
URL: https://sabirhussainbalal.github.io
Status: 200
Title: Heartfelt Harmony Music App
------------------------------
URL: https://sabirhusseinbalal.github.io
Status: 200
Title: My Game Hub | Sabir Hussain Balal
------------------------------
URL: https://www.facebook/sabirhusseinbalal
Status: Error
Title: Cannot connect to host www.facebook:443 ssl:default [getaddrinfo failed]
------------------------------
URL: https://www.youtube.com/@sabirhusseinbalal
Status: 200
Title: Rise with Purpose. - YouTube
------------------------------
URL: https://steamcommunity.com/id/sabirhusseinbalal/
Status: 200
Title: Steam Community :: L4$T D4Y.
------------------------------
------------------------------


Enter up to 5 URLs (or 'q' to quit):
```

## Features
- Takes multiple URLs
- Runs all requests at the same time
- Extracts page title
- Handles errors safely
- Simple async logic



## Project Structure
```
12_async_web_scraper/
├── main.py
└── README.md
```

## Notes
- Uses async instead of normal requests
- Faster for multiple websites
- Good intro to real-world scraping