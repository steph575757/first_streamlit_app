import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit');

streamlit.title('My parents New Healthy Diner');

streamlit.header('Breakfast Favorites');

streamlit.text('🥣 Omega 3 and Blueberry Oatmeal');
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie');
streamlit.text('🐔 Hard-Boiled Free-Range Egg');
streamlit.text('🥑 🍞 Advocado Toast');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries']);
streamlit.dataframe(my_fruit_list)
