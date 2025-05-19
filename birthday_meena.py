import streamlit as st
import time

st.set_page_config(page_title="🎉 Birthday Wishes for Meena! 🎂", page_icon="🎈")

# Meena's Date of Birth
meena_dob = "17 October 2009"

# Show Meena's DOB clearly first
st.markdown(f"<h1 style='text-align: center; color: #ff5722;'>Meena's Date of Birth: {meena_dob}</h1>", unsafe_allow_html=True)

# Islamic greeting
st.markdown("<h2 style='text-align: center; color: #4caf50;'>Asalamualikum Wa Rahmatullahi Wa Barakatuh, Meena! 🌙✨</h2>", unsafe_allow_html=True)

# Birthday wish title
st.markdown("<h1 style='text-align: center; color: #e91e63;'>🎉 Happy Birthday, Meena! 🎉</h1>", unsafe_allow_html=True)

st.write("This special wish is from Sharry ❤️")

if st.button("🎂 Click to Start Your Birthday Surprise! 🎉"):
    st.balloons()
    wishes = [
        "✨ May your day sparkle with joy and laughter! 😊",
        "🌟 May your dreams take flight and shine bright! 🌈",
        "💖 You deserve all the love and happiness today and always!",
        "🎉 Happy Birthday, my amazing Meena! 🎈🎊",
        "With endless love from Sharry — your forever friend! ❤️",
    ]
    for wish in wishes:
        st.markdown(f"<h3 style='color: #9c27b0;'>{wish}</h3>", unsafe_allow_html=True)
        time.sleep(2)
        st.empty()
else:
    st.write("Click the button above to get your birthday wish!")

# Birthday cake image
st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80", caption="🎂 Sweet Birthday Cake 🎂")
