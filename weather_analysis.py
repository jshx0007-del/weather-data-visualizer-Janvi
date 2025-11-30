#---------------------------------------------------
# Data Analysis and Visualization with Real-World Weather Data
# Name: Janvi Sehrawat 
#Roll no :2501350002
#----------------------------------------------------

import pandas as pd
import numpy as np
import csv

dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
np.random.seed(42)

df = pd.DataFrame({
    "Date": dates,
    "Temperature": np.random.uniform(10, 40, len(dates)),
    "Rainfall": np.random.uniform(0, 50, len(dates)),
    "Humidity": np.random.uniform(20, 100, len(dates))
})

with open("weather_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(df.columns)
    for row in df.values:
        writer.writerow(row)


df_loaded = pd.read_csv("weather_data.csv")

print("\n=== HEAD ===\n", df_loaded.head())
print("\n=== INFO ===")
df_loaded.info()
print("\n=== DESCRIBE ===\n", df_loaded.describe().T)


df_loaded["Date"] = pd.to_datetime(df_loaded["Date"])
df_clean = df_loaded.dropna()


df_clean = df_clean[["Date", "Temperature", "Rainfall", "Humidity"]]

with open("weather_data_cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(df_clean.columns)
    for row in df_clean.values:
        writer.writerow(row)


temp = df_clean["Temperature"].values

print("\n=== DAILY TEMPERATURE STATS ===")
print("Mean:", np.mean(temp))
print("Min:", np.min(temp))
print("Max:", np.max(temp))
print("Std Dev:", np.std(temp))

monthly_stats = df_clean.resample("M", on="Date").mean()

print("\n=== MONTHLY STATS ===\n", monthly_stats)
yearly_stats = df_clean.resample("Y", on="Date").mean()

print("\n=== YEARLY STATS ===\n", yearly_stats)


print("\n=== TEXT VISUALIZATION ===")

print("\nTemperature (first 10 days):")
print(df_clean["Temperature"].head(10).to_string(index=False))

print("\nMonthly Rainfall Totals:")
print(df_clean.resample("M", on="Date")["Rainfall"].sum())

print("\nHumidity vs Temperature (sample 10 rows):")
print(df_clean[["Temperature", "Humidity"]].head(10))



monthly_group = df_clean.groupby(df_clean["Date"].dt.month).mean()

season_map = {
    1:"Winter", 2:"Winter",
    3:"Summer", 4:"Summer", 5:"Summer",
    6:"Monsoon", 7:"Monsoon", 8:"Monsoon",
    9:"Post-Monsoon", 10:"Post-Monsoon",
    11:"Winter", 12:"Winter"
}

df_clean["Season"] = df_clean["Date"].dt.month.map(season_map)

seasonal_group = df_clean.groupby("Season").mean()

monthly_group.to_csv("monthly_stats.csv")
seasonal_group.to_csv("seasonal_stats.csv")

report = """
# WEATHER DATA ANALYSIS REPORT

## Summary
All tasks completed using pandas, numpy, and csv modules only.

## Completed Items
- Loaded weather_data.csv
- Cleaned missing values
- Converted date column
- Calculated daily, monthly, and yearly statistics
- Grouped by month and seasons
- All CSV outputs exported
- Visual summaries printed without using Matplotlib

"""

with open("weather_report.md", "w") as f:
    f.write(report)

print("\n✔ All tasks successfully completed!")