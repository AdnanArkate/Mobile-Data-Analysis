import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel("Mobile_Phone_Data.xlsx")
print("\nInitial Data:")
print(df.head())

# Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

# columns in lowercase
df.columns = df.columns.str.strip().str.lower()

# price to int
df['price'] = df['price'].astype(int)

avg_price = df['price'].mean()
print("\nAverage Price:", avg_price)

max_rating = df['rating'].max()
print("Max Rating:", max_rating)

brand_avg_price = df.groupby('brand')['price'].mean()
print("\nAverage Price by Brand:")
print(brand_avg_price)

brand_counts = df['brand'].value_counts()
print("\nBrand Counts:")
print(brand_counts)

# filters
high_price_phones = df[df['price'] > 20000]
print("\nPhones above 20000:")
print(high_price_phones.head())

sorted_df = df.sort_values(by='price', ascending=False)
print("\nTop 5 Expensive Phones:")
print(sorted_df.head())

# bar chart
plt.figure(figsize=(8,5))
brand_counts.plot(kind='bar', color='skyblue')
plt.title("Number of Phones by Brand")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.savefig("brand_counts.png")
plt.show()

# pie chart
plt.figure(figsize=(6,6))
df['rating'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Phone Ratings Distribution")
plt.savefig("ratings_pie.png")
plt.show()

# scatter chart 
plt.figure(figsize=(8,5))
sns.scatterplot(x='price', y='battery(mah)', data=df, hue='brand')
plt.title("Price vs Battery Capacity")
plt.savefig("price_vs_battery.png")
plt.show()

# export data
df.to_excel("cleaned_mobile_phone_data.xlsx", index=False)
print("\nCleaned data exported to 'cleaned_mobile_phone_data.xlsx'")
