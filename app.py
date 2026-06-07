import streamlit as st
from joblib import load
import pandas as pd

df = pd.read_csv("vgsales.csv")

st.title("Video Game Sales Prediction")
platform = st.selectbox(
    "Platform",
    ['Wii', 'NES', 'GB', 'DS', 'X360', 'PS3', 'PS2', 'SNES', 'GBA', '3DS', 'PS4', 'N64',
     'PS', 'XB', 'PC', '2600', 'PSP', 'XOne', 'GC', 'WiiU', 'GEN', 'DC', 'PSV', 'SAT',
     'SCD', 'WS', 'NG', 'TG16', '3DO', 'GG', 'PCFX']
)

genre = st.selectbox(
    "Genre",
    ['Sports', 'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Misc', 'Shooter',
     'Simulation', 'Action', 'Fighting', 'Adventure', 'Strategy']
)

publisher = st.selectbox(
    "Publisher",
    sorted(df["Publisher"].dropna().unique())
)

year = st.number_input(
    "Release Year",
    min_value=1980,
    max_value=2035
)

model = load("vgsalesmodel.joblib")
columns = load("columns.joblib")

input_data = pd.DataFrame({
    "Platform": [platform],
    "Genre": [genre],
    "Publisher": [publisher],
    "Year": [year]
})
input_data = pd.get_dummies(input_data)
input_data = input_data.reindex(columns=columns, fill_value=0)
prediction = model.predict(input_data)[0]
if prediction == 1:
    st.success("Predicted Successful Game")
else:
    st.error("Predicted Not Successful")