# Roast Me, AI!  
**The Internet’s Meanest (and funniest) AI Roaster**  

Live Demo → https://roast-me-ai-yourname.streamlit.app (replace with your actual link after deploying)

### What It Does
You give it a name + (optional) one embarrassing fact → the AI instantly roasts that person in the most savage, hilarious way possible.  
Choose roast style, intensity, and watch the carnage unfold. Perfect for group chats, parties, or settling scores.

### Features
- 5 roast intensity levels (Mild → Nuclear)  
- 9 roast styles: Gen-Z savage, Gordon Ramsay, Shakespeare, Pirate, Karen, etc.  
- Add one embarrassing fact for 10× funnier burns  
- One-click “Copy Roast” & “Send to Victim” (WhatsApp/Telegram ready)  
- 100 % free forever (runs on OpenRouter’s free Llama 3.1 Nemotron)  
- No login, no limits, works on phones too

### How to Use
1. Enter the victim’s name  
2. (Optional) Check the box and add one embarrassing fact  
3. Pick intensity & style  
4. Smash the big red **ROAST THEM** button  
5. Copy & send the burn (your friends will never recover)

### Tech Stack
- Streamlit (frontend + hosting)  
- OpenRouter API (free tier)  
- nvidia/nemotron-nano-9b-v2:free

### Local Run (optional)
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy Your Own (Free Forever)
1. Fork or upload the three files (`app.py`, `requirements.txt`, `.streamlit/secrets.toml`)  
2. Go to https://share.streamlit.io → New app → connect your repo → deploy  
3. Add your OpenRouter key in Secrets (`openrouter_api_key = "sk-or-..."`)

### Credits
Built in 2025 by [Your Name / GitHub Handle]  
Powered by OpenRouter’s free models  
Made to destroy egos and create laughter

Now go roast someone. They deserve it.