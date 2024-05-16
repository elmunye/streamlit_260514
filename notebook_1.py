import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Hello, world!")

#include header in the app
st.header("My first app")

#include a subtitle in the app
st.title("NBA Playoffs hightlights:")

#include a text in the app
st.write("The Denver Nuggets made an impressive come back against the Minnesota Timberwolves in the NBA playoffs.")

#include a youtube video in the app
st.video("https://www.youtube.com/watch?v=BUVMqMsgVqU")

#include a sidebarr in the app
st.sidebar.header("NBA Playoffs")

#include a radio button in sidebar with two images
radio = st.sidebar.radio(
    "Who will win the NBA playoffs?",
    ('Minnesota Timberwolves', 'Denver Nuggets'))

if radio == 'Minnesota Timberwolves':
    st.image("/Users/elyas/PycharmProjects/streamlit_260514/.idea/image2.jpeg")
else:
    st.image("/Users/elyas/PycharmProjects/streamlit_260514/.idea/image1.jpeg")

#create a UI for users to upload a csv file
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

#create bar plot for the variable Day of the week and make sure that the days of the week are organized from Monday to Sunday and note that the category levels are titled Monday to Sunday
data['Day of the week'] = pd.Categorical(data['Day of the week'], categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ordered=True)
st.bar_chart(data['Day of the week'].value_counts())

#create a bar plot for the variable NIBRS Code Name make the bar plot verticle
plt.figure(figsize=(10,5))
data['NIBRS Code Name'].value_counts().plot(kind='bar')
st.pyplot()

