import streamlit as sl

sl.title("My Mom's New Healthy Diner")

sl.header('Breakfast Favorites')
sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale, Spinach & Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Adding a pick list so customers can pick the fruit to include in smoothie
fruits_selected = sl.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display table on page
sl.dataframe(fruits_to_show)

# New section for fruityvice API response
sl.header('Fruityvice Fruit Advice!')

import requests as req
fruityvice_response = req.get("https://fruityvice.com/api/fruit/watermelon")
sl.text(fruityvice_response.json())

# Normalize JSON info
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Place normalized data into table
sl.dataframe(fruityvice_normalized)
