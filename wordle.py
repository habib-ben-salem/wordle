import streamlit as st
import random

# --- SHARED STATE ---
@st.cache_resource
def get_global_game_state():
    return {
        "current_word": "SURGE",
        "dictionary": ["CRAWL", "STONE", "SPIRE", "FUNDS", "SURGE", "CLEAR", "BOARD", "LIGHT"],
        "admin_password": "admin" 
    }

global_state = get_global_game_state()

st.set_page_config(page_title="Global Wordle", layout="centered")

# --- CUSTOM CSS FOR PERFECT ALIGNMENT ---
st.markdown("""
    <style>
    .stApp { background-color: #121213; color: white; }
    header, footer {visibility: hidden;}
    
    /* Center everything */
    .wordle-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }

    /* Grid Styling - Tight gaps */
    .grid {
        display: grid;
        grid-template-rows: repeat(6, 1fr);
        gap: 5px;
        margin-bottom: 20px;
    }
    .row {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 5px;
    }
    .tile {
        width: 52px;
        height: 52px;
        border: 2px solid #3a3a3c;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
    }

    /* Keyboard - Compact and centered */
    .kb-container { width: 100%; max-width: 450px; margin-top: 10px; }
    .kb-row { display: flex; justify-content: center; gap: 4px; margin-bottom: 6px; }
    
    /* We style Streamlit buttons to look like Wordle keys */
    div.stButton > button {
        background-color: #818384 !important;
        color: white !important;
        border: none !important;
        padding: 0px !important;
        height: 58px !important;
        width: 100% !important;
        font-weight: bold !important;
        font-size: 14px !important;
        min-width: 0px !important;
    }
    
    /* Special colors */
    .correct { background-color: #538d4e !important; border: none !important; }
    .present { background-color: #b59f3b !important; border: none !important; }
    .absent { background-color: #3a3a3c !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🌎 Global Wordle")

tab1, tab2 = st.tabs(["🎮 Play Game", "🔒 Admin Panel"])

with tab1:
    target_word = global_state["current_word"]
    
    if 'current_guess' not in st.session_state: st.session_state.current_guess = ""
    if 'guesses' not in st.session_state: st.session_state.guesses = []
    
    # 1. THE GRID (Manual HTML for perfect spacing)
    grid_html = '<div class="wordle-wrapper"><div class="grid">'
    for r in range(6):
        grid_html += '<div class="row">'
        for c in range(5):
            char = ""
            style = ""
            if r < len(st.session_state.guesses):
                guess = st.session_state.guesses[r]
                char = guess[c]
                if char == target_word[c]: style = "correct"
                elif char in target_word: style = "present"
                else: style = "absent"
            elif r == len(st.session_state.guesses) and c < len(st.session_state.current_guess):
                char = st.session_state.current_guess[c]
            grid_html += f'<div class="tile {style}">{char}</div>'
        grid_html += '</div>'
    grid_html += '</div></div>'
    st.markdown(grid_html, unsafe_allow_html=True)

    # 2. THE KEYBOARD (Centered with specific column widths)
    def press(k):
        if k == "ENTER":
            if len(st.session_state.current_guess) == 5:
                st.session_state.guesses.append(st.session_state.current_guess)
                st.session_state.current_guess = ""
        elif k == "⌫":
            st.session_state.current_guess = st.session_state.current_guess[:-1]
        elif len(st.session_state.current_guess) < 5:
            st.session_state.current_guess += k

    kb_rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    
    # Render Keyboard
    for i, row_letters in enumerate(kb_rows):
        letters = list(row_letters)
        if i == 2: # Add Enter and Backspace to bottom row
            letters = ["ENTER"] + letters + ["⌫"]
            cols = st.columns([1.5] + [1]*7 + [1.5])
        else:
            cols = st.columns(len(letters))
            
        for idx, char in enumerate(letters):
            if cols[idx].button(char, key=f"key_{char}"):
                press(char)
                st.rerun()

with tab2:
    pwd = st.text_input("Admin Password", type="password")
    if pwd == global_state["admin_password"]:
        if st.button("🚀 Reset Word for Everyone"):
            global_state["current_word"] = random.choice(global_state["dictionary"]).upper()
            st.session_state.guesses = []
            st.rerun()
