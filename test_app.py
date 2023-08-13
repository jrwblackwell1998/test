import streamlit as st 

# Initialize connection.
conn = st.experimental_connection('snowflake', type='sql')

# Perform query.
df = conn.query('SELECT * from "SAS_PROD_SELF_SERVE"."PRD_SELFSERVE"."SF_HO_DEEPDIVE_20231_JWB" limit 100')

st.write('This is the size of the dataset: ')
st.write(df.shape)

