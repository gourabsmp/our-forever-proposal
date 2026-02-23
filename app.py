import streamlit as st
import os
import time
import requests
from streamlit_lottie import st_lottie

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Project Forever v4.0", page_icon="💍", layout="wide", initial_sidebar_state="collapsed")

# --- 2. INITIALIZE MEMORY (SESSION STATE) ---
if 'proposal_accepted' not in st.session_state:
    st.session_state.proposal_accepted = False
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0

# --- 3. LOAD ANIMATIONS SAFELY ---
@st.cache_data
def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_heart = load_lottie("https://assets5.lottiefiles.com/packages/lf20_077re9y1.json")
lottie_ring = load_lottie("https://assets10.lottiefiles.com/packages/lf20_9n6mub8s.json")

# --- 4. CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #fdfbfb; }
    
    /* Glowing YES Button */
    .yes-button > button {
        width: 100%;
        border-radius: 50px;
        background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
        color: white;
        font-weight: 900;
        font-size: 26px;
        height: 3.5em;
        border: none;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 10px rgba(0, 176, 155, 0.4); transform: scale(1); }
        50% { box-shadow: 0 0 30px rgba(0, 176, 155, 0.8); transform: scale(1.02); }
        100% { box-shadow: 0 0 10px rgba(0, 176, 155, 0.4); transform: scale(1); }
    }
    
    /* Subtle NO Button */
    .no-button > button {
        width: 100%;
        border-radius: 50px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        height: 3.5em;
    }
    
    h1, h2, h3 { color: #d63384; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 5. DYNAMIC HEADER ---
col_h1, col_h2, col_h3 = st.columns([1,2,1])
with col_h2:
    if lottie_heart:
        st_lottie(lottie_heart, height=150, key="heart")
    st.title("Deployment: Our_Forever.exe")
    st.markdown("<p style='text-align: center; font-style: italic; color: gray;'>A personalized software update for my future wife.</p>", unsafe_allow_html=True)

st.divider()

# --- 6. ADVANCED TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 Diagnostics", "📊 The Dataset", "🧠 Predictive ML Model", "💖 Query DB", "🚀 Final Deployment"])

# TAB 1: Diagnostics
with tab1:
    st.subheader("System Diagnostics & Apology")
    st.write("I know I've caused some bugs in our system lately. I might be studying machine learning, but no algorithm could have ever predicted how lucky I'd be to find you.")
    st.write("Even when I'm grinding through those 5:30 PM to 3:30 AM shifts, you are the one keeping my system running. You are the best part of my day.")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Arguments Won By You", value="100%", delta="Always Right")
    col2.metric(label="My Love For You", value="Infinite", delta="Growing Daily")
    col3.metric(label="System Uptime", value="Forever", delta="No More Downtime")

# TAB 2: Memories
with tab2:
    st.subheader("Training Data (Our Best Memories)")
    colA, colB = st.columns(2)
    with colA:
        if os.path.exists("us_yellow.jpeg"):
            st.image("us_yellow.jpeg", caption="The day you outshone the sun.", use_container_width=True)
    with colB:
        if os.path.exists("us_candid.jpeg"):
            st.image("us_candid.jpeg", caption="My favorite dataset.", use_container_width=True)

# TAB 3: MACHINE LEARNING (NEW)
with tab3:
    st.subheader("🧠 Running Future Predictions")
    st.write("Click below to run a predictive model on our relationship trajectory based on historical data.")
    
    if st.button("Initialize ML Model"):
        progress_text = "Training model on our memories..."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.03) # Fakes a loading time
            my_bar.progress(percent_complete + 1, text=progress_text)
            
        time.sleep(0.5)
        my_bar.empty()
        
        st.success("Model Training Complete! Model Accuracy: 100%")
        st.metric(label="Probability of Happily Ever After", value="99.99%", delta="Statistically Significant")
        st.info("The algorithm has spoken. Please proceed to the Final Deployment tab.")

# TAB 4: Expanders
with tab4:
    st.subheader("Querying the Database of You")
    with st.expander("📌 Query 1: Why I work so hard"):
        st.write("Because I want to build a beautiful life for us. Every line of SQL and Python is for our future.")
    with st.expander("📌 Query 2: My favorite feature about you"):
        st.write("Your smile. It's the only code in my life that executes perfectly every single time.")

# TAB 5: The Proposal (With Trick Buttons!)
with tab5:
    st.subheader("🛠️ Connection Security Protocol")
    mood = st.select_slider("", options=["Still Angry 😤", "Processing Data... ⚙️", "Missing You 🥺", "I Forgive You ❤️"], value="Still Angry 😤")

    if mood == "I Forgive You ❤️":
        st.balloons()
        st.divider()
        st.markdown("<h2>💍 The Final Commitment</h2>", unsafe_allow_html=True)
        
        # Terms and Conditions Checkbox
        agree = st.checkbox("I agree to the Terms & Conditions (including putting up with my late night coding sessions).")
        
        if agree:
            # Layout for the two buttons
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

            # Logic for the NO button
            if st.session_state.no_clicks > 0 and not st.session_state.proposal_accepted:
                st.error(f"⚠️ FATAL SYSTEM ERROR: 'No' is not a valid input. (Error count: {st.session_state.no_clicks}). Please click YES to continue.")
                
            # Logic for the YES button
            if st.session_state.proposal_accepted:
                st.snow()
                st.markdown("<h1 style='font-size: 70px; color: #00b09b;'>SHE SAID YES! ❤️</h1>", unsafe_allow_html=True)

                c1, c2, c3 = st.columns([1, 2, 1])
                with c2:
                    if lottie_ring:
                        st_lottie(lottie_ring, height=300, key="ring_final")
                    if os.path.exists("us_red.jpeg"):
                        st.image("us_red.jpeg", use_container_width=True)

                st.markdown("<br>", unsafe_allow_html=True)
                msg = "I promise to love you, support your dreams, and debug our life together forever."
                t = st.empty()
                for i in range(len(msg) + 1):
                    t.markdown(f"<h3><i>{msg[:i]}</i></h3>", unsafe_allow_html=True)
                    time.sleep(0.04)
