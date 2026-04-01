# Webhook Sender & Listener

## Description
This project demonstrates how to send and receive webhook messages between a sender and a listener.

- The **listener** is a Flask server that waits for POST requests at `/webhook`.
- The **sender** script sends messages (JSON) to the listener.
- Can be used for testing APIs, webhooks, or notifications.


## Modules Used
- `requests` – send POST requests
- `flask` – create a simple webhook listener
- `random` – generate random fallback messages

## How to Run

1. Open one terminal and run the listener:
```bash
python listener.py
```
2. Open another terminal and run the sender:
```bash
python sender.py
```

3. Enter messages, or press Enter to send a random one.
4. Messages will appear in the listener terminal.

## Features
- Receives POST requests (listener)
- Sends messages to webhook (sender)
- Handles JSON data
- Simple real-world example


## Project Structure
```
11_webhook_sender_listener/
├── listener.py       # Flask listener
├── sender.py         # Sender script
└── README.md
```

## Notes
- Run listener first
- Then run sender
- Uses local server (127.0.0.1)
