import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("products.csv")

# Clean price column
df['Price'] = df['Price'].str.replace('Â£', '').astype(float)

# Bar Chart: Number of books by rating
rating_count = df['Rating'].value_counts()

plt.figure()
plt.bar(rating_count.index, rating_count.values)
plt.title("Number of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Bar Chart: Average price by rating
avg_price = df.groupby('Rating')['Price'].mean()

plt.figure()
plt.bar(avg_price.index, avg_price.values)
plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.show()

# Histogram: Price distribution
plt.figure()
plt.hist(df['Price'])
plt.title("Price Distribution of Books")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.show()

