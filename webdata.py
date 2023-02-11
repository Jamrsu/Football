# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import csv

# read a CSV file inside the 'data" folder next to 'app.py'
df = pd.read_csv("All Leagues 2023-02-11.csv")
# df = pd.read_excel(...)  # will work for Excel files

st.title("Football Probabilities")  # add a title
st.write(df)  # visualize my dataframe in the Streamlit app


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


csv = convert_df(df)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='probabilities.csv',
    mime='text/csv',
)

# leagues = df['League'].unique()

# league = st.selectbox('Filter League', leagues)
# df[df['League'] == league]
