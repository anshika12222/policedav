import streamlit as st
import pandas as pd

st.title("Population of Indian States")

df = pd.read_csv("census2011.csv")

selected_states = st.multiselect("Select State(s)", df["State"].unique())
state_df = df[df["State"].isin(selected_states)] 
selected_cities = st.multiselect("Select District(s)", state_df["District"].unique())
final_df = state_df[state_df["District"].isin(selected_cities)]

st.subheader(f"Population Data of {', '.join(selected_cities)} india {', '.join(selected_states)}")
st.dataframe(final_df)
