import streamlit as st
from google import genai

st.markdown(
    """
    <h1 style= 'text-align: center;'> My Personal AI Assistant </h1>
    <p style= 'text-align: center; font-size:28px;'>
        Qunch your curiosity
    </p>
    """,
    unsafe_allow_html = True,
)



api_key = st.secrets["GOOGLE_API_KEY"]
robo = genai.Client(api_key=api_key)

mychat = robo.chats.create(model="gemini-3.1-flash-lite")

response_placeholder = st.empty()

question = st.text_input("Ask me something : ")

col1, col2, col3 = st.columns([4,1,4])

with col2 :
    send = st.button("Send")
    
if send:
    response = mychat.send_message(question)
    response_placeholder.write(response.text)
