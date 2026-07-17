import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.figure(figsize=(15,6))

sns.barplot(x="State", y="Temperature", data=df)

plt.xticks(rotation=90)
plt.title("Temperature of Indian State Capitals")
plt.xlabel("State")
plt.ylabel("Temperature (°C)")

plt.show()
plt.figure(figsize=(15,6))

sns.barplot(x="State", y="Humidity", data=df)

plt.xticks(rotation=90)
plt.title("Humidity of Indian State Capitals")
plt.xlabel("State")
plt.ylabel("Humidity (%)")

plt.show()
plt.figure(figsize=(15,6))

sns.barplot(x="State", y="Wind_Speed", data=df)

plt.xticks(rotation=90)
plt.title("Wind Speed of Indian State Capitals")
plt.xlabel("State")
plt.ylabel("Wind Speed (m/s)")

plt.show()

top10 = df.head(10)

plt.figure(figsize=(8,8))

plt.pie(top10["Clouds"],
        labels=top10["State"],
        autopct='%1.1f%%')

plt.title("Cloud Coverage (Top 10 States)")

plt.show()
plt.figure(figsize=(8,6))

sns.scatterplot(
    x="Temperature",
    y="Humidity",
    data=df,
    s=120
)

plt.title("Temperature vs Humidity")

plt.show()
plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include='number')

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.title("Weather Data Correlation")

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("india_weather_data.csv")

plt.figure(figsize=(15,6))

plt.plot(df["State"], df["Pressure"], marker='o')

plt.xticks(rotation=90)
plt.title("Atmospheric Pressure")
plt.xlabel("State")
plt.ylabel("Pressure (hPa)")

plt.show()