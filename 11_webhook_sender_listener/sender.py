import requests
import random

# Predefined fallback messages
messages = [
    "Hello World!",
    "Hey Programmer, Keep Hustling!",
    "Stay Focused, Stay Determined!",
    "Success Is the Sum of Small Efforts!",
    "Keep Learning and Growing!",
    "Your Efforts Will Pay Off!",
    "Embrace Challenges, They Make You Stronger!",
    "Stay Motivated, Stay Positive!",
    "Never Give Up, Great Things Take Time!",
    "Believe in Yourself!",
    "Keep Pushing Forward!"
]

while True:
    try:
        msg = input("\nEnter message (or press Enter for random, 'q' to quit): ")

        if msg.lower() == "q":
            print("Exiting...")
            break

        if not msg:
            msg = random.choice(messages)  # Use a random message if empty

        url = "http://127.0.0.1:5000/webhook"  # Listener URL
        data = {"message": msg}

        response = requests.post(url, json=data, timeout=5)
        print(f"Sent! Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    except Exception as e:
        print(f"Error: {e}")
