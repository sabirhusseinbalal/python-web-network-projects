# HTTP Status & Header Inspector

## Description
Sends an HTTP request to a website and shows the response status code and headers.
Helps understand network fundamentals and prepares you for API automation and web scraping.

It shows:
- Status code (e.g., 200 OK, 404 Not Found)
- Response headers (metadata about the page)
- Handles basic user errors and timeouts

**YouTube Video:**
[[HTTP Status & Header Inspector | Web, Network & API Automation (Project 1)](https://youtu.be/4npsk48_QaA/)]


## Modules Used
- `requests` – send HTTP requests and get responses


## Output
```
Enter URL (or 'q' to quit): https://sabirhusseinbalal.github.io

------------------------------
Requested URL: https://sabirhusseinbalal.github.io
Status Code: 200
Headers:
---------
Connection: keep-alive
Content-Length: 3970
Server: GitHub.com
Content-Type: text/html; charset=utf-8
Last-Modified: Fri, 06 Mar 2026 06:21:43 GMT
...
------------------------------


Enter URL (or 'q' to quit):
```


## Features
- Accepts URL input
- Fixes URLs starting with `www.`
- Displays HTTP status code and headers
- Handles timeouts and connection errors
- Loop until exit


## Project Structure
```
01_http_status_and_header_inspector/
├── main.py
└── README.md
```


## Notes
- Type q to quit anytime
- The project focuses on network fundamentals
- Keeps logic simple and clear for beginners
