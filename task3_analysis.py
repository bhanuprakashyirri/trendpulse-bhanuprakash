import pandas as pd
import numpy as np

# load cleaned csv
file_path = "data/trends_clean.csv"

print("loading data...")
df = pd.read_csv(file_path)

# basic info
print("\nLoaded data:", df.shape)

print("\nFirst 5 rows:")
print(df.head())


# averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))


# numpy stats
scores = df["score"].values

print("\n--- NumPy Stats ---")
print("Mean score:", round(np.mean(scores), 2))
print("Median score:", round(np.median(scores), 2))
print("Std deviation:", round(np.std(scores), 2))
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))


# category with most posts
top_category = df["category"].value_counts().idxmax()
top_count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")


# most commented post
max_comments_row = df.loc[df["num_comments"].idxmax()]

print(f'\nMost commented story: "{max_comments_row["title"]}" — {max_comments_row["num_comments"]} comments')


# new columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)

avg_score_val = df["score"].mean()
df["is_popular"] = df["score"] > avg_score_val


# save result
output_path = "data/trends_analysed.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")