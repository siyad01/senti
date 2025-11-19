import streamlit as st
import openai
import pyperclip
# ──────────────────────────────────────────────────────────────
# 1. HIDE STREAMLIT MENU + FOOTER + MAKE IT LOOK LIKE A REAL APP
# ──────────────────────────────────────────────────────────────
hide_streamlit_style = """
<style>
    #MainMenu {margin-top: -80px;}
    header {visibility: hidden;}
    #MainMenu, footer {visibility: hidden;}
    .stAppDeployButton {display: none;}
    section[data-testid="stSidebar"] {display: none;}  /* optional: hide sidebar */
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.set_page_config(page_title="Senti - Roast",
                   page_icon="fire", layout="centered")

# ──────────────────────────────────────────────────────────────
# 2. OPENROUTER SETUP (safe with secrets)
# ──────────────────────────────────────────────────────────────
try:
    api_key = st.secrets["OPENROUTER_API_KEY"]
except:
    api_key = st.text_input("OpenRouter API Key",
                            type="password", placeholder="sk-or-...")
    if not api_key.startswith("sk-or"):
        st.warning("Enter your free OpenRouter key above")
        st.stop()

client = openai.OpenAI(
    api_key=api_key, base_url="https://openrouter.ai/api/v1")

# ──────────────────────────────────────────────────────────────
# 3. UI
# ──────────────────────────────────────────────────────────────
st.markdown("""
# Senti - Roast!
**The Internet’s Meanest (and funniest) AI Roaster** – 100 % free
""", unsafe_allow_html=True)

victim = st.text_input("Your name (or your friend's name)",
                       placeholder="Elon Musk / My ex / Kevin")

col1, col2 = st.columns(2)
with col1:
    intensity = st.slider("Roast Intensity", 1, 5, 3,
                          help="1 = gentle, 5 = nuclear")
with col2:
    style = st.selectbox("Style", [
        "Gen-Z savage", "Gordon Ramsay", "Shakespeare", "Pirate", "British deadpan",
        "Karen at Starbucks", "Boomer uncle", "Anime villain", "Drunk Irish poet"
    ])

add_fact = st.checkbox("Add one embarrassing fact (makes it 10× funnier)")
fact = st.text_area("Fact about them", height=80) if add_fact else ""

# ──────────────────────────────────────────────────────────────
# 4. ROAST BUTTON + SESSION STATE (prevents refresh & copy issues)
# ──────────────────────────────────────────────────────────────
if "roast" not in st.session_state:
    st.session_state.roast = None

if st.button("ROAST THEM", type="primary", use_container_width=True):
    if not victim.strip():
        st.error("Need a name, coward!")
    else:
        with st.spinner("Cooking the perfect burn..."):
            style_prompt = {
                "Gen-Z savage": "Reply like a brutal Gen-Z TikToker",
                "Gordon Ramsay": "Reply exactly like Gordon Ramsay screaming at idiots",
                "Shakespeare": "Reply in Shakespearean English, dramatic and insulting",
                "Pirate": "Reply like a drunk pirate captain",
                "British deadpan": "Reply like a sarcastic British person, very dry",
                "Karen at Starbucks": "Reply like an entitled Karen demanding the manager",
                "Boomer uncle": "Reply like a conspiracy-loving boomer uncle",
                "Anime villain": "Reply like an over-the-top anime villain monologuing",
                "Drunk Irish poet": "Reply like a drunk Irish poet who insults beautifully"
            }[style]

            temp = 0.7 + (intensity * 0.1)

            prompt = f"""{style_prompt}. Roast this person as harshly and creatively as possible.
            Name: {victim}
            Fact: {fact or "none given"}
            Keep it under 80 words. Be funny, not actually harmful."""

            response = client.chat.completions.create(
                model="nvidia/nemotron-nano-9b-v2:free",   # ← fastest free model right now
                messages=[{"role": "user", "content": prompt}],
                temperature=temp,
                max_tokens=150
            )
            st.session_state.roast = response.choices[0].message.content.strip()
            st.rerun()

# ──────────────────────────────────────────────────────────────
# 5. DISPLAY ROAST + COPY BUTTON (no refresh!)
# ──────────────────────────────────────────────────────────────
if st.session_state.roast:
    st.success("ROAST DELIVERED")
    st.markdown(f"### {st.session_state.roast}")

    st.code(st.session_state.roast)

st.caption("Made with love & chaos in 2025 · Share the pain")
