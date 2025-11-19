import streamlit as st
import openai
import pyperclip

st.set_page_config(page_title="Roast Me AI", page_icon="fire")

# === OpenRouter Setup ===
try:
    api_key = st.secrets["OPENROUTER_API_KEY"]
except:
    api_key = st.sidebar.text_input("OpenRouter API Key", type="password")
    if not api_key.startswith("sk-or"):
        st.sidebar.warning("Enter your free OpenRouter key")
        st.stop()

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

st.title("Roast Me, AI!")
st.markdown("**The Internet's Meanest (and funniest) AI Roaster** - 100 % free")

col1, col2 = st.columns([3, 1])
with col1:
    victim = st.text_input(
        "Your name (or your friend's name)",
        placeholder="Elon Musk / My ex / Kevin from accounting"
    )
with_freq = st.checkbox("Add one embarrassing fact about them (makes it 10x funnier)")

fact = ""
if with_freq:
    fact = st.text_area("One quick fact (e.g. still uses Internet Explorer, cries at Pixar movies...)", height=80)

intensity = st.slider("Roast Intensity", 1, 5, 3,
                     help="1 = gentle nudge, 5 = career-ending")

style = st.selectbox("Roast Style", [
    "Gen-Z savage", "British deadpan", "Pirate", "Shakespeare", "Gordon Ramsay",
    "Karen at Starbucks", "Boomer Facebook uncle", "Anime villain", "Drunk Irish poet"
])

if st.button("ROAST THEM", type="primary"):
    if not victim.strip():
        st.error("Need a name, coward!")
    else:
        with st.spinner("Cooking the perfect burn..."):
            style_prompt = {
                "Gen-Z savage": "Reply like a brutal Gen-Z TikToker",
                "British deadpan": "Reply like a sarcastic British person, very dry",
                "Pirate": "Reply like a drunk pirate captain",
                "Shakespeare": "Reply in Shakespearean English, dramatic and insulting",
                "Gordon Ramsay": "Reply exactly like Gordon Ramsay screaming at idiots",
                "Karen at Starbucks": "Reply like an entitled Karen demanding the manager",
                "Boomer Facebook uncle": "Reply like a conspiracy-loving boomer uncle",
                "Anime villain": "Reply like an over-the-top anime villain monologuing",
                "Drunk Irish poet": "Reply like a drunk Irish poet who insults beautifully"
            }[style]

            temp = 0.7 + (intensity * 0.1)

            prompt = f"""{style_prompt}. Roast this person as harshly and creatively as possible.
            Name: {victim}
            Fact: {fact if fact else "none given"}
            Keep it under 80 words. Be funny, not actually harmful."""

            response = client.chat.completions.create(
                model="nvidia/nemotron-nano-9b-v2:free",
                messages=[{"role": "user", "content": prompt}],
                temperature=temp,
                max_tokens=150
            )
            roast = response.choices[0].message.content.strip()

            st.success("**ROAST DELIVERED**")
            st.markdown(f"### {roast}")

            col_a = st.columns(1)
            with col_a:
                if st.button("Copy Roast"):
                    pyperclip.copy(roast)
                    st.success("Copied!")
            

st.caption("Built in 2025 | Runs on potato laptops | Share the pain")