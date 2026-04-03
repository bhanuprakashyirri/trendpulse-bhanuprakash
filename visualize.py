import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean.csv")

# TOP POSTS
cnt = df["author"].value_counts().head(10)

plt.figure(figsize=(10, 6))

colors = ["#1f77b4"] * len(cnt)
colors[0] = "#ff5733"

plt.barh(cnt.index, cnt.values, color=colors)

plt.xlabel("Number of Posts")
plt.title("Top Authors")
plt.gca().invert_yaxis()

for i, v in enumerate(cnt.values):
    plt.text(v + 0.1, i, str(v), va='center')

plt.tight_layout()
plt.savefig("authors.png")
plt.close()


# TOP AUTHORS
cnt = df["author"].value_counts().head(5)

plt.figure(figsize=(10, 6))

colors = ["#59a14f"] * len(cnt)
colors[0] = "#f28e2b"  # highlight top

plt.barh(cnt.index, cnt.values, color=colors, height=0.6)

plt.xlabel("Number of Posts", fontsize=12)
plt.title("Top Authors by Post Count", fontsize=14, fontweight='bold')

plt.gca().invert_yaxis()

# values
for i, v in enumerate(cnt.values):
    plt.text(v + 0.1, i, str(v), va='center', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig("authors.png")
plt.close()

print("visualization done")