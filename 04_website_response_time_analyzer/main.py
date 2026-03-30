import requests, time

while True:
    try:
        # Get user input
        url = input("\nEnter URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Exiting...")
            break
        elif not url:
            continue

        # Fix URLs 
        if not url.startswith("http"):
            url = f"https://{url}"


        times = []
        count = 4
        while count > 0:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            count-=1
            end_time = time.time() - start_time
            times.append(end_time)
        
        average = sum(times) / len(times)

        # Output basic info
        print("\n------------------------------")
        print(f"Requested URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Average time: {average:.2f} seconds")
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