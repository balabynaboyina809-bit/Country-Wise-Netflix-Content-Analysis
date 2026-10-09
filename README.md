# Country-Wise-Netflix-Content-Analysis
Analyze Netflix content availability across different countries.

## Project overview
This project analyzes Netflix titles by country using the provided CSV dataset. It cleans country names, handles titles associated with multiple countries, ranks countries by title-country records, compares Movies and TV Shows, and exports charts and CSV summaries.

## Files
- `netflix_country_analysis.py` — analysis script.
- `Dataset.csv` — input dataset supplied for this project.
- `outputs/content_by_country.csv` — title-country record count for each country.
- `outputs/content_by_country_and_type.csv` — counts by country and content type.
- `outputs/summary.csv` — high-level dataset summary.
- `outputs/top_15_countries.png` — bar chart of the 15 countries with the most records.
- `outputs/content_type.png` — chart of Movies vs TV Shows in country-tagged records.

## Requirements
Python 3.9+ recommended, plus:
```bash
pip install pandas matplotlib
```

## Run
Place the CSV in the same directory as the Python script, then run:
```bash
python netflix_country_analysis.py --input "Dataset(1).csv" --output-dir outputs
```

## Method
1. Load the CSV with pandas.
2. Exclude records with missing country information from country-level comparisons.
3. Split comma-separated country values and explode them so each country receives a record for a title.
4. Group and rank countries, then export CSV tables and charts.

## Interpretation note
A title associated with multiple countries contributes one record to each listed country. Therefore, country counts are **title-country records**, not unique global title counts, and their sum can exceed the number of dataset rows. Missing country values are omitted from country comparisons.
