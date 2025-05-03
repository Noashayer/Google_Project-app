import streamlit as st

st.title("🎈 The google app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# Get text input from the user
user_text = st.text_input("Please enter some text:")
def func_len(user_text):
    st.write(len(user_text))
func_len(user_text)

