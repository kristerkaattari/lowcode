import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk

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
        "Valitse kulttuuri: ",
        cultural_origin
    )

  
    fig, ax = plt.subplots()
    plt.plot(yp_pivot.index, yp_pivot[sel_origin], marker="o", label=sel_origin)

    st.pyplot(fig)
    
    

    







