import streamlit as st
import random

# --- SHARED STATE ---
@st.cache_resource
def get_global_game_state():
    return {
        "current_word": "SURGE",
        "dictionary": ["CRAWL", "STONE", "SPIRE", "FUNDS", "SURGE", "CLEAR", "BOARD"],
        "admin_password": "admin" 
    }

global_state = get_global_game_state()

st.set_page_config(page_title="Global Wordle", layout="centered")

# CSS for the UI
st.markdown("""
    <style>
    .stApp { background-color: #121213; color: white; }
    .wordle-container { display: flex; flex-direction: column; align-items: center; font-family: 'Clear Sans', 'Helvetica Neue', Arial, sans-serif; }
    .grid { display: grid; grid-template-rows: repeat(6, 1fr); grid-gap: 5px; margin-bottom: 30px; }
    .row { display: grid; grid-template-columns: repeat(5, 1fr); grid-gap: 5px; }
    .tile { width: 58px; height: 58px; border: 2px solid #3a3a3c; display: flex; align-items: center; justify-content: center; font-size: 30px; font-weight: bold; text-transform: uppercase; user-select: none; }
    
    .keyboard { width: 100%; max-width: 500px; display: flex; flex-direction: column; gap: 8px; }
    .kb-row { display: flex; justify-content: center; gap: 6px; }
    .key { background-color: #818384; color: white; border: 0; border-radius: 4px; height: 58px; padding: 0; display: flex; align-items: center; justify-content: center; cursor: pointer; font-weight: bold; flex: 1; text-transform: uppercase; }
    .key.large { flex: 1.5; font-size: 12px; }
    
    /* Wordle Colors */
    .correct { background-color: #538d4e !important; border: none; }
    .present { background-color: #b59f3b !important; border: none; }
    .absent { background-color: #3a3a3c !important; border: none; }
    </style>
""", unsafe_allow_html=True)

st.title("🌎 Global Wordle")

tab1, tab2 = st.tabs(["🎮 Play Game", "🔒 Admin Panel"])

with tab1:
    target_word = global_state["current_word"]
    
    # We use a hidden input and JavaScript to bridge the gap between UI clicks and Streamlit logic
    if 'current_guess' not in st.session_state: st.session_state.current_guess = ""
    if 'guesses' not in st.session_state: st.session_state.guesses = []
    
    # Grid Display logic
    st.markdown('<div class="wordle-container">', unsafe_allow_html=True)
    grid_html = '<div class="grid">'
    for r in range(6):
        grid_html += '<div class="row">'
        for c in range(5):
            char = ""
            status_class = ""
            
            # Filled guesses
            if r < len(st.session_state.guesses):
                guess = st.session_state.guesses[r]
                char = guess[c]
                if char == target_word[c]: status_class = "correct"
                elif char in target_word: status_class = "present"
                else: status_class = "absent"
            # Current typing row
            elif r == len(st.session_state.guesses) and c < len(st.session_state.current_guess):
                char = st.session_state.current_guess[c]
                
            grid_html += f'<div class="tile {status_class}">{char}</div>'
        grid_html += '</div>'
    grid_html += '</div>'
    st.markdown(grid_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Mouse Keyboard Logic
    def handle_click(key):
        if key == "ENTER":
            if len(st.session_state.current_guess) == 5:
                st.session_state.guesses.append(st.session_state.current_guess)
                st.session_state.current_guess = ""
        elif key == "BACK":
            st.session_state.current_guess = st.session_state.current_guess[:-1]
        elif len(st.session_state.current_guess) < 5:
            st.session_state.current_guess += key

    # Keyboard Layout
    kb_layout = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACK"]
    ]

    st.write("") # Spacer
    for row in kb_layout:
        cols = st.columns(len(row))
        for i, char in enumerate(row):
            label = "⌫" if char == "BACK" else char
            # Styling keys based on game history
            if st.button(label, key=f"kb_{char}", use_container_width=True):
                handle_click(char)
                st.rerun()

with tab2:
    pwd = st.text_input("Admin Password", type="password")
    if pwd == global_state["admin_password"]:
        if st.button("🚀 Roll New Global Word"):
            global_state["current_word"] = random.choice(global_state["dictionary"]).upper()
            st.session_state.guesses = []
            st.rerun()
