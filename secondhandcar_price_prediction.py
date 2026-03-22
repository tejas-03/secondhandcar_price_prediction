import streamlit as st
import pandas as pd
import joblib
import os

# Show files for debugging
st.write("Files in directory:", os.listdir())

# Load model
model = joblib.load("secondhandcar_price_predictio.pkl")

st.title("Second Hand Car Price Prediction")

on_road_old = st.number_input("On Road Old Price")
on_road_now = st.number_input("On Road Now Price")
years = st.number_input("Years Used")
km = st.number_input("KM Driven")
rating = st.selectbox("Rating (1-5)", [1,2,3,4,5])
condition = st.selectbox("Condition (1-10)", [1,2,3,4,5,6,7,8,9,10])
economy = st.number_input("Economy")
top_speed = st.number_input("Top Speed")
hp = st.number_input("Horse Power")
torque = st.number_input("Torque")

input_data = pd.DataFrame({
    'on road old':[on_road_old],
    'on road now':[on_road_now],
    'years':[years],
    'km':[km],
    'rating':[rating],
    'condition':[condition],
    'economy':[economy],
    'top speed':[top_speed],
    'hp':[hp],
    'torque':[torque]
})

input_data = input_data.reindex(columns=model.feature_names_in_)

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")
