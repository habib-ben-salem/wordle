import streamlit as st
import random

# --- CONFIGURATION & SHARED STATE ---
@st.cache_resource
def get_global_game_state():
    return {
        "current_word": "SURGE",
        "dictionary": ["CRAWL", "STONE", "SPIRE", "FUNDS", "SURGE", "CLEAR", "BOARD", "LIGHT", "FLAME"],
        "admin_password": "admin" 
    }

global_state = get_global_game_state()

def reset_global_word():
    global_state["current_word"] = random.choice(global_state["dictionary"]).upper()

# --- STYLING (The "Dark Mode" Graphics) ---
st.set_page_config(page_title="Global Wordle", layout="centered")

st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #121213;
        color: white;
    }
    
    /* Wordle Tile Styling */
    .wordle-tile {
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        border: 2px solid #3a3a3c;
        margin: 3px;
        text-transform: uppercase;
        border-radius: 2px;
    }
    
    /* Keyboard Styling */
    .keys {
        display: flex;
        justify-content: center;
        margin: 2px;
        gap: 4px;
    }
    .key-btn {
        background-color: #818384;
        color: white;
        padding: 10px;
        border-radius: 4px;
        min-width: 35px;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
    }
    
    /* Center the grid */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LAYOUT ---
st.title("🌎 Global Wordle")

tab1, tab2 = st.tabs(["🎮 Play Game", "🔒 Admin Panel"])

with tab1:
    target_word = global_state["current_word"]
    
    if "guesses" not in st.session_state or st.session_state.get("last_word") != target_word:
        st.session_state.guesses = []
        st.session_state.last_word = target_word
        st.session_state.game_over = False
        st.session_state.used_letters = {} # Tracks keyboard colors

    # Display the Grid (Always 6 rows)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    for row_idx in range(6):
        cols = st.columns([1,1,1,1,1,3,1,1,1,1,1])[2:7] # Centering hack
        
        if row_idx < len(st.session_state.guesses):
            guess = st.session_state.guesses[row_idx]
            for i, letter in enumerate(guess):
                bg_color = "#3a3a3c" # Gray (Default)
                if letter == target_word[i]:
                    bg_color = "#538d4e" # Green
                    st.session_state.used_letters[letter] = "#538d4e"
                elif letter in target_word:
                    bg_color = "#b59f3b" # Yellow
                    if st.session_state.used_letters.get(letter) != "#538d4e":
                        st.session_state.used_letters[letter] = "#b59f3b"
                else:
                    if letter not in st.session_state.used_letters:
                        st.session_state.used_letters[letter] = "#3a3a3c"

                cols[i].markdown(f"<div class='wordle-tile' style='background-color:{bg_color}; border:none;'>{letter}</div>", unsafe_allow_html=True)
        else:
            # Empty rows
            for i in range(5):
                cols[i].markdown(f"<div class='wordle-tile'></div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Input Area
    if not st.session_state.game_over:
        with st.form("guess_form", clear_on_submit=True):
            user_guess = st.text_input("Enter a 5-letter word:", max_chars=5).upper()
            submit = st.form_submit_button("Submit Guess")
            
            if submit:
                if len(user_guess) == 5:
                    st.session_state.guesses.append(user_guess)
                    if user_guess == target_word or len(st.session_state.guesses) >= 6:
                        st.session_state.game_over = True
                    st.rerun()
    
    if st.session_state.game_over:
        if st.session_state.guesses[-1] == target_word:
            st.success(f"Excellent! The word was {target_word}")
        else:
            st.error(f"Game Over. The word was {target_word}")
        if st.button("New Game (Local Reset)"):
            st.session_state.guesses = []
            st.session_state.game_over = False
            st.rerun()

    # --- VIRTUAL KEYBOARD ---
    st.write("---")
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    for row in rows:
        cols = st.columns(len(row))
        for i, char in enumerate(row):
            color = st.session_state.used_letters.get(char, "#818384")
            cols[i].markdown(f"<div class='key-btn' style='background-color:{color};'>{char}</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Admin Control")
    pwd = st.text_input("Admin Password", type="password")
    if pwd == global_state["admin_password"]:
        if st.button("🚀 Set New Global Word for Everyone"):
            reset_global_word()
            st.success("New word selected!")
            st.rerun()
        st.info(f"The active word is currently: {global_state['current_word']}")
