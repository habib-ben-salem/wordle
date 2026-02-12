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

# --- CSS FOR PIXEL-PERFECT UI ---
st.markdown("""
    <style>
    .stApp { background-color: #121213; color: white; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    
    /* Center the board */
    .wordle-wrapper { display: flex; flex-direction: column; align-items: center; width: 100%; }
    
    /* Grid Styling */
    .grid { display: grid; grid-template-rows: repeat(6, 1fr); gap: 5px; margin-bottom: 30px; }
    .row { display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px; }
    .tile {
        width: 58px; height: 58px; border: 2px solid #3a3a3c;
        display: flex; align-items: center; justify-content: center;
        font-size: 2rem; font-weight: bold; text-transform: uppercase;
    }
    
    /* Colors */
    .correct { background-color: #538d4e !important; border: none; }
    .present { background-color: #b59f3b !important; border: none; }
    .absent { background-color: #3a3a3c !important; border: none; }

    /* Custom Keyboard Styling - NO EXTRA GREY SPACE */
    .kb-row { display: flex; justify-content: center; gap: 6px; margin-bottom: 8px; width: 100%; }
    
    /* Style the actual Streamlit buttons to be tight and dark */
    div.stButton > button {
        background-color: #818384 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        height: 58px !important;
        padding: 0px !important;
        font-weight: bold !important;
        min-width: 40px !important;
        width: 100% !important;
    }
    div.stButton > button:hover { background-color: #565758 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🌎 Global Wordle")

tab1, tab2 = st.tabs(["🎮 Play Game", "🔒 Admin Panel"])

with tab1:
    target_word = global_state["current_word"]
    
    if 'current_guess' not in st.session_state: st.session_state.current_guess = ""
    if 'guesses' not in st.session_state: st.session_state.guesses = []
    
    # 1. RENDER THE GRID
    grid_html = '<div class="wordle-wrapper"><div class="grid">'
    for r in range(6):
        grid_html += '<div class="row">'
        for c in range(5):
            char, status = "", ""
            if r < len(st.session_state.guesses):
                char = st.session_state.guesses[r][c]
                if char == target_word[c]: status = "correct"
                elif char in target_word: status = "present"
                else: status = "absent"
            elif r == len(st.session_state.guesses) and c < len(st.session_state.current_guess):
                char = st.session_state.current_guess[c]
            grid_html += f'<div class="tile {status}">{char}</div>'
        grid_html += '</div>'
    grid_html += '</div></div>'
    st.markdown(grid_html, unsafe_allow_html=True)

    # 2. RENDER THE KEYBOARD (Balanced Layout)
    def handle_click(k):
        if k == "ENTER":
            if len(st.session_state.current_guess) == 5:
                st.session_state.guesses.append(st.session_state.current_guess)
                st.session_state.current_guess = ""
        elif k == "⌫":
            st.session_state.current_guess = st.session_state.current_guess[:-1]
        elif len(st.session_state.current_guess) < 5:
            st.session_state.current_guess += k

    kb_layout = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "⌫"]
    ]

    for row in kb_layout:
        # Using specific width ratios to keep keys square and remove grey gaps
        cols = st.columns([1]*len(row))
        for i, char in enumerate(row):
            if cols[i].button(char, key=f"key_{char}"):
                handle_click(char)
                st.rerun()

with tab2:
    pwd = st.text_input("Admin Password", type="password")
    if pwd == global_state["admin_password"]:
        if st.button("🚀 Roll New Global Word"):
            global_state["current_word"] = random.choice(global_state["dictionary"]).upper()
            st.session_state.guesses = []
            st.rerun()
