import streamlit as st
import pandas as pd


# Title
st.title("Simple Data Dashboard")

# File Uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show Data Preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Show Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # Fixing typo in "columns" and improving column selection
    st.subheader("Filter Data")
    columns = df.columns.tolist()  # Fixing "colums" typo
    selected_column = st.selectbox("Select column to filter by", columns)

    unique_values = df[selected_column].unique()  # Fixed incorrect syntax
    selected_value = st.selectbox("Select value", unique_values)

    # Filtering Data
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plot Data
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        plt.figure(figsize=(10, 5))
        plt.plot(filtered_df[x_column], filtered_df[y_column], marker="o", linestyle="-")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{y_column} vs {x_column}")
        st.pyplot(plt)
    else:
        st.write("Waiting on file upload...")

