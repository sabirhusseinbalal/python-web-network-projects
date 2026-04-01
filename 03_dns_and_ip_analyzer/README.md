# DNS & IP Analyzer

## Description
Analyzes a website by resolving its domain and retrieving the IP address.

It shows:
- Requested URL
- Domain
- HTTP status code
- IP address

## Modules Used
- `requests` – send HTTP requests
- `socket` – resolve domain to IP address

## Output
```
Enter URL (or 'q' to quit): https://sabirhussainbalal.github.io

------------------------------
Requested URL: https://sabirhussainbalal.github.io
Domain: sabirhussainbalal.github.io
Status Code: 200
IP Address: 185.199.111.153
------------------------------


Enter URL (or 'q' to quit):
```

## Features
- Accepts URL input
- Fixes missing `https://`
- Extracts domain and resolves IP
- Handles invalid domains and connection errors
- Loop until exit


## Project Structure
```
03_dns_and_ip_analyzer/
├── main.py
└── README.md
```

## Notes
- Some websites may block requests (e.g., return 403)
- Invalid domains will not resolve to an IP
- Focus is on understanding DNS and basic networking
