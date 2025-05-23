import streamlit as st
import time

st.set_page_config(page_title="🎉 Birthday Wishes for Meena! 🎂", page_icon="🎈")

meena_dob = "17 October 2009"

st.markdown(f"<h1 style='text-align: center; color: #ff5722;'> {meena_dob}</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #4caf50;'>Asalamualikum Wa Rahmatullahi Wa Barakatuh, Meena! 🌙✨</h2>", unsafe_allow_html=True)

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
        "I Love you so much meena,Meri jan,Begum G"
    ]
    for wish in wishes:
        st.markdown(f"<h3 style='color: #9c27b0;'>{wish}</h3>", unsafe_allow_html=True)
        time.sleep(2)
        st.empty()
else:
    st.write("Click the button above to get your birthday wish!")
