import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# COUNTRY-WISE NETFLIX CONTENT ANALYSIS
# ==========================================

# File paths
INPUT_FILE = "Dataset.csv"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Load dataset
df = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("COUNTRY-WISE NETFLIX CONTENT ANALYSIS")
print("=" * 50)

print("\nDataset shape:", df.shape)
print("\nFirst five records:")
print(df.head())

# 2. Clean country information
df_country = df.dropna(subset=["country"]).copy()

df_country["country"] = (
    df_country["country"]
    .astype(str)
    .str.split(",")
)

# Each country gets a separate record
df_country = df_country.explode("country")

df_country["country"] = df_country["country"].str.strip()

df_country = df_country[df_country["country"] != ""]

# 3. Calculate content count by country
country_counts = (
    df_country.groupby("country")
    .size()
    .sort_values(ascending=False)
)

country_report = country_counts.reset_index()
country_report.columns = ["Country", "Content_Count"]

country_report.to_csv(
    os.path.join(OUTPUT_DIR, "content_by_country.csv"),
    index=False
)

print("\nTop 10 Countries by Netflix Content:")
print(country_report.head(10).to_string(index=False))

# 4. Identify top 15 countries
top_countries = country_counts.head(15).sort_values()

plt.figure(figsize=(12, 7))
top_countries.plot(kind="barh")

plt.title("Top 15 Countries by Netflix Content")
plt.xlabel("Number of Title-Country Records")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "top_15_countries.png"),
    dpi=300
)
plt.show()

# 5. Analyze Movies and TV Shows by country
country_type = (
    df_country.groupby(["country", "type"])
    .size()
    .unstack(fill_value=0)
)

country_type.to_csv(
    os.path.join(OUTPUT_DIR, "content_by_country_and_type.csv")
)

print("\nContent Type by Country:")
print(country_type.head(10))

# 6. Compare Movies and TV Shows
type_counts = df["type"].value_counts()

print("\nOverall Content Type Distribution:")
print(type_counts)

plt.figure(figsize=(8, 5))
type_counts.plot(kind="bar")

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "content_type.png"),
    dpi=300
)
plt.show()

# 7. Generate summary report
summary = pd.DataFrame({
    "Metric": [
        "Total Dataset Records",
        "Records with Country Information",
        "Number of Countries",
        "Total Title-Country Records",
        "Total Movies",
        "Total TV Shows"
    ],
    "Value": [
        len(df),
        int(df["country"].notna().sum()),
        df_country["country"].nunique(),
        len(df_country),
        int((df["type"] == "Movie").sum()),
        int((df["type"] == "TV Show").sum())
    ]
})

summary.to_csv(
    os.path.join(OUTPUT_DIR, "summary.csv"),
    index=False
)

print("\nProject Summary:")
print(summary.to_string(index=False))

print("\nAnalysis completed successfully!")
print("Check the 'outputs' folder for charts and CSV reports.")
