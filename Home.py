#Company Dashboard with Streamlit
#© 2023 Tushar Aggarwal. All rights reserved. 
#https://github.com/tushar2704/

#Importing the required Libraries

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
#from query import *
import time



#Page config
#Page setups
#Application Title and Page Structure
#page config
st.set_page_config(page_title="Company Dashboard 🏢",
                   page_icon=":🏢:",
                   layout='wide')
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


#Page Title 
st.title("Company Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

st.markdown("Welcome to the Company Dashboard with Streamlit app! This project aims to provide an easy-to-use interface for users to gain insights into sales trends, product performance, and customer behavior.")
st.markdown("""[Tushar-Aggarwal.com](https://tushar-aggarwal.com/)""")























































































































































































