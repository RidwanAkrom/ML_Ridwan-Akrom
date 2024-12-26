
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit Title
st.title("Case Study Machine Learning GDGoC Sriwijaya University 2024/2025")

st.write("Ridwan Akrom")
st.write("Sistem Komputer")

# Data Wrangling
st.subheader("1.Data Wrangling")
st.subheader("Dataset yang Digunakan")
st.write("Dataset yang digunakan dalam kasus ini adalah StudentPerformanceFactors.csv")
df = pd.read_csv("StudentPerformanceFactors.csv")
st.write(df)

# Code extracted from the Jupyter Notebook
# Adapt the core functionality here

# Example placeholder for visualizations and analysis
st.subheader("Analysis and Visualizations")
st.write("Implement your plots and logic here.")
