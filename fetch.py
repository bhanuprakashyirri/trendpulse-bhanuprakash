import requests
import json
import os

url = "https://hn.algolia.com/api/v1/search?tags=front_page"

r = requests.get(url)
data = r.json()

posts = []

for item in data["hits"]:
    temp = {
        "title": item.get("title"),
        "points": item.get("points"),
        "author": item.get("author"),
        "url": item.get("url"),
        "created_at": item.get("created_at")
    }
    posts.append(temp)

if not os.path.exists("data"):
    os.mkdir("data")

with open("data/raw.json", "w") as f:
    json.dump(posts, f, indent=2)

print("fetch done")