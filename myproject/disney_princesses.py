import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk

from sklearn.ensemble import RandomForestRegressor

header = st.container()
dataset = st.container()
main = st.container()
model_training = st.container()

with header:
    st.title('Disney Princess popularity')
    st.text('In this project I look into the popularity of the Disney princesses through different attributes.')

with dataset:
    st.header('Disney Princess dataset')
    st.text("I found this dataset on Kaggle.com. Creator of the data set Hamna Kaleem. License: CC BY-NC-SA 4.0. " )

    df = pd.read_csv('princess_data.csv')
    st.write(df)

with main:
    st.header('Charts')  

    sales_by_princess = df.groupby(["PrincessName"])["BoxOfficeMillions"].sum()
    st.write(sales_by_princess)

    fig, ax = plt.subplots()
    fig.set_size_inches(15, 10)
    ax.bar(sales_by_princess.index, sales_by_princess.values)
    st.write(fig)

    hair_color_avg_imdb_rating = df.groupby(["HairColor"])["IMDB_Rating"].mean()
    st.write(hair_color_avg_imdb_rating)

    fig, ax = plt.subplots()
    fig.set_size_inches(15, 10)
    ax.bar(hair_color_avg_imdb_rating.index, hair_color_avg_imdb_rating.values)
    st.write(fig)

    year_profit = df.groupby(["FirstMovieYear", "CulturalOrigin", "PrincessName"])["BoxOfficeMillions"].sum().reset_index()
    st.write(year_profit)

    yp_pivot = year_profit.pivot_table(index="FirstMovieYear", columns="CulturalOrigin", values="BoxOfficeMillions")

    yp_pivot

    cultural_origin = df["CulturalOrigin"].unique()
    print(cultural_origin)
    
    sel_origin = st.selectbox(
        "Choose culture: ",
        cultural_origin
    )

    fig, ax = plt.subplots()
    plt.plot(yp_pivot.index, yp_pivot[sel_origin], marker="o", label=sel_origin)
    plt.title("Box Office Millions per cultural by year")
    plt.xlabel("Year")
    plt.ylabel( "Million dollars")
    plt.legend()
    st.pyplot(fig)
  
if 'ratings' not in st.session_state:
    st.session_state.ratings = []

sel_col, display_col = st.columns(2)

rating = sel_col.slider(
    "Do you think this data is relevant for your life?",
    min_value=0, max_value=10, value=5, step=1
)

if sel_col.button("Submit Rating"):
    st.session_state.ratings.append(rating)

if st.session_state.ratings:
    average_rating = round(sum(st.session_state.ratings) / len(st.session_state.ratings), 2)
else:
    average_rating = "No ratings yet."

# Display average rating
display_col.subheader("Average rating:")
display_col.write(average_rating)
display_col.subheader("Ratings given:")
display_col.write(len(st.session_state.ratings))




    

    
    
    

    







