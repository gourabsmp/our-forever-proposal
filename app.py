import streamlit as st
import os
import time
import requests
from streamlit_lottie import st_lottie

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Project Forever", page_icon="💍", layout="wide", initial_sidebar_state="collapsed")

# --- 2. INITIALIZE MEMORY (SESSION STATE) ---
if 'forgiven' not in st.session_state:
    st.session_state.forgiven = False
if 'proposal_accepted' not in st.session_state:
    st.session_state.proposal_accepted = False
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0
if 'decrypted' not in st.session_state:
    st.session_state.decrypted = False

# --- 3. CUSTOM HEART BALLOON ANIMATION ---
def rain_hearts():
    st.markdown("""
    <style>
    .heart-container { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999; overflow: hidden; }
    .heart-balloon { position: absolute; bottom: -100px; font-size: 40px; animation: floatUp 5s ease-in infinite; opacity: 0.8; }
    @keyframes floatUp {
        0% { transform: translateY(0) scale(0.8); opacity: 1; }
        100% { transform: translateY(-120vh) scale(1.2); opacity: 0; }
    }
    .h1 { left: 10%; animation-duration: 4s; animation-delay: 0s; font-size: 50px; }
    .h2 { left: 30%; animation-duration: 6s; animation-delay: 1s; font-size: 60px; }
    .h3 { left: 50%; animation-duration: 5s; animation-delay: 0.5s; font-size: 45px; }
    .h4 { left: 70%; animation-duration: 7s; animation-delay: 0s; font-size: 55px; }
    .h5 { left: 90%; animation-duration: 4.5s; animation-delay: 1.5s; font-size: 65px; }
    .h6 { left: 20%; animation-duration: 5.5s; animation-delay: 0.8s; font-size: 40px; }
    .h7 { left: 80%; animation-duration: 6.5s; animation-delay: 0.2s; font-size: 70px; }
    </style>
    <div class="heart-container">
        <div class="heart-balloon h1">❤️</div>
        <div class="heart-balloon h2">💖</div>
        <div class="heart-balloon h3">❤️</div>
        <div class="heart-balloon h4">💕</div>
        <div class="heart-balloon h5">❤️</div>
        <div class="heart-balloon h6">💗</div>
        <div class="heart-balloon h7">💖</div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. LOAD ANIMATIONS SAFELY ---
@st.cache_data
def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_heart = load_lottie("https://assets5.lottiefiles.com/packages/lf20_077re9y1.json")
lottie_ring = load_lottie("https://assets10.lottiefiles.com/packages/lf20_9n6mub8s.json")
lottie_fireworks = load_lottie("https://assets7.lottiefiles.com/packages/lf20_aefbwihu.json")

# --- 5. PREMIUM CSS ---
st.markdown("""
    <style>
    .gradient-text { background: -webkit-linear-gradient(45deg, #ff0844, #ffb199); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: 900; font-size: 3em; padding-bottom: 10px; }
    .yes-button > button { width: 100%; border-radius: 50px; background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%); color: white; font-weight: 900; font-size: 26px; height: 3.5em; border: none; animation: pulse 2s infinite; transition: 0.3s; }
    .yes-button > button:hover { transform: scale(1.05); }
    @keyframes pulse { 0% { box-shadow: 0 0 10px rgba(0, 176, 155, 0.4); } 50% { box-shadow: 0 0 30px rgba(0, 176, 155, 0.9); } 100% { box-shadow: 0 0 10px rgba(0, 176, 155, 0.4); } }
    .no-button > button { width: 100%; border-radius: 50px; background-color: #2b2b2b; color: #ff4b4b; border: 1px solid #ff4b4b; font-weight: bold; height: 3.5em; transition: 0.1s; }
    .no-button > button:hover { animation: shake 0.4s; animation-iteration-count: infinite; background-color: #ff4b4b; color: white; }
    @keyframes shake { 0% { transform: translate(1px, 1px) rotate(0deg); } 25% { transform: translate(-2px, -2px) rotate(-1deg); } 50% { transform: translate(2px, 2px) rotate(1deg); } 75% { transform: translate(-2px, 2px) rotate(-1deg); } 100% { transform: translate(1px, -1px) rotate(0deg); } }
    </style>
    """, unsafe_allow_html=True)

# --- 6. DYNAMIC HEADER ---
col_h1, col_h2, col_h3 = st.columns([1,2,1])
with col_h2:
    if lottie_heart:
        st_lottie(lottie_heart, height=150, key="heart")
    st.markdown("<div class='gradient-text'>Deployment: Our_Forever.exe</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #a8a8a8;'>A personalized software update for my future wife.</p>", unsafe_allow_html=True)

st.divider()

# --- 7. TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 Diagnostics", "📊 The Dataset", "🧠 Predictive ML Model", "💖 Query DB", "🚀 Final Deployment"])

with tab1:
    st.subheader("System Diagnostics & Apology")
    st.write("I know I've caused some bugs in our system lately. I might be studying machine learning, but no algorithm could have ever predicted how lucky I'd be to find you.")
    st.write("Even when I'm grinding through those 5:30 PM to 3:30 AM shifts, you are the one keeping my system running. You are the best part of my day, every single day.")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Arguments Won By You", value="100%", delta="Always Right")
    col2.metric(label="My Love For You", value="Infinite", delta="Growing Daily")
    col3.metric(label="System Uptime", value="Forever", delta="No More Downtime")

with tab2:
    st.subheader("Training Data (Our Best Memories)")
    colA, colB = st.columns(2)
    with colA:
        if os.path.exists("us_yellow.jpeg"): st.image("us_yellow.jpeg", use_container_width=True)
    with colB:
        if os.path.exists("us_candid.jpeg"): st.image("us_candid.jpeg", use_container_width=True)

with tab3:
    st.subheader("🧠 Running Future Predictions")
    if st.button("Initialize ML Model"):
        my_bar = st.progress(0, text="Training model on our memories...")
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1, text="Training model on our memories...")
        time.sleep(0.5)
        my_bar.empty()
        st.success("Model Training Complete! Accuracy: 100%")
        st.metric(label="Probability of Happily Ever After", value="99.99%", delta="Statistically Significant")

with tab4:
    st.subheader("Querying the Database of You")
    with st.expander("📌 Query 1: Why I work so hard"):
        st.write("Because I want to build a beautiful life for us. Every line of SQL and Python is for our future.")
    with st.expander("📌 Query 2: My favorite feature about you"):
        st.write("Your smile. It's the only code in my life that executes perfectly every single time.")

# TAB 5: THE GRAND REVEAL (NO MORE SLIDER)
with tab5:
    st.subheader("🛠️ Connection Security Protocol")
    st.markdown("<p style='color: #a8a8a8; font-size: 16px;'>🔒 SYSTEM LOCKED: Emotional override required to push this update to production.</p>", unsafe_allow_html=True)
    
    # THE FORGIVENESS BUTTON
    if not st.session_state.forgiven:
        if st.button("❤️ INITIATE FORGIVENESS PROTOCOL ❤️"):
            st.session_state.forgiven = True
            st.rerun()

    # AFTER SHE FORGIVES
    if st.session_state.forgiven:
        # Trigger the custom floating hearts!
        rain_hearts()
        
        # The Hacker Decryption Sequence
        if not st.session_state.decrypted:
            with st.spinner("Decrypting Administrator Heart... Bypassing Firewalls..."):
                time.sleep(2.5)
            st.session_state.decrypted = True
            st.rerun()

        if st.session_state.decrypted:
            st.success("Firewalls disabled. Heart fully unlocked. Welcome to my forever.")
            st.divider()
            
            st.markdown("<div class='gradient-text' style='font-size: 2.5em;'>💍 The Final Commitment</div>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            agree = st.checkbox("I agree to the Terms & Conditions (including putting up with my late night coding sessions).")
            
            if agree:
                st.markdown("<br>", unsafe_allow_html=True)
                b_col1, b_col2 = st.columns(2)
                
                with b_col1:
                    st.markdown('<div class="yes-button">', unsafe_allow_html=True)
                    if st.button("YES, I WILL MARRY YOU! 💍"):
                        st.session_state.proposal_accepted = True
                        st.session_state.no_clicks = 0
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                with b_col2:
                    st.markdown('<div class="no-button">', unsafe_allow_html=True)
                    if st.button("No, cancel update"):
                        st.session_state.no_clicks += 1
                    st.markdown('</div>', unsafe_allow_html=True)

                # Refusal Logic
                if st.session_state.no_clicks > 0 and not st.session_state.proposal_accepted:
                    st.error(f"⚠️ FATAL SYSTEM ERROR: 'No' is strictly forbidden by my heart's protocol. (Attempt {st.session_state.no_clicks}). Please click YES.")
                    
                # Celebration Logic (BUG FIXED HERE!)
                if st.session_state.proposal_accepted:
                    st.snow()
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("<div class='gradient-text' style='font-size: 4em;'>SHE SAID YES! ❤️</div>", unsafe_allow_html=True)

                    c1, c2, c3 = st.columns([1, 2, 1])
                    with c2:
                        if lottie_fireworks:
                            st_lottie(lottie_fireworks, height=200, key="fireworks")
                        if lottie_ring:
                            st_lottie(lottie_ring, height=250, key="ring_final")
                        # The error is completely removed from this line:
                        if os.path.exists("us_red.jpeg"):
                            st.image("us_red.jpeg", use_container_width=True)

                    st.markdown("<br>", unsafe_allow_html=True)
                    msg = "I promise to love you, support your dreams, and debug our life together forever."
                    t = st.empty()
                    for i in range(len(msg) + 1):
                        t.markdown(f"<h3 style='color: #a8a8a8;'><i>{msg[:i]}</i></h3>", unsafe_allow_html=True)
                        time.sleep(0.04)
