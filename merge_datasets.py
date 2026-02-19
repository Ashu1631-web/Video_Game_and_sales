import pandas as pd

games = pd.read_csv("data/games_cleaned.csv")
sales = pd.read_csv("data/vgsales_cleaned.csv")

# Merge on game title/name
merged = pd.merge(
    games,
    sales,
    left_on="title",
    right_on="name",
    how="inner"
)

merged.to_csv("data/merged_games_sales.csv", index=False)

print("✅ Merged Dataset Saved Successfully!")
