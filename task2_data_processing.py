import pandas as pd
import os

# file path (change date if needed)
file_path = "data/trends_20260405.json"

# load json
print("loading data...")
df = pd.read_json(file_path)

print(f"loaded {len(df)} rows")


# remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"after removing duplicates: {len(df)}")


# drop missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"after removing nulls: {len(df)}")


# fix data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# remove low score posts
df = df[df["score"] >= 5]
print(f"after removing low scores: {len(df)}")


# clean title spaces
df["title"] = df["title"].str.strip()


# save csv
os.makedirs("data", exist_ok=True)
output_path = "data/trends_clean.csv"

df.to_csv(output_path, index=False)

print(f"\nsaved {len(df)} rows to {output_path}")


# category summary
print("\nstories per category:")
print(df["category"].value_counts())