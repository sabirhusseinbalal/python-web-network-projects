import requests
from bs4 import BeautifulSoup


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
        soup = BeautifulSoup(response.text, 'html.parser')

        meta_tags = soup.find_all('meta')

        tag_list = ["description", "keywords", "og:title", "og:description"]


        # Output
        print("\n------------------------------")
        print(f"Requested URL: {url}")
        print(f"Status Code: {response.status_code}")
        #
        title = soup.title.string if soup.title else "No title found"
        print(f"Title: {title}")
        for tag in meta_tags:
            name = tag.get('name') or tag.get('property')
            content = tag.get('content')
            if name in tag_list and content:
                print(f"{name}: {content}")
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