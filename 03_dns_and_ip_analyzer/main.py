import requests
import socket

while True:
    try:
        # Get user input
        url = input("\nEnter URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Exiting...")
            break
        elif not url:
            continue

        # Fix URL
        if not url.startswith("http"):
            url = f"https://{url}"

        # Extract domain safely
        domain = url.replace("https://", "").replace("http://", "").split("/")[0]

        # Request
        response = requests.get(url, timeout=5)

        # Get IP
        ip = socket.gethostbyname(domain)

        # Output
        print("\n------------------------------")
        print(f"Requested URL: {url}")
        print(f"Domain: {domain}")
        print(f"Status Code: {response.status_code}")
        print(f"IP Address: {ip}")
        print("------------------------------\n")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except socket.gaierror:
        print("Unable to resolve domain.")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    except Exception as e:
        print(f"Error: {e}")