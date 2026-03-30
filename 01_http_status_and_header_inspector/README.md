# HTTP Status & Header Inspector

## Description
Inspects a website by sending an HTTP request and displaying the response status code and headers.
This project introduces network fundamentals and prepares you for API automation and web scraping.

It shows:
- Status code (e.g., 200 OK, 404 Not Found)
- Response headers (metadata about the page)
- Handles basic user errors and timeouts


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
- Accepts URL input from the user
- Automatically fixes URLs starting with www.
- Displays HTTP status code
- Displays response headers in a clean format
- Handles connection errors and request timeouts
- Loop until user exits
- Simple, beginner-friendly logic


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
