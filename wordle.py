import streamlit as st
import random

# --- CONFIGURATION & STATE ---
st.set_page_config(page_title="Global Wordle", layout="centered")

@st.cache_resource
def get_global_state():
    return {
        "target_word": "SURGE",
        # A small dictionary for demonstration
        "dictionary": ["CRAWL", "STONE", "SPIRE", "FUNDS", "SURGE", "CLEAR", "BOARD", "LIGHT", "POWER", "THINK"],
        "admin_password": "admin"
    }

global_state = get_global_state()

# Initialize session state
if 'guesses' not in st.session_state:
    st.session_state.guesses = []
if 'current_guess' not in st.session_state:
    st.session_state.current_guess = ""
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
# Track the state of each letter key: 'correct', 'present', 'absent', or None
if 'key_states' not in st.session_state:
    st.session_state.key_states = {}

# --- CSS: THE CORE OF THE VISUAL RECREATION ---
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #121213; /* Dark charcoal background */
        color: white;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    header, footer, [data-testid="stHeader"] { visibility: hidden; } # Hide Streamlit UI

    /* Main Container to center everything */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 20px;
    }

    /* --- GRID STYLES --- */
    .grid {
        display: grid;
        grid-template-rows: repeat(6, 1fr);
        gap: 5px; /* Precise gap between tiles */
        margin-bottom: 30px;
    }
    .row {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 5px;
    }
    .tile {
        width: 62px;
        height: 62px;
        border: 2px solid #3a3a3c; /* Dark grey border for empty */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        user-select: none;
    }
    /* Tile Color States */
    .correct { background-color: #538d4e !important; border: none !important; }
    .present { background-color: #b59f3b !important; border: none !important; }
    .absent { background-color: #3a3a3c !important; border: none !important; }
    .typing { border-color: #818384 !important; } /* Lighter border when typing */

    /* --- KEYBOARD STYLES --- */
    /* Override Streamlit button styles to look like keys */
    div.stButton > button {
        background-color: #818384; /* Default key color */
        color: white;
        border: none;
        border-radius: 4px; /* Rounded corners */
        height: 58px; /* Fixed height for all keys */
        width: 100%;
        font-weight: bold;
        font-size: 14px;
        padding: 0;
        margin: 0;
        line-height: 58px;
    }
    div.stButton > button:hover { background-color: #565758; }
    div.stButton > button:active, div.stButton > button:focus {
        background-color: #565758;
        box-shadow: none;
        border: none;
    }

    /* Dynamic Key Colors based on game state */
    .key-correct div.stButton > button { background-color: #538d4e !important; }
    .key-present div.stButton > button { background-color: #b59f3b !important; }
    .key-absent div.stButton > button { background-color: #3a3a3c !important; }

    /* Layout Tweaks for Keyboard Rows */
    [data-testid="stHorizontalBlock"] {
        gap: 6px !important; /* Exact gap between keys */
        justify-content: center;
    }
    /* Ensure columns don't add extra padding */
    [data-testid="column"] {
        padding: 0 !important;
        min-width: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- GAME LOGIC ---
def update_key_states(guess):
    target = global_state["target_word"]
    for i, char in enumerate(guess):
        if char == target[i]:
            st.session_state.key_states[char] = 'correct'
        elif char in target:
            # Only mark as present if it's not already marked as correct
            if st.session_state.key_states.get(char) != 'correct':
                st.session_state.key_states[char] = 'present'
        else:
            # Only mark as absent if it has no other status
            if char not in st.session_state.key_states:
                st.session_state.key_states[char] = 'absent'

def handle_press(key):
    if st.session_state.game_over: return

    if key == "ENTER":
        if len(st.session_state.current_guess) == 5:
            guess = st.session_state.current_guess
            st.session_state.guesses.append(guess)
            update_key_states(guess)
            st.session_state.current_guess = ""
            if guess == global_state["target_word"] or len(st.session_state.guesses) == 6:
                st.session_state.game_over = True
    elif key == "⌫":
        st.session_state.current_guess = st.session_state.current_guess[:-1]
    elif len(st.session_state.current_guess) < 5:
        st.session_state.current_guess += key
    st.rerun()

# --- MAIN APP LAYOUT ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 1. RENDER THE GRID (Using HTML/CSS for precision)
grid_html = '<div class="grid">'
for r in range(6):
    grid_html += '<div class="row">'
    for c in range(5):
        char = ""
        status = ""
        # Completed guesses
        if r < len(st.session_state.guesses):
            char = st.session_state.guesses[r][c]
            if char == global_state["target_word"][c]: status = "correct"
            elif char in global_state["target_word"]: status = "present"
            else: status = "absent"
        # Current typing row
        elif r == len(st.session_state.guesses) and c < len(st.session_state.current_guess):
            char = st.session_state.current_guess[c]
            status = "typing"
        
        grid_html += f'<div class="tile {status}">{char}</div>'
    grid_html += '</div>'
grid_html += '</div>'
st.markdown(grid_html, unsafe_allow_html=True)

# 2. RENDER THE KEYBOARD (Using st.columns with custom CSS classes)
rows = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    ["ENTER"] + list("ZXCVBNM") + ["⌫"]
]

for i, row_keys in enumerate(rows):
    # Define column ratios for precise layout
    if i == 0: # Q-P
        cols = st.columns(10)
    elif i == 1: # A-L (Centered with spacers)
        cols = st.columns([0.5] + [1]*9 + [0.5])
        row_keys = [""] + list(row_keys) + [""] # Add dummy keys for spacers
    else: # Enter-M-Back
        cols = st.columns([1.5] + [1]*7 + [1.5]) # Wider outer keys

    for j, key_char in enumerate(row_keys):
        if key_char == "": continue # Skip spacers

        # Determine key style based on game state
        key_style = ""
        state = st.session_state.key_states.get(key_char)
        if state: key_style = f"key-{state}"
        
        # Use a container to apply the color style to the button inside
        with cols[j]:
            st.markdown(f'<div class="{key_style}">', unsafe_allow_html=True)
            if st.button(key_char, key=f"btn_{i}_{j}"):
                handle_press(key_char)
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # End main-container
