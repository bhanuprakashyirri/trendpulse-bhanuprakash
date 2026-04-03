import pandas as pd

df = pd.read_json("data/raw.json")

# clean data
df = df.dropna(subset=["title", "url"])
df["created_at"] = pd.to_datetime(df["created_at"])

# IMPORTANT FIX (your CSV was broken)
df = df[["title", "points", "author", "url", "created_at"]]

df.to_csv("data/clean.csv", index=False)

print("process done")