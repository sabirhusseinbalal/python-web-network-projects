import requests

while True:
    try:
        # Get user input
        url = input("\nEnter URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Exiting...")
            break
        elif not url:
            continue

        # Fix URLs starting with 'www.' automatically
        if url.startswith("www."):
            url = f"https://{url}"

        # Send GET request with timeout
        response = requests.get(url, timeout=5)

        # Output basic info
        print("\n------------------------------")
        print(f"Requested URL: {url}")
        print(f"Status Code: {response.status_code}")
        print("Headers:")
        print("---------")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        print("------------------------------\n")

    # Timeout handling
    except requests.exceptions.Timeout:
        print("Request timed out.")

    # Connection errors, DNS failure, etc.
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    # Any other unforeseen errors
    except Exception as e:
        print(f"Error: {e}")