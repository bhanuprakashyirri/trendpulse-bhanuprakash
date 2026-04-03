import pandas as pd

df = pd.read_csv("data/clean.csv")

# top posts
top = df.sort_values(by="points", ascending=False).head(5)
print("\nTop posts:")
print(top[["title", "points"]])

# average
avg = df["points"].mean()
print("\nAverage points:", avg)

# authors
cnt = df["author"].value_counts().head(5)
print("\nTop authors:")
print(cnt)