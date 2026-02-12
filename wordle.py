import streamlit as st
import random

# --- CONFIGURATION & SHARED STATE ---
# We use st.cache_resource to share the "Game Master" data across all users
@st.cache_resource
def get_global_game_state():
    return {
        "current_word": "READY",
        "dictionary": ["STEAM", "WORDS", "APPLE", "CLEAR", "PYTHON", "SPACE", "BOARD"], # Add more!
        "admin_password": "admin" 
    }

global_state = get_global_game_state()

def reset_global_word():
    global_state["current_word"] = random.choice(global_state["dictionary"]).upper()

# --- APP LAYOUT ---
st.set_page_config(page_title="Global Wordle", layout="centered")
st.title("🌎 Global Wordle")
st.write("Everyone is playing the same word right now!")

# --- TABS: GAME & ADMIN ---
tab1, tab2 = st.tabs(["🎮 Play Game", "🔒 Admin Panel"])

with tab1:
    target_word = global_state["current_word"]
    
    # Initialize user-specific session state (personal progress)
    if "guesses" not in st.session_state or st.session_state.get("last_word") != target_word:
        st.session_state.guesses = []
        st.session_state.last_word = target_word
        st.session_state.game_over = False

    # Input for guess
    if not st.session_state.game_over:
        user_guess = st.text_input("Enter a 5-letter word:", max_chars=5).upper()
        if st.button("Submit Guess"):
            if len(user_guess) == 5:
                st.session_state.guesses.append(user_guess)
                if user_guess == target_word:
                    st.success("🎉 You found it!")
                    st.session_state.game_over = True
                elif len(st.session_state.guesses) >= 6:
                    st.error(f"Game Over! The word was {target_word}")
                    st.session_state.game_over = True
            else:
                st.warning("Please enter exactly 5 letters.")

    # Display the Grid
    for guess in st.session_state.guesses:
        cols = st.columns(5)
        for i, letter in enumerate(guess):
            if letter == target_word[i]:
                cols[i].markdown(f"<div style='background-color:#6aaa64; color:white; text-align:center; padding:10px; border-radius:5px;'>{letter}</div>", unsafe_allow_html=True)
            elif letter in target_word:
                cols[i].markdown(f"<div style='background-color:#c9b458; color:white; text-align:center; padding:10px; border-radius:5px;'>{letter}</div>", unsafe_allow_html=True)
            else:
                cols[i].markdown(f"<div style='background-color:#787c7e; color:white; text-align:center; padding:10px; border-radius:5px;'>{letter}</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Admin Controls")
    pwd = st.text_input("Enter Admin Password", type="password")
    
    if pwd == global_state["admin_password"]:
        if st.button("🚀 Roll New Global Word"):
            reset_global_word()
            st.rerun()
        st.write(f"**Current active word:** {global_state['current_word']}")
    elif pwd != "":
        st.error("Incorrect Password")
