"""
Wordle Game Application
========================
A multiplayer Wordle game built with Streamlit.
    js = f"""
<script>
    const absent = {list(absent_letters)};
    const correct = {list(correct_letters)};
    const present = {list(present_letters)};
    const doc = window.parent.document;
    const buttons = doc.querySelectorAll('div.stButton > button');
    // 1. Color the keys
    buttons.forEach(btn => {{
        let key = btn.innerText.trim();
        if (key === '✅') key = 'ENTER';
        if (correct.includes(key)) {{
            btn.style.backgroundColor = '#538d4e';
            btn.style.color = 'white';
            btn.style.border = 'none';
        }} else if (present.includes(key)) {{
            btn.style.backgroundColor = '#b59f3b';
            btn.style.color = 'white';
            btn.style.border = 'none';
        }} else if (absent.includes(key)) {{
            btn.style.backgroundColor = '#3b3b3b';
            btn.style.color = '#777';
            btn.style.border = '1px solid #333';
        }} else {{
            btn.style.backgroundColor = '#818384';
            btn.style.color = 'white';
            btn.style.border = 'none';
        }}
    }});
    // 2. Attach Physical Keyboard Listener (A-Z, Enter, Backspace)
    // Use a global function name to avoid duplicate listeners on re-runs
    if (window.parent.wordleKeyListener) {{
        doc.removeEventListener('keydown', window.parent.wordleKeyListener);
    }}
    window.parent.wordleKeyListener = function(e) {{
        // Ignore if typing in an input field
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        let key = e.key.toUpperCase();
        if (e.key === 'Enter') key = '✅';
        if (e.key === 'Backspace') key = '⌫';
        // Find the button with the matching text
        // We search specifically in stButton containers to avoid other buttons
        const allButtons = Array.from(doc.querySelectorAll('div.stButton > button'));
        const targetBtn = allButtons.find(btn => btn.innerText.trim() === key);
        if (targetBtn) {{
            targetBtn.click();
            e.preventDefault();
        }}
    }};
    doc.addEventListener('keydown', window.parent.wordleKeyListener);
</script>
"""
    components.html(js, height=0, width=0)
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
        font-size: 30px;
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
        border-radius: 4px;
        height: 58px;          /* FORCE TALL KEYS */
        width: 100%;           /* FILL THE COLUMN */
        font-weight: bold;
        font-size: 13px;
        padding: 0;
        margin: 0;
        line-height: 58px;
    }

    /* Disabled/Absent Key Styling */
    div.stButton > button:disabled {
        background-color: #3b3b3b !important;
        color: #777 !important;
        border: 1px solid #333 !important;
        opacity: 1 !important;
        cursor: not-allowed;
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

    /* Absent/Wrong Letter Key Styling */
    div.stButton > button.absent-key {
        background-color: #3b3b3b !important;
        color: #777 !important;
        border: 1px solid #333 !important;
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
    
    /* 5. CENTERED NOTIFICATION OVERLAY */
    .centered-notification {
        position: fixed;
        display: none; /* Hide the old class just in case */
        background-color: #333;
        color: #fff;
        padding: 15px 25px;
        border-radius: 8px;
        font-weight: bold;
        z-index: 99999;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        border: 2px solid #555;
        text-align: center;
        animation: fadeOut 2.5s forwards;
    }
    
    /* 5. DEDICATED STATUS BAR (Between Grid and Keyboard) */
    .status-bar-wrapper {
        height: 60px; /* Fixed height to preserve layout */
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
    }
    
    .status-bar {
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        color: white;
        width: 100%;
        max-width: 400px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    
    .status-win { background-color: #538d4e; border: 2px solid #538d4e; }
    .status-loss { background-color: #cf6679; border: 2px solid #cf6679; } /* Red for loss */
    .status-error { background-color: #cf6679; border: 2px solid #cf6679; } /* Red for invalid */
    
    @keyframes fadeOut {
        0% { opacity: 1; margin-top: 0px; }
        70% { opacity: 1; margin-top: 0px; }
        100% { opacity: 0; margin-top: -20px; visibility: hidden; }
    }
    
    /* 6. MOBILE RESPONSIVE FIXES - Prevent keyboard from stacking */
    @media only screen and (max-width: 768px) {
        /* Force columns to stay horizontal on mobile */
        [data-testid="stHorizontalBlock"] {
            flex-wrap: nowrap !important;
            gap: 3px !important; /* Reduce gap on mobile for better fit */
        }
        
        /* Adjust button size for mobile */
        div.stButton > button {
            height: 48px !important; /* Maintain good touch target height */
            font-size: 11px !important; /* Smaller font */
            min-width: 30px; /* Minimum width for touch targets */
            max-width: 45px !important; /* Prevent buttons from becoming too wide on tablets */
        }
        
        /* Adjust tile size for mobile */
        .tile {
            width: 42px !important;
            height: 42px !important;
            font-size: 20px !important;
        }
    }
    
    /* Extra small screens (phones in portrait) */
    @media only screen and (max-width: 480px) {
        [data-testid="stHorizontalBlock"] {
            gap: 2px !important; /* Even tighter gap for very small screens */
        }
        
        div.stButton > button {
            height: 40px !important;
            font-size: 10px !important;
            min-width: 20px;
            max-width: 24px !important;
            padding: 0 1px;
        }
        .tile {
            width: 24px !important;
            height: 24px !important;
            font-size: 13px !important;
            margin: 0 1px !important;
        }
        .row {
            gap: 1px !important;
        }
        .grid {
            gap: 1px !important;
        }
        .wordle-wrapper, .grid, .row {
            max-width: 100vw !important;
            width: 100vw !important;
            overflow-x: hidden !important;
        }

            /* Force keyboard columns to shrink on mobile */
            [data-testid="stHorizontalBlock"] > div {
                flex-basis: 0 !important;
                min-width: 0 !important;
                max-width: 1fr !important;
            }
            .wordle-wrapper, .grid, .row {
                max-width: 100vw !important;
                width: 100vw !important;
                overflow-x: hidden !important;
            }
    }
    </style>

""", unsafe_allow_html=True)

# --- APP LOGIC ---
st.title("🌎 Global Wordle")

tab1, tab2 = st.tabs(["🎮 Play Game", "🔒 Admin Panel"])

with tab1:
    target_word = global_state["current_word"]
    
    # Check if the global word has changed since our last session state. 
    # If so, reset the game for this user.
    if 'last_target_word' not in st.session_state:
        st.session_state.last_target_word = target_word
        
    if st.session_state.last_target_word != target_word:
        st.session_state.guesses = []
        st.session_state.current_guess = ""
        st.session_state.game_over = False
        st.session_state.game_result = None
        st.session_state.last_target_word = target_word
        st.rerun()
    
    if 'current_guess' not in st.session_state: st.session_state.current_guess = ""
    if 'guesses' not in st.session_state: st.session_state.guesses = []
    if 'game_over' not in st.session_state: st.session_state.game_over = False
    if 'game_result' not in st.session_state: st.session_state.game_result = None

    # 1. RENDER THE GRID
    grid_html = '<div class="wordle-wrapper"><div class="grid">'
    
    for r in range(6):
        grid_html += '<div class="row">'
        
        # Pre-calculate row status if it's a past guess to handle duplicate letters correctly
        row_colors = ["empty"] * 5
        if r < len(st.session_state.guesses):
            guess_word = st.session_state.guesses[r]
            
            # 1. Mark Greens first
            target_chars_count = {}
            for char in target_word:
                target_chars_count[char] = target_chars_count.get(char, 0) + 1
            
            # First pass: Greens
            for c in range(5):
                letter = guess_word[c]
                if letter == target_word[c]:
                    row_colors[c] = "correct"
                    target_chars_count[letter] -= 1
            
            # Second pass: Yellows (only if count > 0)
            for c in range(5):
                letter = guess_word[c]
                if row_colors[c] == "empty": # If not green
                    if letter in target_chars_count and target_chars_count[letter] > 0:
                        row_colors[c] = "present"
                        target_chars_count[letter] -= 1
                    else:
                        row_colors[c] = "absent"

        for c in range(5):
            char, status = "", "empty"
            # Previous Guesses
            if r < len(st.session_state.guesses):
                char = st.session_state.guesses[r][c]
                status = row_colors[c]
            # Current Typing Row
            elif r == len(st.session_state.guesses) and c < len(st.session_state.current_guess):
                char = st.session_state.current_guess[c]
                status = "typing"
            
            grid_html += f'<div class="tile {status}">{char}</div>'
        grid_html += '</div>'
    grid_html += '</div></div>'
    
    # Calculate letter statuses for keyboard styling
    absent_letters = set()
    correct_letters = set()
    present_letters = set()

    for guess in st.session_state.guesses:
        for i, char in enumerate(guess):
            if char == target_word[i]:
                correct_letters.add(char)
            elif char in target_word:
                present_letters.add(char)
            else:
                absent_letters.add(char)
    
    # Ensure correct (green) takes precedence over present (yellow) in our sets logic if needed,
    # though the JS logic handles precedence by checking 'correct' first.
    # We can clean up 'present' to remove letters that are already 'correct' to be safe.
    present_letters = present_letters - correct_letters

    # Show Notification if present
    st.markdown(grid_html, unsafe_allow_html=True)

    # --- DEDICATED STATUS BAR ---
    # Determine the message and style based on game state
    status_msg = ""
    status_class = ""
    
    if st.session_state.game_over:
        if st.session_state.game_result == "WIN":
            status_msg = f"🎉 You guessed it! The word was {target_word}"
            status_class = "status-win"
        else:
            status_msg = f"💀 Game Over! The word was {target_word}"
            status_class = "status-loss"
    elif 'notification' in st.session_state and st.session_state.notification:
        status_msg = st.session_state.notification
        status_class = "status-error"
        st.session_state.notification = None # Clear after render
        
    # Render the status bar (invisible if empty)
    if status_msg:
        st.markdown(f'<div class="status-bar-wrapper"><div class="status-bar {status_class}">{status_msg}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-bar-wrapper"></div>', unsafe_allow_html=True)
        
    # No New Game button here. Game resets when admin changes word or reloads.

    # 2. KEYBOARD LOGIC
    def press(key):
        if st.session_state.game_over:
            st.toast("Game is over! Wait for admin to change word.")
            return

        if key == "ENTER":
            if len(st.session_state.current_guess) == 5:
                if st.session_state.current_guess in global_state["dictionary2"]:
                    st.session_state.guesses.append(st.session_state.current_guess)
                    st.session_state.current_guess = ""
                    
                    # Check Win/Loss conditions immediately after guess
                    if st.session_state.guesses[-1] == target_word:
                        st.session_state.game_over = True
                        st.session_state.game_result = "WIN"
                    elif len(st.session_state.guesses) >= 6:
                        st.session_state.game_over = True
                        st.session_state.game_result = "LOSS"
                    
                    st.rerun()
                else:
                    # Show centered notification
                    st.session_state.notification = "⛔ English Only! Not in dictionary"
                    st.rerun()
        elif key == "⌫":
            st.session_state.current_guess = st.session_state.current_guess[:-1]
            st.rerun()
        elif len(st.session_state.current_guess) < 5:
            st.session_state.current_guess += key
            st.rerun()
        """else:
             # Look & Feel: If they try to type > 5 chars
             st.toast("Word is full! Press ENTER or Backspace.")"""

    # 3. RENDER KEYBOARD (Precise Columns)
    
    # Row 1: Q-P (10 Keys)
    keys1 = "QWERTYUIOP"
    c1 = st.columns(10)
    for idx, k in enumerate(keys1):
        if c1[idx].button(k, key=f"btn_{k}", use_container_width=True):
            press(k)

    # Row 2: A-L (9 Keys) - Centered with Spacers
    keys2 = "ASDFGHJKL"
    c2 = st.columns([0.5] + [1]*9 + [0.5]) 
    for idx, k in enumerate(keys2):
        if c2[idx+1].button(k, key=f"btn_{k}", use_container_width=True):
            press(k)

    # Row 3: Validate (checkmark) - Z-M - Backspace
    keys3 = "ZXCVBNM"
    c3 = st.columns([1.2] + [1]*7 + [1.2]) 
    # Validate Button (Checkmark)
    if c3[0].button("✅", key="enter", use_container_width=True):
        press("ENTER")
    for idx, k in enumerate(keys3):
        if c3[idx+1].button(k, key=f"btn_{k}", use_container_width=True):
            press(k)
    # Backspace Button
    if c3[8].button("⌫", key="back", use_container_width=True):
        press("⌫")

    # JavaScript to style keyboard keys based on game state and handle physical keyboard input
    js = f"""
    <script>
        const absent = {list(absent_letters)};
        const correct = {list(correct_letters)};
        const present = {list(present_letters)};
        
        const doc = window.parent.document;
        const buttons = doc.querySelectorAll('div.stButton > button');
        // 1. Color the keys
        buttons.forEach(btn => {
            let key = btn.innerText.trim();
            if (key === '✅') key = 'ENTER';
            if (correct.includes(key)) {
                btn.style.backgroundColor = '#538d4e';
                btn.style.color = 'white';
                btn.style.border = 'none';
            } else if (present.includes(key)) {
                btn.style.backgroundColor = '#b59f3b';
                btn.style.color = 'white';
                btn.style.border = 'none';
            } else if (absent.includes(key)) {
                btn.style.backgroundColor = '#3b3b3b';
                btn.style.color = '#777';
                btn.style.border = '1px solid #333';
            } else {
                btn.style.backgroundColor = '#818384';
                btn.style.color = 'white';
                btn.style.border = 'none';
            }
        });

        // 2. Attach Physical Keyboard Listener (A-Z, Enter, Backspace)
        // Use a global function name to avoid duplicate listeners on re-runs
        if (window.parent.wordleKeyListener) {{
            doc.removeEventListener('keydown', window.parent.wordleKeyListener);
        }}
        
        window.parent.wordleKeyListener = function(e) {{
            // Ignore if typing in an input field
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
            
            let key = e.key.toUpperCase();
            if (e.key === 'Enter') key = '✅';
            if (e.key === 'Backspace') key = '⌫';
            
            // Find the button with the matching text
            // We search specifically in stButton containers to avoid other buttons
            const allButtons = Array.from(doc.querySelectorAll('div.stButton > button'));
            const targetBtn = allButtons.find(btn => btn.innerText.trim() === key);
            
            if (targetBtn) {{
                targetBtn.click();
                e.preventDefault();
            }}
        }};
        
        doc.addEventListener('keydown', window.parent.wordleKeyListener);
    </script>
    """
    components.html(js, height=0, width=0)

with tab2:
    st.header("🔒 Admin Controls")
    pwd = st.text_input("Enter Admin Password", type="password")
    
    if pwd == global_state["admin_password"]:
        st.success("✅ Access Granted")
        st.markdown("---")
        
        # Display Current Word
        if 'show_word' not in st.session_state: st.session_state.show_word = False
        
        col_metric, col_toggle = st.columns([3, 1])
        with col_metric:
            display_word = global_state["current_word"] if st.session_state.show_word else "*****"
            st.metric(label="Current Target Word", value=display_word)
        with col_toggle:
            st.write("") # Spacer
            if st.button("👁️ Toggle", key="toggle_word"):
                st.session_state.show_word = not st.session_state.show_word
                st.rerun()
        
        st.markdown("### Actions")
        c_p1, c_p2 = st.columns(2)
        
        with c_p1:
            if st.button("🎲 Shuffle Word", use_container_width=True):
                global_state["current_word"] = random.choice(global_state["dictionary"]).upper()
                st.session_state.guesses = []
                st.session_state.game_over = False
                st.session_state.game_result = None
                st.toast(f"Word shuffled! New word is: {global_state['current_word']}")
                st.rerun()
                
        with c_p2:
            custom_word = st.text_input("Set Custom Word (5 Letters)", max_chars=5).upper()
            if st.button("💾 Set Word", use_container_width=True):
                if len(custom_word) == 5 and custom_word.isalpha():
                    global_state["current_word"] = custom_word
                    st.session_state.guesses = []
                    st.session_state.current_guess = ""
                    st.session_state.game_over = False
                    st.session_state.game_result = None
                    st.toast(f"Word updated to: {custom_word}")
                    st.rerun()
                else:
                    st.error("Word must be exactly 5 letters.")
                    
        st.markdown("---")
        if st.button("⚠️ Force Reset Game State (Debug)", type="primary"):
            for key in ['guesses', 'current_guess', 'game_over', 'game_result', 'last_target_word']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
    elif pwd:
        st.error("Incorrect Password")
