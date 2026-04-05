# TrendPulse

A data pipeline that fetches trending posts from HackerNews, processes and analyzes the data, and generates visual insights.

---

## Project Structure

```
TrendPulse/
├── fetch.py          # Fetches top posts from HackerNews API
├── process.py        # Cleans and formats raw data
├── analysis.py       # Runs statistical analysis
├── visualize.py      # Generates charts and graphs
└── data/
    ├── raw.json      # Raw API output
    └── clean.csv     # Cleaned, processed data
```

---

## Pipeline Overview

### 1. Fetch Data — `fetch.py`
Connects to the HackerNews API and retrieves the current top posts, saving the raw response to `data/raw.json`.

### 2. Process Data — `process.py`
Cleans the raw data by removing null entries and standardizing date formats, then saves the result to `data/clean.csv`.

### 3. Analysis — `analysis.py`
Reads the cleaned data and outputs:
- **Top 5 posts** by points
- **Average points** across all posts
- **Top authors** by post performance

### 4. Visualization — `visualize.py`
Generates the following charts saved as image files:
- `top_posts.png` — Bar chart of the highest-scoring posts
- `authors.png` — Chart of the most active/top-performing authors

---

## How to Run

Run each step in order:

```bash
python fetch.py
python process.py
python analysis.py
python visualize.py
```

---

## Requirements

Install dependencies before running:

```bash
pip install -r requirements.txt
```

---

## Output

| File | Description |
|---|---|
| `data/raw.json` | Raw HackerNews API data |
| `data/clean.csv` | Cleaned and formatted data |
| `top_posts.png` | Visualization of top posts by points |
| `authors.png` | Visualization of top authors |
