import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel File
df = pd.read_excel("Mobile_Phone_Data.xlsx")
print("\nInitial Data:")
print(df.head())

# -------------------- DATA CLEANING --------------------

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Rename columns to lowercase
df.columns = df.columns.str.strip().str.lower()

# 4. Ensure price is integer
df['price'] = df['price'].astype(int)

# -------------------- DATA ANALYSIS --------------------

# 1. Average price
avg_price = df['price'].mean()
print("\nAverage Price:", avg_price)

# 2. Max rating
max_rating = df['rating'].max()
print("Max Rating:", max_rating)

# 3. Group by brand - average price
brand_avg_price = df.groupby('brand')['price'].mean()
print("\nAverage Price by Brand:")
print(brand_avg_price)

# 4. Value counts of brands
brand_counts = df['brand'].value_counts()
print("\nBrand Counts:")
print(brand_counts)

# 5. Filter: Phones above 20000
high_price_phones = df[df['price'] > 20000]
print("\nPhones above 20000:")
print(high_price_phones.head())

# 6. Sort by price descending
sorted_df = df.sort_values(by='price', ascending=False)
print("\nTop 5 Expensive Phones:")
print(sorted_df.head())

# -------------------- DATA VISUALIZATION --------------------

# 1. Bar Chart - Brand Counts
plt.figure(figsize=(8,5))
brand_counts.plot(kind='bar', color='skyblue')
plt.title("Number of Phones by Brand")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.savefig("brand_counts.png")
plt.show()

# 2. Pie Chart - Ratings
plt.figure(figsize=(6,6))
df['rating'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Phone Ratings Distribution")
plt.savefig("ratings_pie.png")
plt.show()

# 3. Scatter Plot - Price vs Battery
plt.figure(figsize=(8,5))
sns.scatterplot(x='price', y='battery(mah)', data=df, hue='brand')
plt.title("Price vs Battery Capacity")
plt.savefig("price_vs_battery.png")
plt.show()

# -------------------- EXPORT CLEANED DATA --------------------
df.to_excel("cleaned_mobile_phone_data.xlsx", index=False)
print("\nCleaned data exported to 'cleaned_mobile_phone_data.xlsx'")
