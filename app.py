import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.title(" Mobile Phone Data Analysis")


df = pd.read_excel("Mobile_Phone_Data.xlsx")
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Cleaning 
df = df.drop_duplicates()           
df.columns = df.columns.str.strip().str.lower()
df['price'] = df['price'].astype(int)

# metrics
st.subheader("Data Analysis Results")
st.text(f"Average Price: {df['price'].mean():.2f}")
st.text(f"Max Rating: {df['rating'].max()}")

st.write("Average Price by Brand:")
st.dataframe(df.groupby('brand')['price'].mean())
st.write("Brand Counts:")
st.dataframe(df['brand'].value_counts())


st.subheader("Charts")

# brand count (bar) 
st.write(" Number of Phones by Brand")
fig1, ax1 = plt.subplots()
df['brand'].value_counts().plot(kind='bar', color='skyblue', ax=ax1)
st.pyplot(fig1)

# rating (pie) 
st.write(" Ratings Distribution")
fig2, ax2 = plt.subplots()
df['rating'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax2)
st.pyplot(fig2)

# Price vs battery (scatter)
st.write(" Price vs Battery Capacity")
fig3, ax3 = plt.subplots()
sns.scatterplot(x='price', y='battery(mah)', data=df, hue='brand', ax=ax3)
st.pyplot(fig3)
