import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "image.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

st.title("Dashboard - Tips Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Day = st.selectbox("Select the Day:", df['day'].unique())
Time = st.selectbox("Select the Time:", df['time'].unique())
Size = st.selectbox("Select the Size:", df['size'].unique())
Sex = st.selectbox("Select the Sex:", df['sex'].unique())


col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['total_bill'] == total_bill], x="Total Bill")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['total_bill'] == total_bill], y="Total Bill")
col2.plotly_chart(fig_2, use_container_width=True)

coll1, coll2 = st.columns(2)

figg_1 = px.histogram(df[df['tip'] == tip], x="Total Bill")
col1.plotly_chart(fig_1, use_container_width=True)

figg_2 = px.box(df[df['tip'] == tip], y="Tip")
col2.plotly_chart(fig_2, use_container_width=True)