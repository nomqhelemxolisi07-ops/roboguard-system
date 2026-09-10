import streamlit as st

# --- CONFIGURATION & STYLING ---
st.set_page_config(page_title="ROBO GUARD Heritage Portal", page_icon="🏛️", layout="wide")

# Zimbabwe Heritage Color Palette (Green, Gold, Soft Gray)
st.markdown("""
    <style>
    .main { background-color: #f4f6f4; }
    h1, h2 { color: #1e4620; font-weight: bold; }
    .stButton>button { background-color: #d4af37; color: black; font-weight: bold; border-radius: 8px; }
    .stButton>button:hover { background-color: #1e4620; color: white; }
    .css-1r6slb0 { background-color: #1e4620; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("🛡️ ROBO GUARD Network")
st.sidebar.markdown("*Preserving Zimbabwe's Legacy*")
page = st.sidebar.radio("Explore Portal:", ["🏛️ Visitor Information Hub", "🧠 Interactive Heritage Quiz", "🤖 Heritage AI Chatbot"])

st.sidebar.info("🌍 Scan the QR code at any heritage site to interact live!")

# ==========================================
# PAGE 1: VISITOR INFORMATION HUB
# ==========================================
if page == "🏛️ Visitor Information Hub":
    st.title("🏛️ Zimbabwe National Heritage Hub")
    st.subheader("Preserving our past through intelligent automation.")
    st.write("Welcome to the public information gateway. The ROBO GUARD ecosystem protects the structural and historical integrity of our ancestors' stories.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🪨 Matobo Hills")
        st.write("**Active Protection:** San Rock Art")
        st.caption("Monitoring 13,000-year-old ancient pigment drawings to eliminate oil contamination from human touch and unregulated tourist vandalism.")
        
    with col2:
        st.markdown("### 🏰 Great Zimbabwe")
        st.write("**Active Protection:** Mortarless Masonry")
        st.caption("Shielding the Great Enclosure and Conical Tower. Preventing wall degradation, stone climbing, and illicit souvenir rock harvesting.")
        
    with col3:
        st.markdown("### 🧱 Khami Ruins")
        st.write("**Active Protection:** Terraced Stone Platforms")
        st.caption("Active local node tracking structural shifts and human encroachment across the historic royal structural tiers here in Bulawayo.")

# ==========================================
# PAGE 2: INTERACTIVE HERITAGE QUIZ
# ==========================================
elif page == "🧠 Interactive Heritage Quiz":
    st.title("🧠 Tourist Engagement & Verification Quiz")
    st.write("Test your cultural protection knowledge to claim your Heritage Guardian status!")
    
    q1 = st.radio("1. Why were the structures of Great Zimbabwe built entirely without mortar?", 
                  ["They lacked building materials", "It was a specialized traditional stone-shaping engineering style", "They were temporary camps"])
    
    q2 = st.radio("2. What is the main threat to the ancient rock art in Matobo Hills?", 
                  ["Wind and rain erosion", "Wild animals", "Human touch, skin oil transfer, and modern graffiti"])
                  
    q3 = st.radio("3. ROBO GUARD's automated tourist safety signage updates text slideshows in which languages?", 
                  ["English, Shona, and isiNdebele", "Swahili and French", "English only"])

    if st.button("Submit Assessment"):
        score = 0
        if q1 == "It was a specialized traditional stone-shaping engineering style": score += 1
        if q2 == "Human touch, skin oil transfer, and modern graffiti": score += 1
        if q3 == "English, Shona, and isiNdebele": score += 1
        
        st.success(f"Assessment Complete! Your Score: {score}/3")
        if score == 3:
            st.balloons()
            st.markdown("**🎉 Status: Verified Heritage Guardian Certificate Granted!**")

# ==========================================
# PAGE 3: HERITAGE AI CHATBOT
# ==========================================
elif page == "🤖 Heritage AI Chatbot":
    st.title("🤖 ROBO GUARD Interactive Concierge")
    st.write("Ask our on-site digital assistant anything about our heritage conservation zones.")
    
    user_query = st.text_input("Type your question here (e.g., 'How do you protect Matobo?' or 'Tell me about Great Zimbabwe'):")
    
    if user_query:
        query_lower = user_query.lower()
        st.markdown("### 🤖 ROBO GUARD Assistant:")
        if "matobo" in query_lower or "art" in query_lower or "rock" in query_lower:
            st.info("ROBO GUARD deployed at Matobo utilizes localized proximity alerts to detect physical human encroachment within a 1.5-meter boundary of the cave walls, preserving the ancient pigments from destructive skin oils.")
        elif "zimbabwe" in query_lower or "wall" in query_lower or "mortar" in query_lower:
            st.info("At Great Zimbabwe, the system enforces a strict perimeter around the mortarless dry-stone blocks to stop tourists from scaling or leaning on unstable structures.")
        elif "khami" in query_lower or "ruins" in query_lower:
            st.info("The Khami node monitors the terraced retaining masonry layers right outside Bulawayo. It safeguards the historic royal platforms against structural wear caused by pedestrian foot traffic footprint trespass.")
        else:
            st.info("I am the ROBO GUARD visitor framework. I can answer questions about how we protect Matobo Hills, Great Zimbabwe, and Khami Ruins using automated sensor networks.")
