import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "American", "Arabic"))



if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    
    st.header(response['restaurant_name'].strip())
    menu_items_str = response['menu_items']
    menu_items = [item.strip() for item in menu_items_str.split(",")]
    st.write("**Menu Items**")

    for item in menu_items:
        st.write(item)
