import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "what is streamlit ?"}
    ]
)

st.write(completion.choices[0].message.content)

conn = st.experimental_connection("snowpark")
df = conn.query("select current_warehouse()")
st.write(df)
