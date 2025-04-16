import streamlit as st
import random
import string


def password_generator(length , use_digit , use_special_char):
    character = string.ascii_letters

    if use_digit:
        character += string.digits #numbers from 0 to 9

    if use_special_char:
        character += string.punctuation #special characters like !@#$%^&*()

    return  ''.join(random.choice(character) for _i in range(length))


st.title("Password Generator")

length  = st.slider("Password Length", min_value=4, max_value=30 , value=12) 

use_digit = st.checkbox("Include Digit")
use_special_char = st.checkbox  ("Include Special Character")

if st.button("Generate Password"):
    password = password_generator(length , use_digit , use_special_char)
    st.write(f"Password: {password}")

st.title("--------------------------------------------")

st.write("Build with ❤ by [Muhammad Emad Hassan](https://www.linkedin.com/in/muhammad-emad-hassan)")
