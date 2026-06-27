import csv
import requests
from bs4 import BeautifulSoup

url = "https://foodpapa.com/"

def food_information():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("a")
    food_list = []

    for post in links[:5]:
        title = post.text.strip()
        link = post.get("href")

        if link:
            link = link.strip()
            food_list.append({
                "title": title,
                "link": link
            })

    return food_list


def save_to_csv(data):
    if not data:
        print("Nothing to save")
        return

    with open("food_top5.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(data)

    print("Saved to food_top5.csv")


food_data = food_information()
save_to_csv(food_data)
