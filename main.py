import streamlit as st

# Define the prices of Bugatti Chiron in various countries (fictional data)
prices = {
    "USA": "$2.5 million",
    "Canada": "$2.7 million",
    "UK": "£2 million",
    "Germany": "€2.2 million",
    "France": "€2.3 million",
    "Australia": "$3 million",
    # Add more countries and prices as needed
}

# Streamlit app title and description
st.title("Bugatti Chiron Price Viewer")
st.write("Select a country to see the price of a Bugatti Chiron:")

# Dropdown to select the country
selected_country = st.selectbox("Select a Country", list(prices.keys()))

# Display the price
st.write(f"The price of a Bugatti Chiron in {selected_country} is {prices[selected_country]}")

# Button to simulate buying
if st.button("Buy Now"):
    st.success(f"Congratulations! You have purchased a Bugatti Chiron in {selected_country}. 🚗💨")
