# TrendPulse

A Python data pipeline that collects trending stories from HackerNews, processes and cleans the data, performs statistical analysis, and generates visual charts — all automated end to end.

---

## Project Structure

```
trendpulse-bhanuprakash/
├── task1_data_collection.py    # Fetches and categorizes stories from HackerNews API
├── task2_data_processing.py    # Cleans and filters the raw data
├── task3_analysis.py           # Statistical analysis and feature engineering
├── task4_visualization.py      # Generates charts and a dashboard
├── data/
│   ├── trends_YYYYMMDD.json    # Raw collected data
│   ├── trends_clean.csv        # Cleaned data
│   └── trends_analysed.csv     # Analysed data with new columns
└── outputs/
    ├── chart1_top_stories.png  # Top 10 stories by score
    ├── chart2_categories.png   # Stories count per category
    ├── chart3_scatter.png      # Score vs comments scatter plot
    └── dashboard.png           # Combined dashboard (all 3 charts)
```

---

## Pipeline Overview

### Task 1 — Data Collection · `task1_data_collection.py`

Fetches the top 500 story IDs from the HackerNews API, then retrieves details for each story. Stories are categorized into 5 categories using keyword matching — up to 25 stories per category are collected.

Categories: `technology`, `worldnews`, `sports`, `science`, `entertainment`

Each story captures: `post_id`, `title`, `category`, `score`, `num_comments`, `author`, `collected_at`

Output: `data/trends_YYYYMMDD.json`

---

### Task 2 — Data Processing · `task2_data_processing.py`

Loads the raw JSON and cleans it:
- Removes duplicate entries (by `post_id`)
- Drops rows with missing `post_id`, `title`, or `score`
- Filters out low-quality posts with `score < 5`
- Strips extra whitespace from titles
- Casts `score` and `num_comments` to integers

Output: `data/trends_clean.csv`

---

### Task 3 — Analysis · `task3_analysis.py`

Loads the cleaned CSV and computes:
- Average score and average comments
- NumPy stats: mean, median, standard deviation, max, min
- Most active category (by story count)
- Most commented story

Adds two new columns:
- `engagement` — ratio of comments to score
- `is_popular` — boolean flag for above-average score posts

Output: `data/trends_analysed.csv`

---

### Task 4 — Visualization · `task4_visualization.py`

Generates 3 individual charts and a combined dashboard:

| File | Description |
|---|---|
| `chart1_top_stories.png` | Horizontal bar chart — top 10 stories by score |
| `chart2_categories.png` | Bar chart — number of stories per category |
| `chart3_scatter.png` | Scatter plot — score vs comments (popular vs not popular) |
| `dashboard.png` | All 3 charts combined in one figure |

---

## How to Run

Run each task in order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

> After running task 1, update the `file_path` date in `task2_data_processing.py` to match today's date (e.g. `trends_20260405.json`).

---

## Requirements

```bash
pip install requests pandas numpy matplotlib
```

---

## Tech Stack

- **Python** — core language
- **Requests** — HackerNews API calls
- **Pandas** — data cleaning and processing
- **NumPy** — statistical analysis
- **Matplotlib** — chart generation

---

## Author

**Bhanuprakash Yirri**  
[github.com/bhanuprakashyirri](https://github.com/bhanuprakashyirri)
