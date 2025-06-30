import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode

# Load CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

st.title('Interactive Table with Streamlit AgGrid')

    # Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file is not None:
        df = load_data(uploaded_file)

        # Create GridOptionsBuilder to customize grid options
gob = GridOptionsBuilder.from_dataframe(df)

        # Configure column filters for all columns
for column in df.columns:
        gob.configure_column(column, filter=True)

        
        
gridOptions = gob.build()

        # Display the table using streamlit-aggrid
AgGrid(df, gridOptions=gridOptions, update_mode=GridUpdateMode.MODEL_CHANGED,width=190,)



