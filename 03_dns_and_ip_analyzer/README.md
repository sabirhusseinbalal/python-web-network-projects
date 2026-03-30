# DNS & IP Analyzer

## Description
Analyzes a website by resolving its domain and retrieving the IP address.

It extracts:
- Requested URL
- Extracted domain
- HTTP status code
- IP address of the domain
This is a basic step toward understanding networking and how the internet works behind the scenes.

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
- Accepts URL input from the user
- Automatically fixes missing https://
- Extracts domain from URL
- Resolves domain to IP address using DNS
- Displays HTTP status code
- Handles invalid domains and connection errors
- Loop until user exits
- Simple and beginner-friendly logic


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
