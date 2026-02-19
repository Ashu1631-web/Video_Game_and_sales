import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("data/merged_games_sales.csv")

st.title("🎮 Video Game Sales & Engagement Dashboard")

# KPI Metrics
st.metric("Total Games", df.shape[0])
st.metric("Total Global Sales", round(df["global_sales"].sum(), 2))

# Top Genres
st.subheader("Top Selling Genres")
genre_sales = df.groupby("genre")["global_sales"].sum().sort_values(ascending=False)

st.bar_chart(genre_sales.head(10))

# Rating vs Sales Scatter
st.subheader("Rating vs Global Sales")
plt.scatter(df["rating"], df["global_sales"])
st.pyplot(plt)
