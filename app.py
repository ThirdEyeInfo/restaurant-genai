import streamlit as st
from langchain_helper.langchain_util import get_cuisine_for

st.set_page_config(page_title="Restaurant APP", page_icon=":robot:")
st.title("Restaurant APP")

cuisine_type = st.sidebar.selectbox(label="Country Name", options=("Indian", "American", "Mexican", "Italian", "Chinese"))

if cuisine_type:
    response = get_cuisine_for(cuisine_type)

    st.subheader(response["restaurant_name"].strip())

    cuisines = response["menu_items"].strip().split(",")
    st.write("**Menu Items**")
    for cuisine in cuisines:
        st.write(cuisine)