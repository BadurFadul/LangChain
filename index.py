import streamlit as st
from langchain.llms import OpenAI
import os
from apikey import apikey

st.title('🦜🔗 A quick app')

os.environ['OPENAI_API_KEY'] = apikey

def generate_response(input_text):
  llm = OpenAI(temperature=0.9, openai_api_key=os.environ['OPENAI_API_KEY'])
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')

  if not os.environ['OPENAI_API_KEY'].startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  
  if submitted and os.environ['OPENAI_API_KEY'].startswith('sk-'):
    generate_response(text)