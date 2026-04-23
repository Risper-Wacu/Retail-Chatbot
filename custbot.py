import streamlit as st

st.title("🛍️ Retail Assistant Chatbot.")
st.write("Welcome! How can i help you today?")

products = {
    "MacBook Air M2": {
        "price": 1100.00,
        "stock": 8,
        "timeline": "3-5 business days",
        "category": "Electronics"
    },
    "Mechanical Keyboard": {
        "price": 120.00,
        "stock": 15,
        "timeline": "2-3 business days",
        "category": "Accessories"
    },
    "Running Shoes": {
        "price": 85.00,
        "stock": 30,
        "timeline": "2-4 business days",
        "category": "Footwear"
    },
    "Coffee Espresso Machine": {
        "price": 450.00,
        "stock": 5,
        "timeline": "5-7 business days",
        "category": "Appliances"
    },
    "Leather Backpack": {
        "price": 75.00,
        "stock": 20,
        "timeline": "3-4 business days",
        "category": "Apparel"
    },
    "Desk Lamp (LED)": {
        "price": 35.00,
        "stock": 50,
        "timeline": "1-2 business days",
        "category": "Furniture"
    }
}
orders = {
    "ORD-9901": "In Warehouse - Preparing for dispatch",
    "ORD-9902": "Shipped - Currently in transit",
    "ORD-9903": "Out for Delivery - Expected by 4:00 PM",
    "ORD-9904": "Delivered - Left at front door",
    "ORD-9905": "Delayed - Held at customs",
    "ORD-9906": "Cancelled - Refund issued"
}
store_info = {
    "Return Policy": "Items can be returned within 30 days. Must be unused and in original packaging.",
    "Shipping Policy": "Flat rate of $10 for orders under $100. Free shipping for orders above $100.",
    "Delivery Timelines": "Standard shipping takes 3-7 days. Express shipping takes 1-2 days.",
    "Warranty": "All electronic items come with a 1-year manufacturer warranty."
}

#The purpose of with is cleanup and management. 
# Without with the code would look repetitive and messy. 
# By using "with", we create a clear "Home" for the navigation menu.
#st.radio allows users to pick exactly one option from a list of choices. 
# It creates a clickable buttons with little circles next to them.
with st.sidebar:
    st.header("Navigation Menu")
    choice = st.radio("Menu", ["Browse Catalog", "Track Order", "Return Policy"])

# Browse Catalog.
if choice == "Browse Catalog":
    st.header("Product Catalog")

#we turn the dictionary keys into a list since when using st.selectbox 
# streamline won't know if you want to show the names(keys) or the details(values).
    item_list = list(products.keys())
    selected_item = st.selectbox("View price for:", item_list)

#Nested dictionary look-up
    price = products[selected_item]["price"]
    time = products[selected_item]["timeline"]

#st.metric() is a specialized streamline toll designed to make numbers look big and bold.
    st.metric(label="price", value=(f'${price}'))
    st.write(f'🚚 Estimated Delivery: {time}')

#2. Track Delivery 
elif choice == "Track Order":
    st.header("Order Tracking")
    orderId_input = st.text_input("Enter your Order ID")
    status = orders.get(orderId_input, "ID not found. Try ORD-9901" )
    st.info(f'Current Status: {status}')

elif choice == "Return Policy":
    st.header("Store Policies")
    st.write("Items can be returned within 30 days. Must be unused and in original packaging.")
    st.write("Flat rate of $10 for orders under $100. Free shipping for orders above $100.")
    st.write("Standard shipping takes 3-7 days. Express shipping takes 1-2 days.")
    st.write("All electronic items come with a 1-year manufacturer warranty.")

