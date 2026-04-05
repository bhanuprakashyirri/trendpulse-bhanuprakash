import requests
import json
import os
from datetime import datetime


# keywords for each category
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


# function to find category from title
def get_category(title):
    title = title.lower()

    for category, keywords in CATEGORIES.items():
        for word in keywords:
            if word in title:
                return category

    return None


# get top stories ids
print("getting story ids...")
ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
ids = requests.get(ids_url).json()

# take first 500
ids = ids[:500]


data = []
category_count = {key: 0 for key in CATEGORIES}

print("getting story details...")

for story_id in ids:

    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        res = requests.get(url).json()
    except:
        continue

    # skip if no data
    if not res or "title" not in res:
        continue

    title = res.get("title", "")

    # find category
    category = get_category(title)

    # skip if no category matched
    if not category:
        continue

    # max 25 per category
    if category_count[category] >= 25:
        continue

    item = {
        "post_id": res.get("id"),
        "title": title,
        "category": category,
        "score": res.get("score", 0),
        "num_comments": res.get("descendants", 0),
        "author": res.get("by"),
        "collected_at": datetime.now().isoformat()
    }

    data.append(item)
    category_count[category] += 1

    # stop if all categories filled
    if all(v >= 25 for v in category_count.values()):
        break


# create data folder if not exists
os.makedirs("data", exist_ok=True)

date_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date_str}.json"

# save file
with open(filename, "w") as f:
    json.dump(data, f, indent=4)


print(f"collected {len(data)} stories")
print(f"saved to {filename}")