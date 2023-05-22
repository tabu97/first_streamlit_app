import streamlit
streamlit.title('My Parents new Healthy Diner')
streamlit.header('BreakFast Meau')
streamlit.text(' 🥣 Omega 3 and blueberry oatmeal')
streamlit.text(' 🥗 Kale, Spinach and Rocket smoothie')
streamlit.text(' 🐔 Hard-bolied, free range egg')
streamlit.text('🥑🍞 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas as pd
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
