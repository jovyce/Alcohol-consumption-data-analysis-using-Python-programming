import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('drinks.csv')
df.head()
df.isna().sum()
df.columns = df.columns.str.lower().str.replace(" ", "_")
consumption = df.sort_values("total_litres_of_pure_alcohol", ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.barh(consumption["country"], consumption["total_litres_of_pure_alcohol"], color="gold")
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Countries by total consumption")
plt.ylabel("Total consumption")
plt.grid(axis="y")
plt.show()
