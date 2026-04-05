import pandas as pd
import matplotlib.pyplot as plt
import os

# load data
df = pd.read_csv("data/trends_analysed.csv")

# create output folder
os.makedirs("outputs", exist_ok=True)


# Chart 1: Top 10 stories
top10 = df.sort_values(by="score", ascending=False).head(10)

# shorten long titles
def short_title(t):
    return t[:50] + "..." if len(t) > 50 else t

titles = top10["title"].apply(short_title)

plt.figure()
plt.barh(titles, top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# Chart 2: Stories per category
counts = df["category"].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()


# Chart 3: Scatter
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()


# BONUS Dashboard
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

# Chart 1
axs[0].barh(titles, top10["score"])
axs[0].set_title("Top 10 Stories")
axs[0].set_xlabel("Score")
axs[0].set_ylabel("Title")
axs[0].invert_yaxis()

# Chart 2
axs[1].bar(counts.index, counts.values)
axs[1].set_title("Categories")
axs[1].set_xlabel("Category")
axs[1].set_ylabel("Count")
axs[1].tick_params(axis='x', rotation=30)

# Chart 3
axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[2].set_title("Score vs Comments")
axs[2].set_xlabel("Score")
axs[2].set_ylabel("Comments")
axs[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.subplots_adjust(left=0.25)
plt.tight_layout(pad=3)

plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs/")