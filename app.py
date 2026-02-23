import streamlit as st
import os
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Project Forever", page_icon="💍", layout="wide", initial_sidebar_state="expanded")

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #fdfbfb; }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background: linear-gradient(135deg, #ff0844 0%, #ffb199 100%);
        color: white;
        font-weight: 900;
        font-size: 24px;
        height: 3em;
        border: none;
        box-shadow: 0 4px 15px 0 rgba(255, 8, 68, 0.3);
        transition: all 0.3s ease 0s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 8px 25px 0 rgba(255, 8, 68, 0.5); }
    h1, h2, h3 { color: #d63384; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>❤️</h1>", unsafe_allow_html=True)
    st.title("System Patch v2.0")
    st.info("Applying a permanent fix to the most critical connection in my life.")
    st.caption("Environment: Production | Status: Awaiting User Approval")

# --- 4. MAIN DASHBOARD ---
st.title("Deployment: Our_Forever.exe")
st.markdown("*A personalized software update for my future wife.*")
st.divider()

tab1, tab2, tab3 = st.tabs(["🔍 Root Cause Analysis", "📊 The 'Us' Dataset", "🚀 Final Deployment"])

# TAB 1: Diagnostics
with tab1:
    st.subheader("System Diagnostics & Apology")
    st.write("I know I've caused some bugs in our system lately. I might be studying machine learning, but no algorithm could have ever predicted how lucky I'd be to find you. Even during those late night shifts until 3:30 AM, you are the one keeping my system running. You are the best part of my day, every single day.")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Arguments Won By You", value="100%", delta="Always Right")
    col2.metric(label="My Love For You", value="Infinite", delta="Growing Daily")
    col3.metric(label="System Uptime", value="Forever", delta="No More Downtime")

# TAB 2: Memories
with tab2:
    st.subheader("Training Data (Our Best Memories)")
    st.write("I don't need Power BI to see the trend here: my life is objectively better when you are smiling.")
    colA, colB = st.columns(2)
    
    # Safely load Image 1
    with colA:
        if os.path.exists("us_yellow.jpeg"):
            st.image("us_yellow.jpeg", caption="The day you outshone the sun.", use_container_width=True)
        else:
            st.warning("⚠️ Image 'us_yellow.jpeg' not found. Please check spelling in your folder!")
            
    # Safely load Image 2
    with colB:
        if os.path.exists("us_candid.jpeg"):
            st.image("us_candid.jpeg", caption="My favorite dataset: Just Us.", use_container_width=True)
        else:
            st.warning("⚠️ Image 'us_candid.jpeg' not found. Please check spelling in your folder!")

# TAB 3: Proposal
with tab3:
    st.subheader("🛠️ Connection Security Protocol")
    st.write("Before we can push this update to production, I need you to pass the final security check.")
    mood = st.select_slider("", options=["Still Angry 😤", "Processing Data... ⚙️", "Missing You 🥺", "I Forgive You ❤️"], value="Still Angry 😤")

    if mood == "I Forgive You ❤️":
        st.balloons()
        st.success("Authentication successful. Administrator rights granted.")
        st.divider()
        st.markdown("<h2 style='text-align: center;'>💍 The Final Commitment</h2>", unsafe_allow_html=True)
        
        if st.button("WILL YOU MARRY ME?"):
            st.snow()
            st.markdown("<h1 style='text-align: center; color: #ff0844; font-size: 80px; font-weight: 900;'>SHE SAID YES! ❤️</h1>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                # Safely load Image 3
                if os.path.exists("us_red.jpeg"):
                    st.image("us_red.jpeg", use_container_width=True)
                else:
                    st.warning("⚠️ Image 'us_red.jpeg' not found. (But I still love you!)")
                    
            st.markdown("<br>", unsafe_allow_html=True)
            
            msg = "I promise to love you, support your dreams, and debug our life together forever. You are my home."
            t = st.empty()
            for i in range(len(msg) + 1):
                t.markdown(f"<h3 style='text-align: center; color: #333;'><i>{msg[:i]}</i></h3>", unsafe_allow_html=True)
                time.sleep(0.04)