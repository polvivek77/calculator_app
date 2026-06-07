import streamlit as st

st.title("Calculator")

num1 = st.number_input("Number 1")
num2 = st.number_input("Number 2" )

if st.button("Add"):
    st.success(f"Result = {num1 + num2}")