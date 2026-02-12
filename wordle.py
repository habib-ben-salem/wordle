import streamlit as st
import random

# --- CONFIGURATION & STATE ---
@st.cache_resource
def get_global_game_state():
    return {
        "current_word": "SURGE",
        "dictionary": ["MANGY", "CALLS", "ALOUD", "REALM", "BLUER", "DWELL", "FIVES", "STICK", "SPRAY", "OVERT", "COUPE", "THINS", "CHUTE", "DRYER", "REEKS", "GUMBO", "HELMS", "RIGID", "GLADE", "SAPPY", "PHOTO", "LAMED", "SHIRT", "UNTIL", "MEALY", "PIERS", "SHADY", "FARMS", "SWISS", "RABID", "TINGS", "ROYAL", "SKULK", "SCENT", "PRIES", "BOULE", "NODES", "TRASH", "EERIE", "SIRES", "GRAFT", "INBOX", "BIOME", "AMPLE", "SIGNS", "BRUSH", "LEVEL", "FLUID", "SWIFT", "FIRES", "SUAVE", "TROPE", "DRYLY", "KNOWS", "VISIT", "SCARE", "HERDS", "RESIN", "SLATS", "THING", "SMITH", "STALK", "FLOOD", "SLOTH", "PLAID", "WEARY", "BARGE", "ANKLE", "SLIMY", "RAGES", "BULLY", "WINCE", "SHEAR", "BUTCH", "DUMPY", "LOOMS", "RAYON", "MOODS", "HEADY", "PASTS", "HOUND", "COPSE", "MARES", "BROWN", "SPINE", "LOUSY", "FELLA", "CURRY", "DUTCH", "BLADE", "DULLY", "STIFF", "TWILL", "MINES", "GRIMY", "THEIR", "HOODS", "WORRY", "STENT", "FLOOR", "OUTDO", "ABATE", "LUNGE", "SPARK", "PHONY", "LOOPS", "VIPER", "BELTS", "SWORE", "EAVES", "BITTY", "CRUDE", "BULGE", "SALES", "OATHS", "SKIED", "SECTS", "GUIDE", "AMEND", "SMASH", "PESTO", "YEAST", "RAISE", "MOANS", "STRUT", "PACER", "RUDER", "EXILE", "NOMAD", "LEDGE", "PRIZE", "CLEAR", "MAYOR", "SUMAC", "WIDEN", "LIVES", "STRAW", "GNASH", "TITLE", "FRIES", "BABES", "CLOVE", "DOWDY", "RITES", "CAMEL", "HATER", "MOVES", "WRITE", "BOUGH", "QUASH", "BRAVE", "SLEPT", "LOWED", "STEED", "FLOUT", "QUITE", "VIRUS", "GHOST", "ABACK", "OUGHT", "DUMMY", "YIELD", "COYLY", "ALOFT", "BULKY", "DRONE", "RAILS", "DEARY", "MACHO", "HEART", "PLODS", "FOXES", "BINGE", "TUBER", "PANSY", "WELLS", "TELLS", "BEGUN", "PEPPY", "UPSET", "HEDGE", "GUMMY", "DRESS", "ERODE", "OVOID", "FLESH", "LAWNS", "TOPIC", "PATIO", "SWOOP", "ANNUL", "HEFTY", "MADAM", "IMBUE", "OVARY", "LURCH", "WOWED", "FEAST", "WIPES", "TRUCE", "ROTTE", "PUDGY", "FOIST", "GULCH", "SEALS", "SEVEN", "OOZED", "RETRO", "VAPOR", "PARKS", "EATER", "LATEX", "UNZIP", "FEARS", "PERKY", "SEMEN", "ELITE", "SOCKS", "CABLE", "LUMPY", "PEEKS", "STOOP", "TALKS", "CIVIC", "STARE", "PANEL", "NEEDS", "KNACK", "ENTRY", "TAMES", "JUROR", "SNAIL", "QUITS", "VERSO", "KNAVE", "HUNCH", "WOKEN", "CROWN", "FILLY", "HOURS", "REEDY", "HOUSE", "RAKED", "DROOP", "CELEB", "PESTS", "STOLE", "SATIN", "BATCH", "SPIKE", "DEVIL", "TAWNY", "TOUCH", "SNIFF", "CROOK", "INKED", "IONIC", "MINIM", "BRIAR", "ROOMY", "TOOLS", "REVUE", "HORNS", "NEWLY", "ORBIT", "ZEBRA", "CEDAR", "RIVET", "SLINK", "RUMOR", "HADST", "WHALE", "DIZZY", "MODEM", "CHAPS", "BASIL", "SHARE", "SEMIS", "SEVER", "FABLE", "PLIED", "COPRA", "SLEEP", "FLASH", "PAYER", "FUNKY", "HEIST", "SPOUT", "CHAFE", "GANGS", "LOCKS", "LONER", "GRATE", "JUMPY", "PLANT", "MORAL", "MUFFS", "REINS", "PLATE", "ASPEN", "MOWED", "TOURS", "BEAST", "CHEAP", "MEDIC", "SEWER", "PETTY", "PRIMP", "ADMIT", "APART", "STORE", "CRISP", "FLIES", "FAUNA", "FILMS", "BEZEL", "LOSER", "AMITY", "TONIC", "MOATS", "MOURN", "ITEMS", "FRIAR", "RANKS", "THREE", "SEGUE", "CAPUT", "MANGA", "AWAIT", "SKUNK", "MODES", "NAMES", "SONIC", "URINE", "GAINS", "GUILT", "PRIMA", "WANTS", "STUCK", "PUMPS", "ONSET", "START", "FARTS", "FEMUR", "HOSTS", "LUCKY", "LINKS", "APTLY", "CHINA", "WAIST", "DOLOR", "GLACE", "FERRY", "SPICE", "TROOP", "ABHOR", "STOVE", "ESTER", "PACES", "LODGE", "CORDS", "WEIGH", "NERVE", "PARKA", "DRANK", "SHAME", "OCEAN", "TUMMY", "NOVEL", "ROSIN", "FARED", "COMES", "ESSAY", "BASIN", "STACK", "SNOWY", "BEAMY", "AUGUR", "ACORN", "SCALP", "BOOTY", "NAPPY", "BLAME", "BLIND", "ACRID", "TANKS", "TARPS", "CANON", "WOULD", "GROUT", "BLOOD", "CARGO", "TROUT", "FRITZ", "RINGS", "FANNY", "SAMBA", "HOARD", "WARDS", "SISSY", "SETUP", "SHRUG", "PALSY", "SINCE", "LOYAL", "LIONS", "FLEET", "BADGE", "FATED", "PHONE", "HERBS", "MAMBO", "VERBS", "ABBOT", "PROPS", "ADEPT", "TRAIN", "BRINE", "WAXED", "PEERS", "SULKY", "NICER", "GRANT", "CLING", "STAMP", "ETHIC", "ALLOW", "FILTH", "MOCKS", "SLAVE", "SERVO", "RADII", "TRIPE", "NOOSE", "GIVER", "CLOTH", "APRON", "REFER", "WREST", "TIBIA", "THIRD", "NEWER", "EGGED", "DREAM", "EARTH", "PURSE", "SCENE", "SUITE", "LOCAL", "CHARM", "LITER", "GILDS", "HUMOR", "PROSE", "TUTOR", "SHALL", "FRIED", "BREED", "NOBLE", "GIVEN", "KNOTS", "STAGE", "MEDIA", "DYING", "DARED", "DEBUG", "ADAPT", "BLUNT", "CABAL", "LOGIN", "ALIBI", "BOTCH", "LINGO", "CHEFS", "WRACK", "HOPED", "REBUT", "FLUME", "LAYER", "WHIRL", "ARENA", "VALUE", "SUITS", "ANGER", "THIGH", "PANIC", "SHOOT", "DELAY", "LEGAL", "WORTH", "ALOOF", "FEVER", "SOLID", "LIMBO", "ARROW", "DONUT", "MUSIC", "SHAPE", "OPERA", "ALTAR", "RIDER", "FUNDS", "BILLY", "BOWEL", "HIDER", "PAVES", "FELON", "STAIN", "WITTY", "TRADE", "GOODY", "UNWED", "OWING", "CLOWN", "TRAMP", "GAZES", "CLICK", "WORST", "INTRO", "AGAPE", "TOMES", "SEPIA", "SHELL", "ELVEN", "VALET", "WENCH", "FIXES", "SPURS", "AHEAD", "USUAL", "PLOWS", "SHONE", "RALLY", "BACKS", "GROWN", "WATCH", "CORAL", "SENSE", "KAYAK", "PINES", "MALES", "KEBAB", "TIRED", "DRUID", "VOWED", "CLANK", "CHIPS", "PRISM", "RAWLY", "BLISS", "MOSSY", "WAGON", "DRIED", "SWOON", "SAUCE", "PLEAD", "FORAY", "SITED", "ALLEY", "BARON", "URGED", "WORMS", "BELOW", "STILL", "OILER", "ISLET", "FLUFF", "BLOAT", "CRONE", "STOMP", "BOSOM", "DRINK", "EASES", "RABBI", "BEGAN", "RENAL", "CHURN", "COCOA", "RIDES", "TRIAD", "OUNCE", "HATCH", "STORM", "TEXTS", "POKER", "OLDER", "GROPE", "ROCKY", "HURTS", "FATES", "SKATE", "HELIX", "GOING", "ELATE", "FRAIL", "ALONG", "DEUCE", "STILT", "BUSHY", "OILED", "DRIFT", "RINSE", "JOINS", "TINGE", "GEODE", "WEIRD", "HONEY", "GLOVE", "SALON", "FETCH", "HEATH", "WHILE", "WARES", "EMCEE", "FOLKS", "OFFAL", "NETTS", "SNIDE", "HOLLY", "GIPSY", "MELTS", "BATHE", "GLUED", "POKES", "WAKEN", "SNORE", "OASIS", "WOUND", "SERFS", "ARGUE", "HIKES", "ARSON", "SERIF", "FISTS", "LADEN", "CREEK", "NOISY", "TOPAZ", "SLEEK", "GLAZE", "STROP", "RATIO", "THORN", "JERKS", "TAKER", "VAPID", "DENIM", "SMACK", "ALARM", "GIFTS", "LOVES", "BASIC", "BEATS", "BLIMP", "CHORD", "SQUID", "SHUTS", "VERSE", "SLOPS", "ZONED", "BINGO", "BERRY", "WREAK", "OWNED", "CRIMP", "CROUP", "HOPES", "OBOES", "EPOCH", "BUNNY", "DOWEL", "RIGOR", "GEARS", "ERASE", "PAVED", "IDEAS", "VEGAN", "SQUAT", "WELCH", "SPICY", "SHARK", "HARPS", "UNDID", "CHILI", "ORGAN", "JADES", "APPLE", "REIGN", "QUEEN", "EQUIP", "MUSTY", "APHID", "DOCKS", "SAVES", "GECKO", "COTTA", "LEAST", "SPAWN", "THINK", "FAULT", "JUNTO", "HANDS", "TUNED", "GOOFY", "GOOEY", "KETCH", "BACON", "BUSED", "GROWS", "LEEKS", "LIKES", "CHUNK", "VILLA", "HEELS", "GLOSS", "FORGE", "HABIT", "SCUBA", "JARLS", "DITTY", "YARDS", "SPACE", "PINKY", "ROVES", "EPOXY", "DRAKE", "FOAMY", "RECON", "SLURP", "HENCE", "HAMZA", "OWLET", "TRUTH", "TRAWL", "BRAKE", "DINGY", "FIBER", "STEEP", "ANIME", "SENDS", "FOODS", "CASTE", "FLICK", "YUMMY", "ADOPT", "DUSTY", "DRUMS", "PUNKS", "LAXLY", "JIFFY", "PIQUE", "HANKY", "CUBIT", "GRAVE", "SKEIN", "LIMPS", "SNOUT", "SEATS", "PULSE", "SCAMP", "LIGHT", "HITCH", "BRIBE", "WISER", "DINER", "STINT", "SHAFT", "KINKY", "PATHS", "FANGS", "ETHER", "HEAVY", "HANGS", "MODAL", "SOLED", "PORTS", "RISER", "TIDAL", "SNUCK", "PATTY", "ROBOT", "MUCUS", "HARSH", "STEEL", "IDIOT", "LULLS", "ASKED", "BERTH", "USING", "ARBOR", "PIETY", "SHOWN", "TEMPT", "STEAL", "SALLY", "STRAY", "SMEAR", "BEARD", "BURNT", "SKIFF", "FETUS", "NOSEY", "BYLAW", "SHAKE", "PEDAL", "SEEDY", "SPINY", "CLUCK", "USHER", "DEMUR", "ADORE", "DEALS", "VOICE", "NAVAL", "TASKS", "FIRED", "PACKS", "HUMID", "NANNY", "SHIFT", "USERS", "KINKS", "FADED", "RHYME", "STAGS", "CANNY", "PINCH", "SERGE", "LUPUS", "INANE", "LEFTS", "AUDIO", "BASIS", "ANTIC", "QUOTA", "FINER", "RUMBA", "DEMON", "GOURD", "FRILL", "CRIES", "GROSS", "FATAL", "HIPPY", "POSED", "FIGHT", "RACES", "TEAMS", "PINEY", "COMIC", "ADMIN", "CHESS", "SURGE", "CRATE", "STEAK", "KINGS", "SANDY", "REEDS", "SMOCK", "GENIE", "RISES", "PLOTS", "POLLS", "NESTS", "CRASS", "FREED", "ALIGN", "HOBBY", "FEWER", "ROBES", "MIRTH", "FAILS", "THANK", "SAFER", "UMBRA", "ETHOS", "PUNKY", "TODAY", "TRUCK", "DIVES", "LAMPS", "YUCKY", "MENUS", "EMBER", "MIGHT", "PLACE", "STINK", "HOWDY", "IRATE", "MOTEL", "MAIDS", "MESSY", "TAKEN", "FINCH", "BORAX", "MOMMY", "AIDED", "WEEKS", "GAPED", "BONEY", "HUMUS", "TAPES", "DECOY", "DIVER", "WRONG", "CANES", "LADLE", "SHINE", "IMAGE", "FOOLS", "FLAKY", "BLOND", "HUMAN", "STUNK", "RUNES", "GRIDS", "TULIP", "BRING", "TUBES", "SNORT", "FENCE", "AZURE", "DEBIT", "SPURT", "LOFTY", "SPOOF", "PALMY", "RIVER", "INDEX", "GIDDY", "ARTSY", "LIARS", "TRICK", "HALES", "MIMIC", "RAIDS", "MANED", "PLAIT", "SHIPS", "VOUCH", "OBEYS", "ROWER", "ASHEN", "PAIRS", "CIRCA", "NYMPH", "MAULS", "SLIME", "AUNTY", "FEEDS", "TRUSS", "WHICH", "EXERT", "LINES", "FEINT", "DAZED", "SITAR", "JUMBO", "NOWAY", "TURNS", "MIDST", "PARER", "UNDER", "TESTS", "CRASH", "DIMLY", "HAPPY", "KNELL", "UPPER", "DROOL", "AVERT", "EMBED", "SEXED", "SCOOP", "TENOR", "BOOBY", "CONDO", "COWER", "SHOAL", "PRIOR", "LOADS", "TEARY", "SIXES", "STALL", "HOVEL", "MOTES", "DONOR", "TAROT", "STUMP", "MOREL", "OCCUR", "PASTY", "BASTE", "QUALM", "PEEPS", "GENTS", "THERE", "ARMOR", "EYING", "FORTE"]
        "admin_password": "123321" 
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
        top: 15%;
        left: 50%;
        transform: translate(-50%, -50%);
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
    
    @keyframes fadeOut {
        0% { opacity: 1; margin-top: 0px; }
        70% { opacity: 1; margin-top: 0px; }
        100% { opacity: 0; margin-top: -20px; visibility: hidden; }
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
    
    # Calculate absent letters for keyboard styling
    absent_letters = set()
    for guess in st.session_state.guesses:
        for char in guess:
            if char not in target_word:
                absent_letters.add(char)

    # Show Notification if present
    if 'notification' in st.session_state and st.session_state.notification:
        st.markdown(f'<div class="centered-notification">{st.session_state.notification}</div>', unsafe_allow_html=True)
        # Clear notification after one render
        st.session_state.notification = None

    st.markdown(grid_html, unsafe_allow_html=True)

    if st.session_state.game_over:
        if st.session_state.game_result == "WIN":
            st.success(f"🎉 You guessed it! The word was {target_word}")
        else:
            st.error(f"💀 Game Over! The word was {target_word}")
        
        if st.button("New Game"):
            st.session_state.guesses = []
            st.session_state.current_guess = ""
            st.session_state.game_over = False
            st.session_state.game_result = None
            st.rerun()

    # 2. KEYBOARD LOGIC
    def press(key):
        if st.session_state.game_over:
            return

        if key == "ENTER":
            if len(st.session_state.current_guess) == 5:
                if st.session_state.current_guess in global_state["dictionary"]:
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
                    st.session_state.notification = "⛔ English Yazbi! Not in dictionary"
                    st.rerun()
        elif key == "⌫":
            st.session_state.current_guess = st.session_state.current_guess[:-1]
            st.rerun()
        elif len(st.session_state.current_guess) < 5:
            st.session_state.current_guess += key
            st.rerun()

    # 3. RENDER KEYBOARD (Precise Columns)
    
    # Row 1: Q-P (10 Keys)
    keys1 = "QWERTYUIOP"
    c1 = st.columns(10)
    for idx, k in enumerate(keys1):
        is_absent = k in absent_letters
        if c1[idx].button(k, key=f"btn_{k}", use_container_width=True, disabled=is_absent):
            press(k)

    # Row 2: A-L (9 Keys) - Centered with Spacers
    keys2 = "ASDFGHJKL"
    c2 = st.columns([0.5] + [1]*9 + [0.5]) 
    for idx, k in enumerate(keys2):
        if c2[idx+1].button(k, key=f"btn_{k}", use_container_width=True, disabled=k in absent_letters):
            press(k)

    # Row 3: Enter - Z-M - Backspace
    keys3 = "ZXCVBNM"
    c3 = st.columns([1.5] + [1]*7 + [1.5]) 
    
    # Enter Button
    if c3[0].button("ENTER", key="enter", use_container_width=True):
        press("ENTER")
        
    for idx, k in enumerate(keys3):
        if c3[idx+1].button(k, key=f"btn_{k}", use_container_width=True, disabled=k in absent_letters):
            press(k)
            
    # Backspace Button
    if c3[8].button("⌫", key="back", use_container_width=True):
        press("⌫")

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
                    st.session_state.game_over = False
                    st.session_state.game_result = None
                    st.toast(f"Word updated to: {custom_word}")
                    st.rerun()
                else:
                    st.error("Word must be exactly 5 letters.")
    elif pwd:
        st.error("Incorrect Password")

