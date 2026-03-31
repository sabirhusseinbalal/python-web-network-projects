import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    try:
        if not url.startswith("http"):
            url = f"https://{url}"

        async with session.get(url, timeout=5) as response:
            text = await response.text()

            soup = BeautifulSoup(text, "html.parser")

            title = soup.title.string if soup.title else "No title"

            return {
                "url": url,
                "status": response.status,
                "title": title
            }

    except Exception as e:
        return {
            "url": url,
            "status": "Error",
            "title": str(e)
        }


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in urls:
            tasks.append(fetch(session, url))

        results = await asyncio.gather(*tasks)

        print("\n------------------------------")
        for res in results:
            print(f"URL: {res['url']}")
            print(f"Status: {res['status']}")
            print(f"Title: {res['title']}")
            print("-" * 30)
        print("------------------------------\n")


while True:
    urls = []
    print("\nEnter up to 5 URLs (or 'q' to quit):")

    for i in range(5):
        url = input(f"{i+1}: ").strip()

        if url.lower() == "q":
            exit()

        if url:
            urls.append(url)

    if urls:
        asyncio.run(main(urls))