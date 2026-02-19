import pandas as pd

# Load datasets
games = pd.read_csv("data/games.csv")
sales = pd.read_csv("data/vgsales.csv")

# Remove duplicates
games.drop_duplicates(inplace=True)
sales.drop_duplicates(inplace=True)

# Handle missing values
games["Rating"].fillna(games["Rating"].mean(), inplace=True)
games["Plays"].fillna(0, inplace=True)
games["Wishlist"].fillna(0, inplace=True)

# Standardize column names
games.columns = games.columns.str.lower().str.replace(" ", "_")
sales.columns = sales.columns.str.lower().str.replace(" ", "_")

# Save cleaned files
games.to_csv("data/games_cleaned.csv", index=False)
sales.to_csv("data/vgsales_cleaned.csv", index=False)

print("✅ Data Cleaning Completed!")
