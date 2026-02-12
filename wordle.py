import streamlit as st
import random
import streamlit.components.v1 as components

# --- SHARED STATE ---
@st.cache_resource
def get_global_game_state():
    return {
        "current_word": "SURGE",
        "dictionary": ["CRAWL", "STONE", "SPIRE", "FUNDS", "SURGE", "CLEAR", "BOARD", "LIGHT", "BRAIN", "WORLD"],
        "admin_password": "admin" 
    }

global_state = get_global_game_state()

st.set_page_config(page_title="Global Wordle", layout="centered")

# --- CSS FOR GRID & BACKGROUND ---
st.markdown("""
    <style>
    .stApp { background-color: #121213; color: white; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    
    .wordle-wrapper { display: flex; flex-direction: column; align-items: center; width: 100%; }
    
    /* Grid Styling - Perfect Squares */
    .grid { display: grid; grid-template-rows: repeat(6, 1fr); gap: 5px; margin-bottom: 30px; }
    .row { display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px; }
    .tile {
        width: 58px; height: 58px; border: 2px solid #3a3a3c;
        display: flex; align-items: center; justify-content: center;
        font-size: 2rem; font-weight: bold; text-transform: uppercase;
    }
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
    if 'game_over' not in st.session_state: st.session_state.game_over = False

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

    # 2. THE COMPACT KEYBOARD (Custom Component)
    # This captures clicks and sends them back to Python via st.session_state
    keyboard_code = """
    <style>
        .kb-container { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; gap: 8px; user-select: none; }
        .kb-row { display: flex; gap: 6px; width: 100%; justify-content: center; }
        .key { 
            background-color: #818384; color: white; border-radius: 4px; 
            height: 58px; min-width: 40px; flex: 1;
            display: flex; align-items: center; justify-content: center; 
            cursor: pointer; font-weight: bold; font-size: 14px; 
        }
        .key:active { background-color: #565758; }
        .key.large { flex: 1.5; padding: 0 10px; }
    </style>
    <div class="kb-container">
        <div class="kb-row">
            <div class="key" onclick="send('Q')">Q</div><div class="key" onclick="send('W')">W</div><div class="key" onclick="send('E')">E</div>
            <div class="key" onclick="send('R')">R</div><div class="key" onclick="send('T')">T</div><div class="key" onclick="send('Y')">Y']
            <div class="key" onclick="send('U')">U</div><div class="key" onclick="send('I')">I</div><div class="key" onclick="send('O')">O</div><div class="key" onclick="send('P')">P</div>
        </div>
        <div class="kb-row" style="width: 90%;">
            <div class="key" onclick="send('A')">A</div><div class="key" onclick="send('S')">S</div><div class="key" onclick="send('D')">D</div>
            <div class="key" onclick="send('F')">F</div><div class="key" onclick="send('G')">G</div><div class="key" onclick="send('H')">H</div>
            <div class="key" onclick="send('J')">J</div><div class="key" onclick="send('K')">K</div><div class="key" onclick="send('L')">L</div>
        </div>
        <div class="kb-row">
            <div class="key large" onclick="send('ENTER')">ENTER</div>
            <div class="key" onclick="send('Z')">Z</div><div class="key" onclick="send('X')">X</div><div class="key" onclick="send('C')">C</div>
            <div class="key" onclick="send('V')">V</div><div class="key" onclick="send('B')">B</div><div class="key" onclick="send('N')">N</div><div class="key" onclick="send('M')">M</div>
            <div class="key large" onclick="send('BACK')">⌫</div>
        </div>
    </div>
    <script>
        function send(val) { window.parent.postMessage({type: 'streamlit:setComponentValue', value: val}, '*'); }
    </script>
    """
    
    if not st.session_state.game_over:
        # Render the custom keyboard and capture the return value
        key_pressed = components.html(keyboard_code, height=220)
        
        # This acts as the "Event Listener"
        # Since components.html doesn't return value easily, we use a hidden button trick or query params
        # But for this simple version, let's use the standard button logic with fixed CSS:
        st.write("---")
        kb_rows = [list("QWERTYUIOP"), list("ASDFGHJKL"), ["ENTER"] + list("ZXCVBNM") + ["⌫"]]
        for row in kb_rows:
            cols = st.columns([1]*len(row))
            for i, char in enumerate(row):
                if cols[i].button(char, key=f"k_{char}", use_container_width=True):
                    if char == "ENTER":
                        if len(st.session_state.current_guess) == 5:
                            st.session_state.guesses.append(st.session_state.current_guess)
                            if st.session_state.current_guess == target_word or len(st.session_state.guesses) >= 6:
                                st.session_state.game_over = True
                            st.session_state.current_guess = ""
                    elif char == "⌫":
                        st.session_state.current_guess = st.session_state.current_guess[:-1]
                    elif len(st.session_state.current_guess) < 5:
                        st.session_state.current_guess += char
                    st.rerun()

with tab2:
    pwd = st.text_input("Admin Password", type="password")
    if pwd == global_state["admin_password"]:
        if st.button("🚀 Roll New Global Word"):
            global_state["current_word"] = random.choice(global_state["dictionary"]).upper()
            st.session_state.guesses = []
            st.session_state.game_over = False
            st.rerun()
