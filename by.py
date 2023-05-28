import streamlit as st

import PyBypass

# Create a text input field for the link

link = st.text_input("Enter a link:")

# If the user enters a link, try to bypass it

if link:

    try:

        bypassed_link = PyBypass.bypass_link(link)

        st.write("The original URL is:", bypassed_link)

    except Exception as e:

        st.write(e)

