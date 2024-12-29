import streamlit as st
import pandas as pd
import io
import numpy as np

st.title("Streamlit CSV Download Example")

# Sample Data Generation (can be replaced with your actual data processing)
@st.cache_data # Cache the data for better performance
def generate_data(num_rows=1000):
    data = {'col1': np.random.rand(num_rows), 'col2': np.random.randint(0, 100, num_rows)}
    return pd.DataFrame(data)

df = generate_data()

# Download Button
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='my_data.csv',
    mime='text/csv',
)

# Large Data Download Example
large_df = generate_data(100000)

if st.button("Download Large CSV"):
    csv_buffer = io.StringIO()
    large_df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="Download Large Data as CSV",
        data=csv_buffer.getvalue().encode('utf-8'),
        file_name='large_data.csv',
        mime='text/csv'
    )

if st.button("Download Large CSV as byte buffer"):
    csv_buffer = io.BytesIO()
    large_df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="Download Large Data as CSV with byte buffer",
        data=csv_buffer.getvalue(), # no need to encode as it is already in bytes
        file_name='large_data_byte.csv',
        mime='text/csv'
    )
