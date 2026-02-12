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

# --- CSS FOR EXACT VISUAL MATCH ---
st.markdown("""
    <style>
    /* 1. Reset the entire page background */
    .stApp {
        background-color: #121213;
        color: white;
    }
    header, footer {visibility: hidden;}

    /* 2. Center the Game Board */
    .wordle-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }

    /* 3. The Word Grid (Pixel-Perfect from Image) */
    .grid {
        display: grid;
        grid-template-rows: repeat(6, 1fr);
        gap: 5px;
        margin-bottom: 40px; /* Space between board and keyboard */
    }
    .row {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 5px;
    }
    .tile {
        width: 62px;
        height: 62px;
        border: 2px solid #3a3a3c;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        font-weight: bold;
        text-transform: uppercase;
        font-family: 'Clear Sans', 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Tile Colors */
    .correct { background-color: #538d4e !important; border-color: #538d4e !important; }
    .present { background-color: #b59f3b !important; border-color: #b59f3b !important; }
    .absent { background-color: #3a3a3c !important; border-color: #3a3a3c !important; }
    .empty { background-color: transparent; }

    /* 4. KEYBOARD STYLING (The Hard Part) */
    
    /* Remove standard Streamlit button styling */
    div.stButton > button {
        background-color: #818384;
        color: white;
        border: none;
        border-radius: 4px;
        height: 58px;
        width: 100%;
        font-weight: bold;
        font-size: 14px;
        padding: 0;
        margin: 0;
        line-height: 58px; /* Vertically center text */
    }
    
    /* Hover Effect */
    div.stButton > button:hover {
        background-color: #565758;
        color: white;
        border: none;
    }
    
    /* Active/Focus Effect (Remove red border) */
    div.stButton > button:focus {
        background-color: #818384;
        color: white;
        box-shadow: none;
    }
    div.stButton > button:active {
        background-color: #565758;
        box-shadow: none;
    }

    /* Tweak the gap between columns in the keyboard rows */
    [data-testid="stHorizontalBlock"] {
        gap: 6px !important; /* Forces the keys to be close together */
    }
    
    </style>
""", unsafe_allow_html=True)

# --- LOGIC ---
st.title("🌎 Global Wordle")

tab1, tab2 = st.tabs(["🎮 Play Game", "🔒 Admin Panel"])

with tab1:
    target_word = global_state["current_word"]
    
    if 'current_guess' not in st.session_state: st.session_state.current_guess = ""
    if 'guesses' not in st.session_state: st.session_state.guesses = []
    
    # --- RENDER GRID ---
    grid_html = '<div class="wordle-wrapper"><div class="grid">'
    for r in range(6):
        grid_html += '<div class="row">'
        for c in range(5):
            char, status = "", "empty"
            # Past Guesses
            if r < len(st.session_state.guesses):
                char = st.session_state.guesses[r][c]
                if char == target_word[c]: status = "correct"
                elif char in target_word: status = "present"
                else: status = "absent"
            # Current Typing Row
            elif r == len(st.session_state.guesses) and c < len(st.session_state.current_guess):
                char = st.session_state.current_guess[c]
                status = "typing" # Could add a border style here if needed
                
            grid_html += f'<div class="tile {status}">{char}</div>'
        grid_html += '</div>'
    grid_html += '</div></div>'
    st.markdown(grid_html, unsafe_allow_html=True)

    # --- RENDER KEYBOARD ---
    def press_key(key):
        if key == "ENTER":
            if len(st.session_state.current_guess) == 5:
                st.session_state.guesses.append(st.session_state.current_guess)
                st.session_state.current_guess = ""
                st.rerun()
        elif key == "⌫":
            st.session_state.current_guess = st.session_state.current_guess[:-1]
            st.rerun()
        elif len(st.session_state.current_guess) < 5:
            st.session_state.current_guess += key
            st.rerun()

    # Keyboard Layout Configuration
    # We use st.columns with specific gap settings to create the layout
    
    # ROW 1 (Q-P)
    row1 = "QWERTYUIOP"
    c1 = st.columns(10)
    for idx, char in enumerate(row1):
        with c1[idx]:
            if st.button(char, key=f"btn_{char}", use_container_width=True):
                press_key(char)

    # ROW 2 (A-L) - Needs spacers to be centered
    row2 = "ASDFGHJKL"
    # We use a ratio: 0.5 spacer, 9 keys (size 1), 0.5 spacer
    c2 = st.columns([0.5] + [1]*9 + [0.5])
    for idx, char in enumerate(row2):
        with c2[idx+1]: # +1 because index 0 is spacer
            if st.button(char, key=f"btn_{char}", use_container_width=True):
                press_key(char)

    # ROW 3 (Enter - Z-M - Backspace)
    row3 = "ZXCVBNM"
    # Enter/Back are wider (1.5x)
    c3 = st.columns([1.5] + [1]*7 + [1.5])
    
    # Enter Key
    with c3[0]:
        if st.button("ENTER", key="btn_ENTER", use_container_width=True):
            press_key("ENTER")
            
    # Middle Keys
    for idx, char in enumerate(row3):
        with c3[idx+1]:
            if st.button(char, key=f"btn_{char}", use_container_width=True):
                press_key(char)
                
    # Backspace Key
    with c3[8]:
        if st.button("⌫", key="btn_BACK", use_container_width=True):
            press_key("⌫")

with tab2:
    pwd = st.text_input("Admin Password", type="password")
    if pwd == global_state["admin_password"]:
        if st.button("🚀 Reset Word"):
            global_state["current_word"] = random.choice(global_state["dictionary"]).upper()
            st.session_state.guesses = []
            st.rerun()
