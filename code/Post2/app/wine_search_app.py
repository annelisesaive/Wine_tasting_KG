import pandas as pd
import streamlit as st

# Load the "interesting wines" dataset
csv_file = "./code/Post2/app/concise_interesting_wines.csv"
wine_data = pd.read_csv(csv_file)

# Title of the app
st.markdown("""
            # Welcome to QUALITYSIP 🍷
            ## Discover The Best Wines That Match Your Budget
            """)

# Add the logo of the app
image_path = './code/Post2/app/QualitySip_logo.png'  # Ensure the image is in the same directory
st.image(image_path, caption=None, use_column_width=True)

# App explanation & functionalities
st.markdown("""
---
QualitySip is your personalized wine discovery tool! Whether you're a casual drinker or a wine connoisseur, 
our app helps you find the best wines that offer great value for money. 

The wines featured here have been selected because they stand out for offering exceptional quality for their price, 
based on ratings and reviews from expert tasters at **WineEnthusiast**. 
Along with each wine's rating, you'll also find an expert description to help guide your choice.

You can search by ***price, country, variety, & region*** to find the perfect bottle. 
Enjoy the journey of discovering new wines tailored to your taste and budget!

---

""")

# Search Criteria: Price Range
price_range = st.slider('Select Price Range', min_value=float(wine_data['price'].min()), max_value=float(wine_data['price'].max()), value=(0.0, 50.0))

# Filter the data based on price range first
filtered_data = wine_data[
    (wine_data['price'] >= price_range[0]) & 
    (wine_data['price'] <= price_range[1])
]

# Dynamic Search Criteria: Country (multi-select for multiple countries)
countries = st.multiselect('Select Country', options=filtered_data['country'].unique(), default=None)

# Update filtered_data based on selected countries (if any are selected)
if countries:
    filtered_data = filtered_data[filtered_data['country'].isin(countries)]

# Dynamic Search Criteria: Variety (multi-select for multiple varieties)
varieties = st.multiselect('Select Variety', options=filtered_data['variety'].unique(), default=None)

# Update filtered_data based on selected varieties (if any are selected)
if varieties:
    filtered_data = filtered_data[filtered_data['variety'].isin(varieties)]

# Dynamic Search Criteria: Province (multi-select for multiple provinces)
provinces = st.multiselect('Select Province', options=filtered_data['province'].unique(), default=None)

# Update filtered_data based on selected provinces (if any are selected)
if provinces:
    filtered_data = filtered_data[filtered_data['province'].isin(provinces)]

# Display filtered results
st.write(f"Found {filtered_data.shape[0]} wines:")
st.dataframe(filtered_data)

# Option to download the filtered results
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(filtered_data)

st.download_button(
    label="Download results as CSV",
    data=csv,
    file_name='filtered_wines.csv',
    mime='text/csv',
)
