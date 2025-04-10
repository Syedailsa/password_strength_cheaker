# import json
# try:
#     from streamlit_lottie import st_lottie
#     lottie_available = True
# except ImportError:
#     lottie_available = False

import streamlit as st
import re
import random

# Guide

with st.container():
    st.title("🔐 Password Guardian")
    st.subheader("Stronger Passwords, Safer You!")
st.markdown("""
✨ **What It Does:**   
🔍 Checks Strength of your passwords (Weak/Moderate/Strong)  
⚡ Generates Secure 10-character passwords instantly  
📊 Analyzes 4 key security factors  

🛠️ **How To Use:**  
1. Type any password in the input box below  
2. Get instant strength feedback  
3. Copy auto-generated secure passwords  
""")

#password generator

numb = ["0","1","2","3","4","5","6","7","8","9"]
Upper_case = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Lower_case = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

password_created = []

password_created += random.sample(numb, 2)
password_created += random.sample(Upper_case, 2)
password_created += random.sample(Lower_case, 2)
password_created += random.sample(symbols, 2)

# add random characters to make it 10 char
remaining_chars = random.choices(numb + Upper_case + Lower_case + symbols, k=10 - len(password_created))
password_created += remaining_chars

random.shuffle(password_created)

suggested_password = ''.join(password_created)

#password strength cheaker

def pasword_strength_cheaker(password):

    score = 0

    #length 

    if len(password) >= 8:
        score += 1
    else:
        st.warning("❌ Password should be at least 8 characters long.")

    #uppercase and lowercase

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.warning("❌ Password should contain both uppercase and lowercase letters.")

    #numbers

    if re.search(r"\d", password): #\d means numbers from 0-9
        score += 1
    else:
       st.warning("❌ Password should be at least one number from (0-9).") 

    #special letters

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.warning("❌ Password should contain be at least one special character (ex: &,# etc).")


    #score rate

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
        st.write(f"Suggested password: {suggested_password}")
        if st.button ("Copy Suggested Password"):
            st.text_area("Suggested Password", suggested_password, height=68)
            st.info("click on the suggested password above to copy")
    else:
        st.warning("❌ Weak Password!")
        st.write(f"Suggested password: {suggested_password}")
        if st.button ("Copy Suggested Password"):
            st.text_area("Suggested Password", suggested_password, height=68)
            st.info("click on the suggested password above to copy")

# streamlit app

st.title("Try it out !")


User_password = st.text_input("Enter a strong password: ")

if User_password:
    pasword_strength_cheaker(User_password)


st.write("-" * 20)
st.caption("Developed with ❤️ by Ilsa Ubaid | Keep your accounts secure!")

# Lottie animation with Json file ( "not working on deployment :(" )

# def load_lottie_file(filepath: str):
#     try:    
#         with open(filepath, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         st.error("lottie file path not found")
#         return None
    
# lottie_file = load_lottie_file("password-anim.json")

# if lottie_file:
#     st_lottie(
#         lottie_file,
#         reverse = False,
#         key="password cheaker",
#         loop = True,
#         height = None,
#         width = None
#     )

