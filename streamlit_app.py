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
sl.multiselect("Pick some Fruits:", list(my_fruit_list.index), ['Avacodo','Strawberries'])

# Display table on page
sl.dataframe(my_fruit_list)


