import streamlit as st
import random

# --- CONFIGURATION & STATE ---
@st.cache_resource
def get_global_game_state():
    return {
        "current_word": "SURGE",
        "dictionary": ["CRAWL", "STONE", "SPIRE", "FUNDS", "SURGE", "CLEAR", "BOARD", "LIGHT"],
        "admin_password": "admin" 
    }

global_state = get_global_game_state()

st.set_page_config(page_title="Global Wordle", layout="centered")

# --- CSS: THE ENGINE FOR THE VISUALS ---
st.markdown("""
    <style>
    /* 1. MAIN BACKGROUND - Dark Charcoal */
    .stApp {
        background-color: #121213;
        color: white;
    }
    
    /* Hide Streamlit elements we don't need */
    header, footer {visibility: hidden;}
    
    /* 2. THE GRID TILES */
    .tile {
        width: 62px;
        height: 62px;
        border: 2px solid #3a3a3c;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 50px;
        font-weight: bold;
        text-transform: uppercase;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        user-select: none;
    }
    
    /* TILE COLORS */
    .correct { background-color: #538d4e !important; border-color: #538d4e !important; }
    .present { background-color: #b59f3b !important; border-color: #b59f3b !important; }
    .absent  { background-color: #3a3a3c !important; border-color: #3a3a3c !important; }
    .empty   { background-color: transparent; }
    .typing  { border-color: #565758 !important; } /* Highlight current box */

    /* 3. KEYBOARD BUTTON STYLING (The most important part) */
    
    /* Target ALL buttons inside the columns */
    div.stButton > button {
        background-color: #818384;
        color: white;
        border: none;
        border-radius: 8px;
        height: 58px;          /* FORCE TALL KEYS */
        width: 100%;           /* FILL THE COLUMN */
        font-weight: bold;
        font-size: 30px;
        padding: 0;
        margin: 0;
        line-height: 58px;
    }

    /* Hover State */
    div.stButton > button:hover {
        background-color: #565758;
        color: white;
        border: none;
    }
    
    /* Click/Active State */
    div.stButton > button:active, div.stButton > button:focus {
        background-color: #565758;
        color: white;
        border: none;
        box-shadow: none;
    }

    /* 4. LAYOUT TIGHTENING (Removing the Gaps) */
    
    /* Squeeze the columns together */
    [data-testid="stHorizontalBlock"] {
        gap: 6px !important; /* Matches strict 6px gap from Wordle */
        align-items: center;
    }
    
    /* Remove padding inside columns */
    [data-testid="column"] {
        padding: 0px !important;
        min-width: 0px !important;
        flex: 1;
    }
    
    /* Center the Grid Wrapper */
    .wordle-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
    }
    .grid {
        display: grid;
        grid-template-rows: repeat(6, 1fr);
        gap: 5px;
    }
    .row {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP LOGIC ---
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
            char, status = "", "empty"
            # Previous Guesses
            if r < len(st.session_state.guesses):
                char = st.session_state.guesses[r][c]
                if char == target_word[c]: status = "correct"
                elif char in target_word: status = "present"
                else: status = "absent"
            # Current Typing Row
            elif r == len(st.session_state.guesses) and c < len(st.session_state.current_guess):
                char = st.session_state.current_guess[c]
                status = "typing"
            
            grid_html += f'<div class="tile {status}">{char}</div>'
        grid_html += '</div>'
    grid_html += '</div></div>'
    st.markdown(grid_html, unsafe_allow_html=True)

    # 2. KEYBOARD LOGIC
    def press(key):
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

    # 3. RENDER KEYBOARD (Precise Columns)
    
    # Row 1: Q-P (10 Keys) - Standard spacing
    keys1 = "QWERTYUIOP"
    c1 = st.columns(10)
    for idx, k in enumerate(keys1):
        if c1[idx].button(k, key=f"btn_{k}", use_container_width=True):
            press(k)

    # Row 2: A-L (9 Keys) - Centered with Spacers
    keys2 = "ASDFGHJKL"
    # [0.5 spacer] [1] [1] ... [0.5 spacer]
    c2 = st.columns([0.5] + [1]*9 + [0.5]) 
    for idx, k in enumerate(keys2):
        if c2[idx+1].button(k, key=f"btn_{k}", use_container_width=True):
            press(k)

    # Row 3: Enter - Z-M - Backspace
    keys3 = "ZXCVBNM"
    # Enter is 1.5x, Letters are 1x, Backspace is 1.5x
    c3 = st.columns([1.5] + [1]*7 + [1.5])
    
    if c3[0].button("ENTER", key="enter", use_container_width=True):
        press("ENTER")
        
    for idx, k in enumerate(keys3):
        if c3[idx+1].button(k, key=f"btn_{k}", use_container_width=True):
            press(k)
            
    if c3[8].button("⌫", key="back", use_container_width=True):
        press("⌫")

with tab2:
    pwd = st.text_input("Admin Password", type="password")
    if pwd == global_state["admin_password"]:
        if st.button("🚀 New Word"):
            global_state["current_word"] = random.choice(global_state["dictionary"]).upper()
            st.session_state.guesses = []
            st.rerun()
        st.info(f"Current Word: {global_state['current_word']}")
