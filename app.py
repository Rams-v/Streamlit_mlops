import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page configuration for a wider layout
st.set_page_config(layout="wide")

st.title("Interactive Data Explorer")
st.subheader("Explore a random dataset")

# Generate some random data
@st.cache_data
def load_data():
    return pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c']
    )

df = load_data()

# Create a sidebar for user input
st.sidebar.header("Controls")

# Sliders for filtering data
x_value = st.sidebar.slider("Select the x-axis variable", 0.0, 1.0, 0.5)
y_value = st.sidebar.slider("Select the y-axis variable", 0.0, 1.0, 0.5)
df_filtered = df[(df['a'] > x_value) & (df['b'] > y_value)]

# Create two columns for the layout
col1, col2 = st.columns(2)

with col1:
    st.write("### Filtered Data Table")
    st.dataframe(df_filtered)

with col2:
    st.write("### Scatter Plot of Filtered Data")
    
    # Use matplotlib to create a scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df_filtered['a'], df_filtered['b'], c='c', cmap='viridis', s=df_filtered['c'] * 100)
    ax.set_xlabel('a > {}'.format(x_value))
    ax.set_ylabel('b > {}'.format(y_value))
    ax.set_title("Scatter Plot")
    st.pyplot(fig)

# Display a bar chart
st.write("### Bar Chart of Column 'c'")
st.bar_chart(df_filtered['c'])