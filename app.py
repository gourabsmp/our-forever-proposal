import streamlit as st
import os
import time
import requests
import base64
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Project Forever", page_icon="💍", layout="wide", initial_sidebar_state="collapsed")

# --- 2. INITIALIZE MEMORY (SESSION STATE) ---
if 'forgiven' not in st.session_state:
    st.session_state.forgiven = False
if 'proposal_accepted' not in st.session_state:
    st.session_state.proposal_accepted = False
if 'decrypted' not in st.session_state:
    st.session_state.decrypted = False

# --- 3. HELPER FUNCTIONS ---
def rain_hearts():
    st.markdown("""
    <style>
    .heart-container { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999; overflow: hidden; }
    .heart-balloon { position: absolute; bottom: -100px; font-size: 45px; animation: floatUp 6s ease-in infinite; opacity: 0.85; filter: drop-shadow(0px 0px 10px rgba(255, 105, 180, 0.5)); }
    @keyframes floatUp { 0% { transform: translateY(0) scale(0.8) rotate(0deg); opacity: 1; } 100% { transform: translateY(-120vh) scale(1.3) rotate(20deg); opacity: 0; } }
    .h1 { left: 10%; animation-duration: 4.5s; animation-delay: 0s; }
    .h2 { left: 30%; animation-duration: 6.5s; animation-delay: 1s; font-size: 65px; }
    .h3 { left: 50%; animation-duration: 5.5s; animation-delay: 0.5s; }
    .h4 { left: 70%; animation-duration: 7.5s; animation-delay: 0s; font-size: 60px; }
    .h5 { left: 90%; animation-duration: 5s; animation-delay: 1.5s; font-size: 70px; }
    .h6 { left: 20%; animation-duration: 6s; animation-delay: 0.8s; }
    .h7 { left: 80%; animation-duration: 7s; animation-delay: 0.2s; font-size: 55px; }
    </style>
    <div class="heart-container">
        <div class="heart-balloon h1">❤️</div><div class="heart-balloon h2">💖</div><div class="heart-balloon h3">❤️</div>
        <div class="heart-balloon h4">💕</div><div class="heart-balloon h5">❤️</div><div class="heart-balloon h6">💗</div><div class="heart-balloon h7">💖</div>
    </div>
    """, unsafe_allow_html=True)

def autoplay_audio(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
            st.markdown(md, unsafe_allow_html=True)

def render_polaroid(image_path, caption, tilt="0deg"):
    if os.path.exists(image_path):
        st.markdown(f"""
        <div style="background: #ffffff; padding: 10px 10px 45px 10px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); 
                    border-radius: 4px; text-align: center; margin: auto; margin-bottom: 20px; 
                    transform: rotate({tilt}); transition: transform 0.3s;">
            <img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, 'rb').read()).decode()}" style="width: 100%; border-radius: 2px;">
            <div style="font-family: 'Brush Script MT', cursive; font-size: 26px; color: #2b2b2b; margin-top: 10px;">~ {caption} ~</div>
        </div>
        """, unsafe_allow_html=True)

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

# --- 4. PREMIUM CSS ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #2a0a18 0%, #0a0a0a 100%); }
    .gradient-text { background: -webkit-linear-gradient(45deg, #ff758c, #ff7eb3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: 900; font-size: 3.5em; padding-bottom: 5px; letter-spacing: 2px;}
    .sub-text { text-align: center; font-style: italic; color: #ffb6c1; font-size: 1.2em; margin-bottom: 20px;}
    .yes-button > button { width: 100%; border-radius: 50px; background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%); color: white; font-weight: 900; font-size: 26px; height: 3.5em; border: none; animation: pulse 2s infinite; z-index: 100; }
    .yes-button > button:hover { transform: scale(1.05); }
    @keyframes pulse { 0% { box-shadow: 0 0 15px rgba(0, 176, 155, 0.6); } 50% { box-shadow: 0 0 35px rgba(0, 176, 155, 1); } 100% { box-shadow: 0 0 15px rgba(0, 176, 155, 0.6); } }
    </style>
    """, unsafe_allow_html=True)

# --- 5. DYNAMIC HEADER ---
col_h1, col_h2, col_h3 = st.columns([1,3,1])
with col_h2:
    if lottie_heart: st_lottie(lottie_heart, height=180, key="heart")
    st.markdown("<div class='gradient-text'>Deployment: Our_Forever.exe</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>A personalized software update for the love of my life.</div>", unsafe_allow_html=True)

st.divider()

# --- 6. TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["❤️ Diagnostics", "📜 Commit History", "🧠 The Algorithm", "📂 Database", "💍 Final Update"])

# TAB 1: Diagnostics
with tab1:
    st.subheader("System Diagnostics: My Heart")
    st.write("I might be studying Python, SQL, and Machine Learning, but no algorithm could have ever predicted how incredibly lucky I'd be to find you.")
    st.write("Even when I'm grinding through those brutal 5:30 PM to 3:30 AM work shifts, you are the light keeping my servers running. You are my greatest feature.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c1:
        render_polaroid("Always_Smiling.jpeg", "My favorite view", tilt="-3deg")
    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.metric(label="Arguments Won By You", value="100%", delta="Always Right")
        st.metric(label="My Love For You", value="Infinite", delta="Growing Daily")
        st.metric(label="System Uptime", value="Forever", delta="No More Downtime")
    with c3:
        render_polaroid("Beautiful_Day.jpeg", "Stunning", tilt="3deg")

# TAB 2: Commit History
with tab2:
    st.subheader("📜 Version Control: Our Story")
    st.write("Every great software has a beautiful version history. Here is ours.")
    
    t1, t2 = st.columns([2, 1])
    with t1:
        st.markdown("### 🔹 Commit #001: The Initial Push")
        st.write("The moment my life changed for the better. The foundation of our entire project was built on smiles like this.")
    with t2: render_polaroid("us_yellow.jpeg", "The Spark", tilt="2deg")
    
    st.divider()
    
    st.markdown("### 🔹 Commit #050: Merging Branches")
    st.write("Navigating life together. From the late nights to the early mornings, we started building our own little world.")
        
    st.divider()
    
    t5, t6 = st.columns([2, 1])
    with t5:
        st.markdown("### 🔹 Commit #100: Flawless Execution")
        st.write("Look at us now. Every bug fixed, every issue resolved. We are ready for the ultimate production deployment.")
    with t6: render_polaroid("Glowing_Together.jpeg", "Shining Bright", tilt="1deg")

# TAB 3: The Algorithm
with tab3:
    st.subheader("🧠 Running The Soulmate Algorithm")
    st.write("Analyzing historical data, late-night conversations, and thousands of smiles to predict our future trajectory...")
    
    if st.button("Initialize Soulmate Prediction"):
        my_bar = st.progress(0, text="Training model on our memories...")
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1, text="Calculating forever...")
        time.sleep(0.5)
        my_bar.empty()
        
        st.success("Analysis Complete! Result: Perfect Match.")
        st.metric(label="Probability of Happily Ever After", value="100%", delta="Statistically Guaranteed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        c_space1, c_img, c_space2 = st.columns([1, 2, 1])
        with c_img:
            # THIS IS YOUR NEW FESTIVAL PHOTO
            render_polaroid("Perfect_Match.jpeg", "The Ultimate Training Data")

# TAB 4: Database
with tab4:
    st.subheader("📂 Querying the Database of You")
    
    with st.expander("📌 Query: SELECT * FROM motivations WHERE reason = 'work_hard';"):
        st.write("Result: Because I want to build a beautiful life and a safe home for us. Every line of code is dedicated to building our future.")
    with st.expander("📌 Query: SELECT best_feature FROM you;"):
        st.write("Result: Your smile. It's the only code in my life that executes flawlessly every single time.")
        
    st.markdown("<br><h4>Running Final Query: <code>SELECT * FROM our_future;</code></h4>", unsafe_allow_html=True)
    c_space3, c_img2, c_space4 = st.columns([1, 2, 1])
    with c_img2:
        render_polaroid("Never_Letting_Go.jpeg", "Never letting go", tilt="-1deg")

# TAB 5: The Proposal
with tab5:
    st.subheader("🛠️ Connection Security Protocol")
    st.markdown("<p style='color: #ffb6c1; font-size: 16px;'>🔒 SYSTEM LOCKED: Emotional override required to push this update to production.</p>", unsafe_allow_html=True)
    
    if not st.session_state.forgiven:
        if st.button("❤️ INITIATE FORGIVENESS PROTOCOL ❤️"):
            st.session_state.forgiven = True
            st.rerun()

    if st.session_state.forgiven:
        # Hearts appear immediately
        rain_hearts()
        
        if not st.session_state.decrypted:
            with st.spinner("Decrypting Administrator Heart... Bypassing Firewalls..."):
                time.sleep(2.5)
            st.session_state.decrypted = True
            st.rerun()

        if st.session_state.decrypted:
            st.success("Firewalls disabled. Heart fully unlocked. Welcome to my forever.")
            st.divider()
            
            st.markdown("<div class='gradient-text' style='font-size: 3em;'>💍 The Final Commitment</div>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            agree = st.checkbox("I agree to the Terms & Conditions (including loving me through all my late night coding sessions).")
            
            if agree:
                st.markdown("<br>", unsafe_allow_html=True)
                b_col1, b_col2 = st.columns(2)
                
                with b_col1:
                    st.markdown('<div class="yes-button">', unsafe_allow_html=True)
                    if st.button("YES, I WILL MARRY YOU! 💍"):
                        st.session_state.proposal_accepted = True
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                with b_col2:
                    st.button("No, cancel update", key="no_btn_static")

                components.html(
                    """
                    <script>
                    const huntAndAnimate = () => {
                        const parentDoc = window.parent.document;
                        const buttons = parentDoc.querySelectorAll('button');
                        buttons.forEach(btn => {
                            if (btn.innerText.includes("No, cancel update") && !btn.dataset.dodging) {
                                btn.dataset.dodging = 'true';
                                btn.style.backgroundColor = '#ff4b4b'; btn.style.color = 'white';
                                btn.style.border = '1px solid #ff4b4b'; btn.style.borderRadius = '50px';
                                btn.style.position = 'relative'; btn.style.zIndex = '999';
                                
                                const moveBtn = function(e) {
                                    e.preventDefault();
                                    const x = Math.floor(Math.random() * 400) - 200; 
                                    const y = Math.floor(Math.random() * 300) - 150;
                                    this.style.transform = `translate(${x}px, ${y}px)`;
                                    this.style.transition = 'transform 0.15s ease-out';
                                };
                                btn.addEventListener('mouseenter', moveBtn);
                                btn.addEventListener('touchstart', moveBtn, {passive: false});
                            }
                        });
                    };
                    setInterval(huntAndAnimate, 300);
                    </script>
                    """, height=0, width=0)
                    
                if st.session_state.proposal_accepted:
                    # MUSIC ONLY PLAYS HERE AFTER SHE CLICKS YES
                    autoplay_audio("song.mp3")
                    st.snow()
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # NEW CELEBRATION TEXT
                    st.markdown("<div class='gradient-text' style='font-size: 4em;'>LIFETIME UPDATE ACCEPTED! ❤️</div>", unsafe_allow_html=True)

                    c1, c2, c3 = st.columns([1, 2, 1])
                    with c2:
                        if lottie_fireworks: st_lottie(lottie_fireworks, height=250, key="fireworks")
                        if lottie_ring: st_lottie(lottie_ring, height=300, key="ring_final")
                        render_polaroid("My_Forever_Rose.jpeg", "My Forever")

                    st.markdown("<br>", unsafe_allow_html=True)
                    msg = "I promise to love you, support your dreams, and debug our life together forever."
                    t = st.empty()
                    for i in range(len(msg) + 1):
                        t.markdown(f"<h3 style='color: #ffb6c1; text-align: center;'><i>{msg[:i]}</i></h3>", unsafe_allow_html=True)
                        time.sleep(0.04)
