import streamlit as st
import pandas as pd
import joblib

model = joblib.load("secondhandcar_price_predictio.pkl")

st.title("Second Hand Car Price Prediction")

years = st.selectbox("Years Used", list(range(1, 15)))
km = st.number_input("KM Driven")

rating = st.selectbox("Rating (1-5)", [1,2,3,4,5])
condition = st.selectbox("Condition (1-10)", [1,2,3,4,5,6,7,8,9,10])

on_road_old = st.number_input("On Road Old Price")
on_road_now = st.number_input("On Road Now Price")
hp = st.number_input("Horse Power")
economy = st.number_input("Economy")
top_speed = st.number_input("Top Speed")
torque = st.number_input("Torque")

input_data = pd.DataFrame({
    "years":[years],
    "km":[km],
    "rating":[rating],
    "condition":[condition],
    "on road old":[on_road_old],
    "on road now":[on_road_now],
    "hp":[hp],
    "economy":[economy],
    "top speed":[top_speed],
    "torque":[torque]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")
