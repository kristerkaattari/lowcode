import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Disney Princess popularity')
    st.text('In this project I look into the popularity of the Disney princesses through different attributes.')

with dataset:
    st.header('Disney Princess dataset')
    st.text("I found this dataset on Kaggle.com. Creator of the data set Hamna Kaleem. License: CC BY-NC-SA 4.0. " )

with features:
    st.header('The features I created')

with model_training:
    st.header('Time to train the model!')




