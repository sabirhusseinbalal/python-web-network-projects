import requests, json
import hashlib
from pathlib import Path
import shutil
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent


while True:
    try:
        # Input
        url = input("\nEnter URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Exiting...")
            break
        elif not url:
            continue

        # Fix URL
        if not url.startswith("http"):
            url = f"https://{url}"

        output_dir = BASE_DIR / "output"
        if output_dir.exists():
            confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
            if confirm != "y":
                print("Cancelled.")
                break
            shutil.rmtree(output_dir)
        
        output_dir.mkdir(parents=True, exist_ok=True)


        # Send request
        response = requests.get(url, timeout=5)

        data = response.json()

        records = data if isinstance(data, list) else [data]
        print(f"Processing {len(records)} record(s)...")


        df = pd.DataFrame(records)

        csv_path = output_dir / "data.csv"
        df.to_csv(csv_path, index=False)

        print("\n------------------------------")
        print(f"URL: {url}")
        print(f"Status: {response.status_code}")
        print(df.head(3))
        print(f"CSV saved to: {csv_path}")
        print("------------------------------\n")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    except Exception as e:
        print(f"Error: {e}")
