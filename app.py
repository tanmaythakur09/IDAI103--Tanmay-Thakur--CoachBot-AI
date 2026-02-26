import streamlit as st
import google.generativeai as genai
import time

# Configure page
st.set_page_config(
    page_title="CoachBot AI - Youth Sports Assistant",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global futuristic theme CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Mono:wght@400;700&display=swap');

:root {
    --primary-neon: #00ff88;
    --secondary-neon: #00ccff;
    --accent-neon: #ff006e;
    --dark-bg: #0a0e27;
    --card-bg: rgba(10, 14, 39, 0.7);
    --border-glow: rgba(0, 255, 136, 0.3);
}

* {
    font-family: 'Space Mono', monospace;
}

body {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f4a 50%, #0f0f2e 100%);
    color: #e0e0e0;
    overflow-x: hidden;
}

.main {
    background: transparent;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, rgba(10, 14, 39, 0.8) 0%, rgba(26, 31, 74, 0.8) 50%, rgba(15, 15, 46, 0.8) 100%);
}

[data-testid="stTabs"] {
    background: rgba(26, 31, 74, 0.4);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 136, 0.2);
}

.st-tabs [role="tab"] {
    font-family: 'Orbitron', monospace;
    font-weight: 700;
    color: rgba(224, 224, 224, 0.7);
    border: 2px solid transparent;
    border-radius: 8px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.st-tabs [role="tab"][aria-selected="true"] {
    color: #00ff88;
    border-bottom: 3px solid #00ff88;
    box-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
    letter-spacing: 2px;
}

.st-tabs [role="tab"]:hover {
    color: #00ccff;
    border-color: rgba(0, 204, 255, 0.5);
}

/* Input styling */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox div > div > div,
.stTextArea > div > div > textarea {
    background: rgba(10, 14, 39, 0.6) !important;
    border: 2px solid rgba(0, 255, 136, 0.2) !important;
    border-radius: 10px;
    color: #e0e0e0 !important;
    font-family: 'Space Mono', monospace;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #00ff88 !important;
    box-shadow: 0 0 20px rgba(0, 255, 136, 0.5), inset 0 0 10px rgba(0, 255, 136, 0.1);
}

/* Button styling */
.stButton > button {
    background: linear-gradient(135deg, #00ff88 0%, #00ccff 100%);
    color: #0a0e27 !important;
    border: none;
    border-radius: 10px;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    font-family: 'Orbitron', monospace;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    text-transform: uppercase;
    letter-spacing: 1px;
    cursor: pointer;
    box-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 0 40px rgba(0, 255, 136, 0.8), 0 0 20px rgba(0, 204, 255, 0.5);
}

/* Select slider styling */
.stSelectSlider > div > div {
    background: rgba(26, 31, 74, 0.5);
    border-radius: 10px;
}

/* Divider styling */
hr {
    border: 1px solid rgba(0, 255, 136, 0.2);
    margin: 20px 0;
}

/* Success/Error/Warning messages */
.stSuccess, .stError, .stWarning, .stInfo {
    border-left: 4px solid #00ff88;
    border-radius: 8px;
    background: rgba(0, 255, 136, 0.1);
}

.stSuccess {
    border-left-color: #00ff88;
}

.stError {
    border-left-color: #ff006e;
    background: rgba(255, 0, 110, 0.1);
}

.stWarning {
    border-left-color: #ffbe0b;
    background: rgba(255, 190, 11, 0.1);
}

/* Spinner animation enhancement */
.stSpinner > div > div {
    border-color: rgba(0, 255, 136, 0.2);
    border-right-color: #00ff88;
}

/* Select box styling */
.stSelectbox > div > div {
    background: rgba(10, 14, 39, 0.6);
    border: 2px solid rgba(0, 255, 136, 0.2);
    border-radius: 10px;
}

/* Card/Container styling */
.st-emotion-cache-1wmy9hs {
    background: rgba(26, 31, 74, 0.3) !important;
    border: 1px solid rgba(0, 255, 136, 0.15);
    border-radius: 12px;
    backdrop-filter: blur(10px);
}

/* Column container styling */
[data-testid="column"] {
    background: rgba(26, 31, 74, 0.2);
    border-radius: 10px;
    padding: 15px;
    transition: all 0.3s ease;
}

[data-testid="column"]:hover {
    background: rgba(26, 31, 74, 0.4);
    border: 1px solid rgba(0, 255, 136, 0.2);
}

/* Expand/collapse styling */
.streamlit-expanderHeader {
    background: rgba(26, 31, 74, 0.5);
    border: 1px solid rgba(0, 255, 136, 0.2);
    border-radius: 8px;
    transition: all 0.3s ease;
}

.streamlit-expanderHeader:hover {
    background: rgba(26, 31, 74, 0.7);
    border-color: #00ff88;
}

/* Markdown styling */
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
    font-family: 'Orbitron', monospace;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Metrics and KPI styling */
[data-testid="stMetric"] {
    background: rgba(26, 31, 74, 0.4);
    border: 1px solid rgba(0, 255, 136, 0.2);
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 0 20px rgba(0, 255, 136, 0.1);
}

/* JSON display styling */
.stJson {
    background: rgba(10, 14, 39, 0.8);
    border: 1px solid rgba(0, 255, 136, 0.2);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# Initialize login session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}
if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# ============ USER ACTIVITY TRACKING ============
# Initialize activity tracking
if "user_activities" not in st.session_state:
    st.session_state.user_activities = {
        "workouts": [],
        "nutrition_logs": [],
        "recovery_sessions": [],
        "goals": [],
        "stats": {
            "total_workouts": 0,
            "total_calories_burned": 0,
            "current_streak": 0,
            "hydration_cups": 0,
            "avg_sleep_hours": 0
        }
    }

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# Initialize logger states
if "show_workout_logger" not in st.session_state:
    st.session_state.show_workout_logger = False
if "show_nutrition_logger" not in st.session_state:
    st.session_state.show_nutrition_logger = False
if "show_sleep_logger" not in st.session_state:
    st.session_state.show_sleep_logger = False

# Initialize advanced features
if "user_badges" not in st.session_state:
    st.session_state.user_badges = {
        "first_workouts": False,
        "week_warrior": False,
        "calorie_crusher": False,
        "nutrition_master": False,
        "streak_champion": False,
        "recovery_king": False,
        "consistency": 0  # For tracking consecutive days
    }

if "leaderboard_data" not in st.session_state:
    st.session_state.leaderboard_data = {
        "test": 0,
        "Guest": 0
    }

if "ai_coach_memory" not in st.session_state:
    st.session_state.ai_coach_memory = []

if "community_challenges" not in st.session_state:
    st.session_state.community_challenges = {
        "monthly_step": {"participants": 0, "goal": 100000},
        "calorie_burn": {"participants": 0, "goal": 50000},
        "hydration_hero": {"participants": 0, "goal": 240},
        "sleep_master": {"participants": 0, "goal": 56}  # 8 hours × 7 days
    }

if "goal_predictions" not in st.session_state:
    st.session_state.goal_predictions = {}

# ============ SIGNUP PAGE (ADVANCED) ============
def signup_page():
    """Display the advanced, interactive & motivating signup page"""
    # Advanced CSS styling
    st.markdown("""
    <style>
    .signup-container {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f4a 25%, #0f0f2e 50%, #1a1f4a 75%, #0a0e27 100%);
        min-height: 100vh;
        padding: 40px 20px;
        position: relative;
        overflow: hidden;
    }
    
    .signup-box {
        background: linear-gradient(135deg, rgba(26, 31, 74, 0.9) 0%, rgba(10, 14, 39, 0.95) 100%);
        border-radius: 24px;
        padding: 60px;
        box-shadow: 
            0 0 100px rgba(0, 255, 136, 0.35),
            0 0 60px rgba(0, 204, 255, 0.25),
            inset 0 0 50px rgba(0, 255, 136, 0.08);
        border: 2px solid rgba(0, 255, 136, 0.4);
        text-align: center;
        max-width: 550px;
        backdrop-filter: blur(25px);
        animation: float-up 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    @keyframes float-up {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .signup-title {
        font-family: 'Orbitron', monospace;
        font-size: 52px;
        font-weight: 900;
        background: linear-gradient(135deg, #00ff88 0%, #00ccff 50%, #ffbe0b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 5px;
        letter-spacing: 2px;
        animation: glow 3s ease-in-out infinite;
    }
    
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 30px rgba(0, 255, 136, 0.3); }
        50% { text-shadow: 0 0 50px rgba(0, 255, 136, 0.6), 0 0 20px rgba(0, 204, 255, 0.4); }
    }
    
    .signup-subtitle {
        color: #00ff88;
        font-size: 14px;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: bold;
    }
    
    .signup-tagline {
        color: #00ccff;
        font-size: 13px;
        margin-bottom: 40px;
        font-style: italic;
        opacity: 0.85;
    }
    
    .benefits-row {
        display: flex;
        justify-content: space-around;
        margin: 30px 0;
        gap: 10px;
    }
    
    .benefit-item {
        text-align: center;
        font-size: 24px;
    }
    
    .benefit-text {
        color: rgba(224, 224, 224, 0.7);
        font-size: 11px;
        margin-top: 5px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .input-field {
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(0, 255, 136, 0.25);
        border-radius: 12px;
        padding: 14px 16px;
        color: #e0e0e0;
        font-family: 'Space Mono', monospace;
        margin-bottom: 10px;
        transition: all 0.3s ease;
        font-size: 14px;
    }
    
    .input-field:focus {
        border-color: #00ff88;
        box-shadow: 0 0 25px rgba(0, 255, 136, 0.4), inset 0 0 10px rgba(0, 255, 136, 0.1);
        background: rgba(255, 255, 255, 0.12);
    }
    
    .validation-text {
        font-size: 11px;
        margin-top: 5px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        min-height: 16px;
    }
    
    .validation-good {
        color: #00ff88;
    }
    
    .validation-bad {
        color: #ff4444;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00ff88 0%, #00ccff 100%);
        color: #0a0e27;
        border: none;
        border-radius: 12px;
        padding: 14px;
        font-size: 15px;
        font-weight: bold;
        font-family: 'Orbitron', monospace;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        box-shadow: 0 0 25px rgba(0, 255, 136, 0.5);
        margin: 5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 0 50px rgba(0, 255, 136, 0.8), 0 0 25px rgba(0, 204, 255, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .divider-line {
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.4), transparent);
        margin: 30px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2.5, 1])
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 40px 0; font-size: 45px; opacity: 0.6;">
            <div>⚡</div>
            <div style="margin: 40px 0;">💪</div>
            <div style="margin: 40px 0;">🎯</div>
            <div style="margin: 40px 0;">🏆</div>
            <div style="margin: 40px 0;">🚀</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="signup-box">', unsafe_allow_html=True)
        
        # Animated emoji
        st.markdown("""
        <div style="text-align: center; font-size: 70px; margin-bottom: 15px; animation: bounce 2.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;">
            🚀
        </div>
        <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<h1 class="signup-title">⚽ COACHBOT AI</h1>', unsafe_allow_html=True)
        st.markdown('<p class="signup-subtitle">JOIN THE REVOLUTION</p>', unsafe_allow_html=True)
        st.markdown('<p class="signup-tagline">Unlock your athletic potential with AI-powered coaching</p>', unsafe_allow_html=True)
        
        # Benefits preview
        st.markdown("""
        <div class="benefits-row">
            <div class="benefit-item">
                <div>🤖</div>
                <div class="benefit-text">AI Coach</div>
            </div>
            <div class="benefit-item">
                <div>📊</div>
                <div class="benefit-text">Real Analytics</div>
            </div>
            <div class="benefit-item">
                <div>🎯</div>
                <div class="benefit-text">Smart Goals</div>
            </div>
            <div class="benefit-item">
                <div>🏅</div>
                <div class="benefit-text">Achievements</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
        
        # Sign up form with validation
        new_username = st.text_input(
            "👤 Create Username",
            placeholder="3+ characters",
            key="signup_username",
            label_visibility="collapsed"
        )
        
        # Real-time username validation
        if new_username:
            if len(new_username) < 3:
                st.markdown('<p class="validation-text validation-bad">❌ Minimum 3 characters required</p>', unsafe_allow_html=True)
            elif new_username in st.session_state.registered_users:
                st.markdown('<p class="validation-text validation-bad">❌ Username already taken</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="validation-text validation-good">✅ Username available</p>', unsafe_allow_html=True)
        
        new_email = st.text_input(
            "📧 Email Address",
            placeholder="your@email.com",
            key="signup_email",
            label_visibility="collapsed"
        )
        
        # Email validation
        if new_email:
            if "@" not in new_email or "." not in new_email:
                st.markdown('<p class="validation-text validation-bad">❌ Invalid email format</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="validation-text validation-good">✅ Valid email</p>', unsafe_allow_html=True)
        
        new_password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="4+ characters (strong recommended)",
            key="signup_password",
            label_visibility="collapsed"
        )
        
        # Password strength indicator
        if new_password:
            strength = "Weak"
            color = "validation-bad"
            if len(new_password) >= 8:
                strength = "Strong"
                color = "validation-good"
            elif len(new_password) >= 6:
                strength = "Medium"
                color = "validation-text"
            
            st.markdown(f'<p class="validation-text {color}">⚡ Strength: {strength}</p>', unsafe_allow_html=True)
        
        confirm_password = st.text_input(
            "🔐 Confirm Password",
            type="password",
            placeholder="Re-enter password",
            key="signup_confirm_password",
            label_visibility="collapsed"
        )
        
        # Password match validation
        if confirm_password and new_password:
            if new_password == confirm_password:
                st.markdown('<p class="validation-text validation-good">✅ Passwords match</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="validation-text validation-bad">❌ Passwords don\'t match</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("✨ CREATE ACCOUNT", key="signup_btn", use_container_width=True):
                # Comprehensive validation
                if not new_username or not new_email or not new_password or not confirm_password:
                    st.error("❌ Please fill all fields!")
                elif len(new_username) < 3:
                    st.error("❌ Username must be at least 3 characters!")
                elif "@" not in new_email or "." not in new_email:
                    st.error("❌ Please enter a valid email!")
                elif len(new_password) < 4:
                    st.error("❌ Password must be at least 4 characters!")
                elif new_password != confirm_password:
                    st.error("❌ Passwords don't match!")
                elif new_username in st.session_state.registered_users:
                    st.error("❌ Username already exists!")
                else:
                    # Register user
                    st.session_state.registered_users[new_username] = {
                        "password": new_password,
                        "email": new_email
                    }
                    st.markdown("""
                    <div style="text-align: center; margin: 20px 0;">
                        <div style="font-size: 40px; animation: celebrate 0.6s ease-out;">🎉</div>
                        <h3 style="color: #00ff88;">WELCOME CHAMPION!</h3>
                        <p style="color: #00ccff;">Your account is ready. Redirecting...</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    st.session_state.show_signup = False
                    time.sleep(1.5)
                    st.rerun()
        
        with col_b:
            if st.button("🔙 BACK", key="back_to_login", use_container_width=True):
                st.session_state.show_signup = False
                st.rerun()
        
        st.markdown('<p style="text-align: center; color: #00ccff; font-size: 11px; margin-top: 20px; opacity: 0.7; text-transform: uppercase; letter-spacing: 1px;">Secure • Fast • Powerful</p>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 40px 0; font-size: 45px; opacity: 0.6;">
            <div>⚽</div>
            <div style="margin: 40px 0;">🏀</div>
            <div style="margin: 40px 0;">⚾</div>
            <div style="margin: 40px 0;">🎾</div>
            <div style="margin: 40px 0;">🏈</div>
        </div>
        """, unsafe_allow_html=True)

# ============ LOGIN PAGE (ADVANCED & INTERACTIVE) ============
def login_page():
    """Display the premium, interactive, and motivating login page"""
    # Advanced CSS styling with animations
    st.markdown("""
    <style>
    .login-outer {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f4a 25%, #0f0f2e 50%, #1a1f4a 75%, #0a0e27 100%);
        min-height: 100vh;
        padding: 40px 20px;
        position: relative;
        overflow: hidden;
    }
    
    .login-wrapper {
        position: relative;
        z-index: 10;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .login-box {
        background: linear-gradient(135deg, rgba(26, 31, 74, 0.95) 0%, rgba(10, 14, 39, 0.98) 100%);
        border-radius: 24px;
        padding: 65px;
        box-shadow: 
            0 0 120px rgba(0, 255, 136, 0.4),
            0 0 80px rgba(0, 204, 255, 0.3),
            inset 0 0 60px rgba(0, 255, 136, 0.1);
        border: 2.5px solid rgba(0, 255, 136, 0.45);
        text-align: center;
        max-width: 580px;
        backdrop-filter: blur(30px);
        animation: slideInCenter 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }
    
    @keyframes slideInCenter {
        0% { opacity: 0; transform: scale(0.95); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    .login-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(0, 255, 136, 0.1) 0%, transparent 70%);
        animation: orbit 8s linear infinite;
        pointer-events: none;
    }
    
    @keyframes orbit {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .login-content {
        position: relative;
        z-index: 1;
    }
    
    .login-emoji {
        font-size: 75px;
        margin-bottom: 15px;
        animation: float-bounce 2.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
        display: inline-block;
    }
    
    @keyframes float-bounce {
        0%, 100% { transform: translateY(0) rotateZ(0deg); }
        50% { transform: translateY(-15px) rotateZ(2deg); }
    }
    
    .login-title {
        font-family: 'Orbitron', monospace;
        font-size: 54px;
        font-weight: 900;
        background: linear-gradient(135deg, #00ff88 0%, #00ccff 60%, #ffbe0b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 8px;
        letter-spacing: 3px;
        animation: glow-pulse 3s ease-in-out infinite;
    }
    
    @keyframes glow-pulse {
        0%, 100% { filter: drop-shadow(0 0 30px rgba(0, 255, 136, 0.3)); }
        50% { filter: drop-shadow(0 0 50px rgba(0, 255, 136, 0.6)) drop-shadow(0 0 20px rgba(0, 204, 255, 0.4)); }
    }
    
    .login-tagline {
        color: #00ff88;
        font-size: 14px;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 2.5px;
        font-weight: bold;
        text-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
    }
    
    .login-subtitle {
        color: #00ccff;
        font-size: 13px;
        margin-bottom: 35px;
        font-style: italic;
        opacity: 0.85;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    .login-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.4), transparent);
        margin: 30px 0;
    }
    
    .features-line {
        display: flex;
        justify-content: space-around;
        margin: 25px 0;
        padding: 20px 0;
        gap: 8px;
    }
    
    .feature-badge {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.15) 0%, rgba(0, 204, 255, 0.1) 100%);
        border: 1.5px solid rgba(0, 255, 136, 0.3);
        border-radius: 10px;
        padding: 12px 16px;
        font-size: 12px;
        color: #00ff88;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        cursor: default;
    }
    
    .feature-badge:hover {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.25) 0%, rgba(0, 204, 255, 0.2) 100%);
        border-color: #00ff88;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.3);
        transform: translateY(-2px);
    }
    
    .login-input {
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(0, 255, 136, 0.3);
        border-radius: 12px;
        padding: 15px 18px;
        color: #e0e0e0;
        font-family: 'Space Mono', monospace;
        margin-bottom: 12px;
        transition: all 0.3s ease;
        font-size: 15px;
    }
    
    .login-input:focus {
        border-color: #00ff88;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.5), inset 0 0 15px rgba(0, 255, 136, 0.08);
        background: rgba(255, 255, 255, 0.12);
        transform: translateY(-2px);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00ff88 0%, #00ccff 100%);
        color: #0a0e27;
        border: none;
        border-radius: 12px;
        padding: 16px;
        font-size: 16px;
        font-weight: bold;
        font-family: 'Orbitron', monospace;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.6);
        margin: 6px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.2);
        transition: left 0.5s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 0 60px rgba(0, 255, 136, 0.9), 0 0 30px rgba(0, 204, 255, 0.7);
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .button-row {
        display: flex;
        gap: 10px;
        margin: 15px 0;
    }
    
    .btn-primary {
        flex: 1;
    }
    
    .btn-secondary {
        flex: 1;
    }
    
    .footer-text {
        text-align: center;
        color: #00ccff;
        font-size: 12px;
        margin-top: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.8;
    }
    
    .demo-hint {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 204, 255, 0.08) 100%);
        border: 1.5px dashed rgba(0, 255, 136, 0.3);
        border-radius: 10px;
        padding: 15px;
        margin-top: 25px;
        color: rgba(224, 224, 224, 0.8);
        font-size: 12px;
        line-height: 1.6;
    }
    
    .demo-hint-title {
        color: #00ff88;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }
    
    .demo-credentials {
        color: #ffbe0b;
        font-family: 'Space Mono', monospace;
        font-weight: bold;
        margin: 8px 0;
    }
    
    .testimonial-box {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.08) 0%, rgba(0, 204, 255, 0.08) 100%);
        border-left: 4px solid rgba(0, 255, 136, 0.5);
        border-radius: 8px;
        padding: 15px;
        margin: 20px 0;
        color: rgba(224, 224, 224, 0.85);
        font-size: 13px;
        font-style: italic;
        line-height: 1.5;
    }
    
    .testimonial-author {
        color: #00ff88;
        font-weight: bold;
        margin-top: 8px;
        text-transform: uppercase;
        font-size: 11px;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create the layout
    col1, col2, col3 = st.columns([0.9, 2.2, 0.9])
    
    # Left decorative elements
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 50px 10px; font-size: 48px; opacity: 0.5; animation: float 4s ease-in-out infinite;">
            <div>🎯</div>
            <div style="margin: 45px 0;">💪</div>
            <div style="margin: 45px 0;">⚡</div>
            <div style="margin: 45px 0;">🏆</div>
            <div style="margin: 45px 0;">🚀</div>
        </div>
        <style>
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Main login form
    with col2:
        st.markdown('<div class="login-box"><div class="login-content">', unsafe_allow_html=True)
        
        # Animated hero emoji
        st.markdown('<div class="login-emoji">🤖</div>', unsafe_allow_html=True)
        
        # Title and tagline
        st.markdown('<h1 class="login-title">⚽ COACHBOT AI</h1>', unsafe_allow_html=True)
        st.markdown('<p class="login-tagline">⚡ ELITE PERFORMANCE AWAITS ⚡</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-subtitle">Your AI-powered personal sports coach is ready</p>', unsafe_allow_html=True)
        
        # Feature badges
        st.markdown("""
        <div class="features-line">
            <div class="feature-badge">🤖 AI Coach</div>
            <div class="feature-badge">📊 Analytics</div>
            <div class="feature-badge">🎯 Smart Goals</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="login-divider"></div>', unsafe_allow_html=True)
        
        # Login input fields
        username = st.text_input(
            "👤 USERNAME",
            placeholder="Enter your username",
            key="login_username",
            label_visibility="collapsed"
        )
        
        password = st.text_input(
            "🔒 PASSWORD",
            type="password",
            placeholder="Enter your password",
            key="login_password",
            label_visibility="collapsed"
        )
        
        # Remember me simulation
        col_check, col_empty = st.columns([1, 3])
        with col_check:
            remember = st.checkbox("Remember me", key="remember_login", label_visibility="collapsed")
        
        st.markdown('<div class="login-divider"></div>', unsafe_allow_html=True)
        
        # Login/Signup buttons
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("🚀 LOGIN", key="login_btn", use_container_width=True):
                if username and password:
                    if username in st.session_state.registered_users:
                        if st.session_state.registered_users[username]["password"] == password:
                            st.session_state.logged_in = True
                            st.session_state.user_name = username
                            st.markdown("""
                            <div style="text-align: center;">
                                <div style="font-size: 50px; animation: celebrate 0.6s ease-out;">🎉</div>
                                <h3 style="color: #00ff88; margin: 10px 0;">WELCOME BACK!</h3>
                                <p style="color: #00ccff;">Loading your dashboard...</p>
                            </div>
                            """, unsafe_allow_html=True)
                            st.balloons()
                            time.sleep(0.8)
                            st.rerun()
                        else:
                            st.error("❌ Incorrect password!")
                    else:
                        st.error("❌ User not found! Please sign up first.")
                else:
                    st.warning("⚠️ Please enter both username and password!")
        
        with col_b:
            if st.button("📝 SIGN UP", key="signup_link_btn", use_container_width=True):
                st.session_state.show_signup = True
                st.rerun()
        
        # Demo accounts & features
        st.markdown("""
        <div class="demo-hint">
            <div class="demo-hint-title">🎮 QUICK START:</div>
            <div>Create your own account or test with:</div>
            <div class="demo-credentials">Username: test<br>Password: test1234</div>
            <div style="margin-top: 10px; opacity: 0.7;">Experience real-time activity tracking, AI coaching, and performance analytics!</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Motivational testimonial
        st.markdown("""
        <div class="testimonial-box">
            <div style="font-size: 16px; margin-bottom: 10px;">⭐⭐⭐⭐⭐</div>
            <div>"CoachBot AI transformed my training routine. The personalized insights and real-time feedback helped me achieve my fitness goals 40% faster!"</div>
            <div class="testimonial-author">— Elite Athlete, Performance Champion 🏆</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="footer-text">🔒 Secure • 🚀 Powerful • 🤖 Intelligent</p>', unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Right decorative elements
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 50px 10px; font-size: 48px; opacity: 0.5; animation: float-reverse 4s ease-in-out infinite;">
            <div>⚽</div>
            <div style="margin: 45px 0;">🏀</div>
            <div style="margin: 45px 0;">💡</div>
            <div style="margin: 45px 0;">📈</div>
            <div style="margin: 45px 0;">🎖️</div>
        </div>
        <style>
        @keyframes float-reverse {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(8px); }
        }
        </style>
        """, unsafe_allow_html=True)

# Show login/signup page if not logged in
if not st.session_state.logged_in:
    if st.session_state.show_signup:
        signup_page()
    else:
        login_page()
    st.stop()

# ============ MAIN APP (shown after login) ============

# Enhanced main styling with professional hero section
st.markdown("""
<style>
/* Premium Luxury Theme */
.hero-container {
    background: linear-gradient(135deg, rgba(0, 255, 136, 0.08) 0%, rgba(0, 204, 255, 0.08) 50%, rgba(255, 0, 110, 0.05) 100%);
    border: 2px solid rgba(0, 255, 136, 0.4);
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 30px;
    backdrop-filter: blur(20px);
    box-shadow: 
        0 0 60px rgba(0, 255, 136, 0.2),
        0 0 30px rgba(0, 204, 255, 0.15),
        inset 0 0 40px rgba(0, 255, 136, 0.05);
    animation: float-in 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    border-image: linear-gradient(135deg, #00ff88 0%, #00ccff 50%, #ff006e 100%) 1;
}

@keyframes float-in {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-title {
    font-family: 'Orbitron', monospace;
    color: transparent;
    background: linear-gradient(135deg, #00ff88 0%, #00ccff 50%, #ffbe0b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 56px;
    font-weight: 900;
    text-shadow: 0 0 40px rgba(0, 255, 136, 0.6);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 12px;
    margin-top: 0;
    animation: glow-pulse 3s ease-in-out infinite;
}

@keyframes glow-pulse {
    0%, 100% { 
        text-shadow: 0 0 30px rgba(0, 255, 136, 0.4), 0 0 60px rgba(0, 204, 255, 0.2);
    }
    50% { 
        text-shadow: 0 0 50px rgba(0, 255, 136, 0.6), 0 0 80px rgba(0, 204, 255, 0.4);
    }
}

.hero-tagline {
    color: #00ff88;
    font-size: 18px;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: bold;
    margin-bottom: 12px;
    text-shadow: 0 0 20px rgba(0, 255, 136, 0.4);
}

.hero-quote {
    color: #00ccff;
    font-size: 14px;
    font-style: italic;
    opacity: 0.85;
    letter-spacing: 1px;
    font-weight: 300;
}

/* Premium stat card */
.premium-stat-card {
    background: linear-gradient(135deg, rgba(26, 31, 74, 0.5) 0%, rgba(10, 14, 39, 0.7) 100%);
    border: 2px solid rgba(0, 255, 136, 0.3);
    border-radius: 15px;
    padding: 24px;
    margin-bottom: 16px;
    backdrop-filter: blur(15px);
    box-shadow: 
        0 8px 32px rgba(0, 255, 136, 0.1),
        0 0 20px rgba(0, 204, 255, 0.08),
        inset 0 0 25px rgba(0, 255, 136, 0.03);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.premium-stat-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.1), transparent);
    transition: left 0.5s ease;
}

.premium-stat-card:hover {
    border-color: #00ff88;
    box-shadow: 
        0 12px 48px rgba(0, 255, 136, 0.2),
        0 0 30px rgba(0, 204, 255, 0.15),
        inset 0 0 35px rgba(0, 255, 136, 0.08);
    transform: translateY(-5px);
}

.premium-stat-card:hover::before {
    left: 100%;
}

.stat-number {
    color: #00ff88;
    font-size: 48px;
    font-weight: bold;
    font-family: 'Orbitron', monospace;
    text-shadow: 0 0 25px rgba(0, 255, 136, 0.4);
    margin-bottom: 8px;
}

.stat-label {
    color: rgba(224, 224, 224, 0.8);
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 600;
}

.stat-delta {
    color: #ffbe0b;
    font-size: 12px;
    margin-top: 8px;
    font-weight: bold;
}

/* Activity card */
.activity-card {
    background: linear-gradient(135deg, rgba(0, 255, 136, 0.08) 0%, rgba(0, 204, 255, 0.08) 100%);
    border: 1.5px solid rgba(0, 255, 136, 0.25);
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 14px;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 20px rgba(0, 255, 136, 0.08);
    transition: all 0.3s ease;
    animation: slide-in-left 0.5s ease-out;
}

@keyframes slide-in-left {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.activity-card:hover {
    border-color: #00ff88;
    box-shadow: 0 6px 30px rgba(0, 255, 136, 0.12);
    background: linear-gradient(135deg, rgba(0, 255, 136, 0.12) 0%, rgba(0, 204, 255, 0.12) 100%);
}

.activity-title {
    color: #00ff88;
    font-weight: bold;
    font-size: 15px;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.activity-meta {
    color: #00ccff;
    font-size: 12px;
    margin: 4px 0;
}

.activity-stats {
    color: rgba(224, 224, 224, 0.7);
    font-size: 12px;
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px solid rgba(0, 255, 136, 0.15);
}

/* Premium section card */
.section-card {
    background: linear-gradient(135deg, rgba(26, 31, 74, 0.45) 0%, rgba(10, 14, 39, 0.6) 100%);
    border: 2px solid rgba(0, 255, 136, 0.25);
    border-radius: 15px;
    padding: 28px;
    margin-bottom: 22px;
    backdrop-filter: blur(15px);
    box-shadow: 
        0 10px 40px rgba(0, 255, 136, 0.1),
        0 0 25px rgba(0, 204, 255, 0.08),
        inset 0 0 30px rgba(0, 255, 136, 0.04);
    transition: all 0.4s ease;
}

.section-card:hover {
    background: linear-gradient(135deg, rgba(26, 31, 74, 0.6) 0%, rgba(10, 14, 39, 0.75) 100%);
    border-color: rgba(0, 255, 136, 0.4);
    box-shadow: 
        0 15px 50px rgba(0, 255, 136, 0.15),
        0 0 35px rgba(0, 204, 255, 0.12),
        inset 0 0 40px rgba(0, 255, 136, 0.06);
}

.section-header {
    font-family: 'Orbitron', monospace;
    color: #00ffff;
    font-size: 22px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 12px;
    text-shadow: 0 0 15px rgba(0, 204, 255, 0.3);
}

/* Premium button styling */
.stButton > button {
    background: linear-gradient(135deg, #00ff88 0%, #00ccff 100%);
    color: #0a0e27 !important;
    border: none;
    border-radius: 12px;
    padding: 14px 28px;
    font-size: 15px;
    font-weight: bold;
    font-family: 'Orbitron', monospace;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    cursor: pointer;
    box-shadow: 
        0 8px 25px rgba(0, 255, 136, 0.3),
        0 0 15px rgba(0, 204, 255, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.6s ease;
}

.stButton > button:hover::before {
    left: 100%;
}

.stButton > button:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 
        0 12px 40px rgba(0, 255, 136, 0.5),
        0 0 25px rgba(0, 204, 255, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.4);
}

.stButton > button:active {
    transform: translateY(-2px);
}

/* Progress bar - premium style */
.progress-container {
    margin: 16px 0;
}

.progress-label {
    color: #e0e0e0;
    font-size: 13px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    font-weight: 500;
    letter-spacing: 0.5px;
}

.progress-value {
    color: #00ff88;
    font-weight: bold;
    font-family: 'Orbitron', monospace;
    text-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
}

.intensity-bar {
    background: linear-gradient(90deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 204, 255, 0.1) 100%);
    height: 10px;
    border-radius: 5px;
    margin-bottom: 18px;
    border: 1px solid rgba(0, 255, 136, 0.2);
    overflow: hidden;
    box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.3);
    position: relative;
}

.intensity-bar::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background: linear-gradient(90deg, #00ff88 0%, #00ccff 100%);
    border-radius: 5px;
    box-shadow: 0 0 15px rgba(0, 255, 136, 0.5);
    animation: pulse-width 0.6s ease-out;
}

@keyframes pulse-width {
    from {
        width: 0%;
    }
    to {
        width: var(--progress-width, 100%);
    }
}

/* Tab enhancement */
[data-testid="stTabs"] {
    background: rgba(26, 31, 74, 0.3);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(0, 255, 136, 0.2);
    box-shadow: 0 0 30px rgba(0, 255, 136, 0.08);
}

.st-tabs [role="tab"] {
    font-family: 'Orbitron', monospace;
    font-weight: 700;
    color: rgba(224, 224, 224, 0.6);
    border: 2px solid transparent;
    border-radius: 10px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    text-transform: uppercase;
    letter-spacing: 1.2px;
    padding: 12px 20px;
}

.st-tabs [role="tab"][aria-selected="true"] {
    color: #00ff88;
    border-bottom: 3px solid #00ff88;
    box-shadow: 0 0 25px rgba(0, 255, 136, 0.4);
    letter-spacing: 2px;
    background: rgba(0, 255, 136, 0.1);
}

.st-tabs [role="tab"]:hover {
    color: #00ccff;
    border-color: rgba(0, 204, 255, 0.5);
}

</style>

<div class="hero-container">
    <h1 class="hero-title">⚽ COACHBOT AI</h1>
    <p class="hero-tagline">🚀 Elite Athletic Performance Platform</p>
    <p class="hero-quote">Track. Train. Transform. Achieve Championship Performance.</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for api_key
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# ============ SIDEBAR NAVIGATION ============
with st.sidebar:
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, rgba(10, 14, 39, 0.95) 0%, rgba(26, 31, 74, 0.9) 100%);
        border-right: 3px solid rgba(0, 255, 136, 0.3);
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #00ff88;
        font-family: 'Orbitron', monospace;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
    }
    
    .sidebar-section {
        background: rgba(0, 255, 136, 0.05);
        border: 1px solid rgba(0, 255, 136, 0.2);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
    
    .profile-card {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 204, 255, 0.1) 100%);
        border: 2px solid rgba(0, 255, 136, 0.3);
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 20px;
        animation: fade-in 0.6s ease-out;
    }
    
    .profile-name {
        color: #00ff88;
        font-weight: bold;
        font-size: 16px;
        margin: 10px 0;
    }
    
    .nav-button {
        width: 100%;
        padding: 12px;
        margin: 8px 0;
        background: rgba(0, 255, 136, 0.1);
        border: 2px solid rgba(0, 255, 136, 0.2);
        color: #e0e0e0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: left;
    }
    
    .nav-button:hover {
        background: rgba(0, 255, 136, 0.2);
        border-color: #00ff88;
        color: #00ff88;
    }
    
    @keyframes fade-in {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Profile Section
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 40px; margin-bottom: 5px;">💪</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-name">Welcome {st.session_state.user_name}!</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: #00ccff; font-size: 12px; margin: 5px 0;">Elite Athlete Mode</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Navigation Section
    st.markdown("<h3 style='color: #00ff88;'>🗂️ Navigation</h3>", unsafe_allow_html=True)
    
    nav_options = {
        "🏠 Dashboard": "Dashboard",
        "🏋️ Generate Plans": "Plans",
        "📊 Performance": "Performance",
        "🏆 Achievements": "Achievements",
        "👥 Community": "Community",
        "💬 AI Coach": "AICoach",
        "💬 Help & Support": "Help",
    }
    
    for nav_label, nav_value in nav_options.items():
        if st.button(nav_label, use_container_width=True, key=f"nav_{nav_value}"):
            st.session_state.current_page = nav_value
            st.rerun()
    
    st.divider()
    
    # API Configuration
    st.markdown("<h3 style='color: #00ff88;'>🔐 API Setup</h3>", unsafe_allow_html=True)
    api_key = st.text_input(
        "Google AI Studio Key",
        type="password",
        placeholder="Paste your API key here",
        help="Get from https://ai.google.dev/app/apikey",
        key="sidebar_api_key"
    )
    
    if api_key:
        st.session_state.api_key = api_key
        try:
            genai.configure(api_key=api_key)
            st.success("✅ API Key Active!")
        except:
            st.error("❌ Invalid API Key")
    
    st.info("❕ Free tier has request limits. Upgrade for unlimited access.")
    
    st.divider()
    
    # Quick Stats
    st.markdown("<h3 style='color: #00ff88;'>📈 Your Stats</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Workouts", "12", "+2")
    with col2:
        st.metric("Streak", "8d", "+1d")
    
    st.divider()
    
    # Logout
    if st.button("🚪 LOGOUT", use_container_width=True, key="logout_final"):
        st.session_state.logged_in = False
        st.rerun()

# Set default values
temperature = 0.7

# ============ DASHBOARD PAGE ============
def dashboard_page():
    """Main dashboard with real user activity tracking"""
    
    # Dynamic stats based on user activities
    stats = st.session_state.user_activities["stats"]
    
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>📊 Today's Performance</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{stats['total_workouts']}</div>
            <div class="stat-label">💪 Workouts</div>
            <div class="stat-delta">+{max(0, stats['total_workouts'] - max(0, stats['total_workouts']-1))} this week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{stats['current_streak']}</div>
            <div class="stat-label">🔥 Day Streak</div>
            <div class="stat-delta">Keep it going!</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{stats['hydration_cups']}/8</div>
            <div class="stat-label">💧 Hydration</div>
            <div class="stat-delta">{max(0, 8 - stats['hydration_cups'])} cups left</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{stats['avg_sleep_hours']:.1f}h</div>
            <div class="stat-label">😴 Sleep</div>
            <div class="stat-delta">Excellent recovery</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Quick Activity Logging Section
    st.markdown("<h2 style='color: #00ccff; font-family: Orbitron, monospace;'>⚡ Log Activity</h2>", unsafe_allow_html=True)
    
    log_col1, log_col2, log_col3, log_col4 = st.columns(4)
    
    with log_col1:
        if st.button("🏋️ Log Workout", use_container_width=True, key="quick_log_workout"):
            st.session_state.show_workout_logger = True
    
    with log_col2:
        if st.button("🥗 Log Meal", use_container_width=True, key="quick_log_meal"):
            st.session_state.show_nutrition_logger = True
    
    with log_col3:
        if st.button("💧 Add Hydration", use_container_width=True, key="quick_log_hydration"):
            stats['hydration_cups'] = min(8, stats['hydration_cups'] + 1)
            st.success(f"✅ Hydration logged! {stats['hydration_cups']}/8 cups")
            st.rerun()
    
    with log_col4:
        if st.button("😴 Log Sleep", use_container_width=True, key="quick_log_sleep"):
            st.session_state.show_sleep_logger = True
    
    st.divider()
    
    # Workout Logger Modal
    if st.session_state.get("show_workout_logger", False):
        with st.container():
            st.markdown("<div class='section-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #00ff88;'>💪 Log Workout</h3>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                workout_type = st.selectbox("Type", ["Strength", "Cardio", "Flexibility", "Sports Practice", "Other"], key="wout_type")
                duration = st.number_input("Duration (min)", 10, 300, 60, key="wout_duration")
            
            with col2:
                intensity = st.select_slider("Intensity", ["Light", "Moderate", "High", "Very High"], value="Moderate", key="wout_intensity")
                calories = st.number_input("Calories Burned", 0, 2000, 300, key="wout_cals")
            
            notes = st.text_area("Notes (optional)", placeholder="How did the workout feel?", key="wout_notes", height=80)
            
            col_log, col_cancel = st.columns(2)
            with col_log:
                if st.button("✅ Save Workout", use_container_width=True, key="save_workout"):
                    from datetime import datetime
                    workout_entry = {
                        "type": workout_type,
                        "duration": duration,
                        "intensity": intensity,
                        "calories": calories,
                        "notes": notes,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    st.session_state.user_activities["workouts"].append(workout_entry)
                    stats['total_workouts'] += 1
                    stats['total_calories_burned'] += calories
                    stats['current_streak'] += 1
                    st.session_state.show_workout_logger = False
                    st.success(f"✅ Workout logged! +{calories} calories, Streak: {stats['current_streak']} days")
                    st.rerun()
            
            with col_cancel:
                if st.button("❌ Cancel", use_container_width=True, key="cancel_workout"):
                    st.session_state.show_workout_logger = False
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Nutrition Logger Modal
    if st.session_state.get("show_nutrition_logger", False):
        with st.container():
            st.markdown("<div class='section-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #00ff88;'>🥗 Log Nutrition</h3>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack", "Pre-Workout", "Post-Workout"], key="meal_type")
                meal_name = st.text_input("Meal Name", placeholder="e.g., Chicken & Rice", key="meal_name")
            
            with col2:
                calories_meal = st.number_input("Calories", 0, 2000, 500, key="meal_cals")
                protein = st.number_input("Protein (g)", 0, 200, 30, key="meal_protein")
            
            col3, col4 = st.columns(2)
            with col3:
                carbs = st.number_input("Carbs (g)", 0, 500, 60, key="meal_carbs")
            with col4:
                fats = st.number_input("Fats (g)", 0, 200, 20, key="meal_fats")
            
            col_log, col_cancel = st.columns(2)
            with col_log:
                if st.button("✅ Save Meal", use_container_width=True, key="save_meal"):
                    from datetime import datetime
                    nutrition_entry = {
                        "meal_type": meal_type,
                        "name": meal_name,
                        "calories": calories_meal,
                        "protein": protein,
                        "carbs": carbs,
                        "fats": fats,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    st.session_state.user_activities["nutrition_logs"].append(nutrition_entry)
                    st.session_state.show_nutrition_logger = False
                    st.success(f"✅ Meal logged! {calories_meal} calories")
                    st.rerun()
            
            with col_cancel:
                if st.button("❌ Cancel", use_container_width=True, key="cancel_meal"):
                    st.session_state.show_nutrition_logger = False
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Sleep Logger Modal
    if st.session_state.get("show_sleep_logger", False):
        with st.container():
            st.markdown("<div class='section-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #00ff88;'>😴 Log Sleep</h3>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                sleep_hours = st.number_input("Hours Slept", 3.0, 12.0, 8.0, 0.5, key="sleep_hours")
            with col2:
                sleep_quality = st.select_slider("Sleep Quality", ["Poor", "Fair", "Good", "Excellent"], value="Good", key="sleep_quality")
            
            col_log, col_cancel = st.columns(2)
            with col_log:
                if st.button("✅ Save Sleep", use_container_width=True, key="save_sleep"):
                    from datetime import datetime
                    sleep_entry = {
                        "hours": sleep_hours,
                        "quality": sleep_quality,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    st.session_state.user_activities["recovery_sessions"].append(sleep_entry)
                    stats['avg_sleep_hours'] = sleep_hours
                    st.session_state.show_sleep_logger = False
                    st.success(f"✅ Sleep logged! {sleep_hours:.1f} hours of {sleep_quality} sleep")
                    st.rerun()
            
            with col_cancel:
                if st.button("❌ Cancel", use_container_width=True, key="cancel_sleep"):
                    st.session_state.show_sleep_logger = False
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    
    # Recent Activity Feed
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>📝 Recent Activities</h2>", unsafe_allow_html=True)
    
    activities = st.session_state.user_activities
    
    # Display Recent Workouts
    if activities["workouts"]:
        st.markdown("<h3 style='color: #00ccff;'>💪 Latest Workouts</h3>", unsafe_allow_html=True)
        for i, workout in enumerate(reversed(activities["workouts"][-3:])):
            st.markdown(f"""
            <div class="activity-card">
                <div class="activity-title">{workout['type']} Session • {workout['intensity']}</div>
                <div class="activity-meta">⏱️ {workout['duration']} min | 🔥 {workout['calories']} calories</div>
                <div class="activity-stats">{workout['timestamp']}</div>
                {f'<div style="color: #00ccff; font-size: 12px; margin-top: 8px;"><strong>Note:</strong> {workout["notes"]}</div>' if workout['notes'] else ''}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📭 No workouts logged yet. Start by logging your first workout!")
    
    st.divider()
    
    # Display Recent Meals
    if activities["nutrition_logs"]:
        st.markdown("<h3 style='color: #00ccff;'>🥗 Recent Meals</h3>", unsafe_allow_html=True)
        for meal in reversed(activities["nutrition_logs"][-3:]):
            st.markdown(f"""
            <div class="activity-card">
                <div class="activity-title">{meal['meal_type']} • {meal['name']}</div>
                <div class="activity-meta">🔥 {meal['calories']} cal | P: {meal['protein']}g C: {meal['carbs']}g F: {meal['fats']}g</div>
                <div class="activity-stats">{meal['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # Progress Overview
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>📈 Weekly Progress</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="section-card">
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="color: #00ccff; font-weight: bold; margin-bottom: 10px;">Training Load</div>
            <div style="color: #00ff88; font-size: 24px; margin-bottom: 10px;">78%</div>
            <div style="background: linear-gradient(90deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 204, 255, 0.1) 100%); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 78%; height: 100%; background: linear-gradient(90deg, #00ff88 0%, #00ccff 100%); border-radius: 4px; box-shadow: 0 0 15px rgba(0, 255, 136, 0.5);"></div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="color: #00ccff; font-weight: bold; margin-bottom: 10px;">Nutrition Goals</div>
            <div style="color: #00ff88; font-size: 24px; margin-bottom: 10px;">85%</div>
            <div style="background: linear-gradient(90deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 204, 255, 0.1) 100%); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 85%; height: 100%; background: linear-gradient(90deg, #00ff88 0%, #00ccff 100%); border-radius: 4px; box-shadow: 0 0 15px rgba(0, 255, 136, 0.5);"></div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="color: #00ccff; font-weight: bold; margin-bottom: 10px;">Recovery Status</div>
            <div style="color: #00ff88; font-size: 24px; margin-bottom: 10px;">92%</div>
            <div style="background: linear-gradient(90deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 204, 255, 0.1) 100%); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 92%; height: 100%; background: linear-gradient(90deg, #00ff88 0%, #00ccff 100%); border-radius: 4px; box-shadow: 0 0 15px rgba(0, 255, 136, 0.5);"></div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============ PLANS PAGE ============
def plans_page():
    """Training, Nutrition, and Recovery Plans"""
    
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>🎯 Plan Generator</h2>", unsafe_allow_html=True)
    
    plan_tabs = st.tabs(["💪 Workouts", "🏥 Recovery", "⚡ Tactics", "🥗 Nutrition"])
    
    # ============ TAB 1: WORKOUTS ============
    with plan_tabs[0]:
        st.markdown("""
        <div class="section-card">
            <div class="section-header">💪 WORKOUT SYSTEM</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            sport = st.selectbox(
                "🏆 Your Sport",
                ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"],
                key="workout_sport"
            )
            position = st.text_input("📍 Your Position", placeholder="e.g., Midfielder, Fast Bowler", key="workout_pos")
        
        with col2:
            age = st.number_input("🎂 Age", 10, 25, 16, key="workout_age")
            intensity = st.select_slider(
                "⚡ Intensity Level",
                ["Light", "Moderate", "High", "Very High"],
                value="Moderate",
                key="workout_intensity"
            )
        
        goal = st.text_area(
            "🎯 Training Goal",
            placeholder="e.g., Build stamina, improve speed, increase strength",
            height=80,
            key="workout_goal"
        )
        
        # Progress indicator
        st.markdown("""
        <div class="progress-label">
            <span>Plan Customization</span>
            <span style="color: #00ff88;">100%</span>
        </div>
        <div class="intensity-bar" style="width: 100%;"></div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Generate Workout Plan", use_container_width=True, key="gen_workout"):
            if goal.strip():
                if not st.session_state.api_key:
                    st.error("❌ Please configure API Key in sidebar first!")
                else:
                    with st.spinner("🔮 Generating personalized workout plan..."):
                        prompt = f"""You are an expert youth sports coach for {sport}.

Create a detailed 6-week progressive workout plan for:
- Sport: {sport}
- Position: {position}
- Age: {age} years old
- Intensity: {intensity}
- Goal: {goal}

Provide:
1. Weekly training split (which muscles/focus each day)
2. Week 1 detailed workout (exercises, sets, reps, rest)
3. Progression guidelines for weeks 2-6
4. Injury prevention tips
5. Recovery protocols

Make it age-appropriate and safe."""
                        
                        try:
                            model = genai.GenerativeModel('gemini-2.0-flash')
                            response = model.generate_content(
                                prompt,
                                generation_config=genai.types.GenerationConfig(
                                    temperature=temperature,
                                    max_output_tokens=1500,
                                )
                            )
                            st.success("✅ Workout plan generated successfully!")
                            st.markdown("### 📋 Your Personalized Workout Plan")
                            st.markdown(response.text)
                        except Exception as e:
                            error_msg = str(e)
                            if "429" in error_msg or "quota" in error_msg.lower():
                                st.error("⚠️ **API Quota Exceeded**\n\nYou've exceeded the free tier limits. Please:\n1. Upgrade your Google API plan\n2. Wait for the quota to reset\n3. Check: https://ai.google.dev/gemini-api/docs/rate-limits")
                            else:
                                st.error(f"Error: {error_msg}")
            else:
                st.warning("⚠️ Please enter your training goal!")
    
    # ============ TAB 2: RECOVERY ============
    with plan_tabs[1]:
        st.markdown("""
        <div class="section-card">
            <div class="section-header">🏥 RECOVERY SYSTEM</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            sport_injury = st.selectbox(
                "🏆 Your Sport",
                ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"],
                key="recovery_sport"
            )
            recovery_stage = st.selectbox(
                "📍 Recovery Stage",
                ["Acute (0-3 days)", "Early Sub-acute (4-14 days)", "Late Sub-acute (2-8 weeks)", "Remodeling (8+ weeks)"]
            )
        
        with col2:
            injury = st.text_input("🤕 Injury Type", placeholder="e.g., Knee sprain, ankle strain", key="injury_type")
            previous = st.text_input("📜 Previous injuries? (optional)", placeholder="e.g., Sprained same ankle before", key="prev_injury")
        
        if st.button("🔧 Get Recovery Plan", use_container_width=True, key="gen_recovery"):
            if injury.strip():
                if not st.session_state.api_key:
                    st.error("❌ Please configure API Key in sidebar first!")
                else:
                    with st.spinner("🔮 Generating recovery protocol..."):
                        prompt = f"""You are a sports physiotherapist specializing in youth athlete recovery.

Create a safe, progressive recovery plan for:
- Sport: {sport_injury}
- Injury: {injury}
- Recovery Stage: {recovery_stage}
- Previous History: {previous if previous else "None"}

Provide:
1. Phase-specific exercises (with reps)
2. Pain management suggestions
3. Return-to-sport timeline
4. Exercises to avoid
5. Red flags to watch for
6. When to see a professional

⚠️ IMPORTANT: Emphasize consulting a physiotherapist."""
                        
                        try:
                            model = genai.GenerativeModel('gemini-2.0-flash')
                            response = model.generate_content(
                                prompt,
                                generation_config=genai.types.GenerationConfig(
                                    temperature=0.5,
                                    max_output_tokens=1500,
                                )
                            )
                            st.success("✅ Recovery plan generated successfully!")
                            st.markdown("### 🏃 Recovery & Rehabilitation Plan")
                            st.markdown(response.text)
                        except Exception as e:
                            error_msg = str(e)
                            if "429" in error_msg or "quota" in error_msg.lower():
                                st.error("⚠️ **API Quota Exceeded**\n\nYou've exceeded the free tier limits. Please:\n1. Upgrade your Google API plan\n2. Wait for the quota to reset\n3. Check: https://ai.google.dev/gemini-api/docs/rate-limits")
                            else:
                                st.error(f"Error: {error_msg}")
            else:
                st.warning("⚠️ Please describe your injury!")
    
    # ============ TAB 3: TACTICS ============
    with plan_tabs[2]:
        st.markdown("""
        <div class="section-card">
            <div class="section-header">⚡ TACTICAL ENGINE</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            sport_tactic = st.selectbox(
                "🏆 Your Sport",
                ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"],
                key="tactic_sport"
            )
            position_tactic = st.text_input("📍 Your Position", placeholder="e.g., Centre-back, Fast bowler", key="tactic_pos")
        
        with col2:
            skill = st.selectbox(
                "🎯 Skill to Improve",
                ["Ball Control", "Shooting", "Defense", "Passing", "Speed", "Decision Making", "Game IQ", "Set Plays"]
            )
            level = st.select_slider(
                "📈 Current Level",
                ["Beginner", "Intermediate", "Advanced", "Elite"],
                value="Intermediate",
                key="tactic_level"
            )
        
        challenge = st.text_area(
            "🔍 Specific Challenge",
            placeholder="e.g., Struggling with low crosses, footwork against faster defenders",
            height=80,
            key="tactic_challenge"
        )
        
        if st.button("📊 Get Tactical Analysis", use_container_width=True, key="gen_tactics"):
            if challenge.strip():
                if not st.session_state.api_key:
                    st.error("❌ Please configure API Key in sidebar first!")
                else:
                    with st.spinner("🔮 Analyzing your tactical challenges..."):
                        prompt = f"""You are a professional {sport_tactic} skills coach.

Provide tactical coaching for:
- Position: {position_tactic}
- Skill Focus: {skill}
- Current Level: {level}
- Challenge: {challenge}

Include:
1. Root cause analysis
2. 5-7 specific drills with instructions
3. Game scenarios and how to handle them
4. Mental tips to improve performance
5. Weekly progression (milestones)
6. Expected timeline for improvement

Make it practical and motivating for a young athlete."""
                        
                        try:
                            model = genai.GenerativeModel('gemini-2.0-flash')
                            response = model.generate_content(
                                prompt,
                                generation_config=genai.types.GenerationConfig(
                                    temperature=temperature,
                                    max_output_tokens=1500,
                                )
                            )
                            st.success("✅ Tactical plan generated successfully!")
                            st.markdown("### ⚡ Tactical Development Plan")
                            st.markdown(response.text)
                        except Exception as e:
                            error_msg = str(e)
                            if "429" in error_msg or "quota" in error_msg.lower():
                                st.error("⚠️ **API Quota Exceeded**\n\nYou've exceeded the free tier limits. Please:\n1. Upgrade your Google API plan\n2. Wait for the quota to reset\n3. Check: https://ai.google.dev/gemini-api/docs/rate-limits")
                            else:
                                st.error(f"Error: {error_msg}")
            else:
                st.warning("⚠️ Please describe your challenge!")
    
    # ============ TAB 4: NUTRITION ============
    with plan_tabs[3]:
        st.markdown("""
        <div class="section-card">
            <div class="section-header">🥗 NUTRITION OPTIMIZER</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            sport_nut = st.selectbox(
                "🏆 Your Sport",
                ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"],
                key="nut_sport"
            )
            position_nut = st.text_input("📍 Your Position", placeholder="e.g., Striker, Fast bowler", key="nut_pos")
            age_nut = st.number_input("🎂 Your Age", 10, 25, 16, key="nut_age")
        
        with col2:
            diet = st.selectbox(
                "🍽️ Diet Type",
                ["Vegetarian", "Non-vegetarian", "Vegan", "Pescatarian", "No preference"]
            )
            allergies = st.text_input("⚠️ Allergies/Intolerances (optional)", key="nut_allergies")
        
        nut_goal = st.selectbox(
            "🎯 Nutrition Goal",
            ["Build muscle", "Increase endurance", "Weight management", "Speed & power", "Recovery", "General health"]
        )
        
        if st.button("🍎 Generate Nutrition Plan", use_container_width=True, key="gen_nutrition"):
            if not st.session_state.api_key:
                st.error("❌ Please configure API Key in sidebar first!")
            else:
                with st.spinner("🔮 Creating personalized nutrition plan..."):
                    prompt = f"""You are a sports nutritionist specializing in youth athletes.

Create a personalized nutrition plan for:
- Sport: {sport_nut}
- Position: {position_nut}
- Age: {age_nut}
- Diet Type: {diet}
- Allergies: {allergies if allergies else "None"}
- Goal: {nut_goal}

Provide:
1. Daily macronutrient breakdown (exact grams)
2. Complete meal plan (all meals + snacks)
3. Sample rest day meal plan
4. Pre-match nutrition strategy
5. Hydration schedule
6. Recovery nutrition tips
7. Foods to prioritize and avoid

Make it practical and age-appropriate for a {age_nut}-year-old."""
                    
                    try:
                        model = genai.GenerativeModel('gemini-2.0-flash')
                        response = model.generate_content(
                            prompt,
                            generation_config=genai.types.GenerationConfig(
                                temperature=0.6,
                                max_output_tokens=1500,
                            )
                        )
                        st.success("✅ Nutrition plan generated successfully!")
                        st.markdown("### 🥗 Personalized Nutrition Plan")
                        st.markdown(response.text)
                    except Exception as e:
                        error_msg = str(e)
                        if "429" in error_msg or "quota" in error_msg.lower():
                            st.error("⚠️ **API Quota Exceeded**\n\nYou've exceeded the free tier limits. Please:\n1. Upgrade your Google API plan\n2. Wait for the quota to reset\n3. Check: https://ai.google.dev/gemini-api/docs/rate-limits")
                        else:
                            st.error(f"Error: {error_msg}")

# ============ PERFORMANCE PAGE ============
def performance_page():
    """Performance insights and analytics based on real user data"""
    
    activities = st.session_state.user_activities
    stats = activities["stats"]
    
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>📈 Performance Analytics</h2>", unsafe_allow_html=True)
    
    # Top metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{len(activities['workouts'])}</div>
            <div class="stat-label">🏋️ Total Workouts</div>
            <div class="stat-delta">This session</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{stats['total_calories_burned']}</div>
            <div class="stat-label">🔥 Calories Burned</div>
            <div class="stat-delta">Peak performance</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{stats['current_streak']}</div>
            <div class="stat-label">💪 Day Streak</div>
            <div class="stat-delta">{'Keep going!' if stats['current_streak'] > 0 else 'Start today!'}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("<h3 style='color: #00ccff; font-family: Orbitron, monospace;'>📊 Your Workouts</h3>", unsafe_allow_html=True)
    
    if activities["workouts"]:
        # Workout breakdown by type
        workout_types = {}
        for w in activities["workouts"]:
            workout_types[w['type']] = workout_types.get(w['type'], 0) + 1
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4 style='color: #00ff88;'>Workout Breakdown</h4>", unsafe_allow_html=True)
            for wtype, count in sorted(workout_types.items(), key=lambda x: x[1], reverse=True):
                st.markdown(f"""
                <div class="activity-card">
                    <div class="activity-title">{wtype}</div>
                    <div class="activity-meta">Sessions: {count}</div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h4 style='color: #00ff88;'>Intensity Distribution</h4>", unsafe_allow_html=True)
            intensity_count = {}
            for w in activities["workouts"]:
                intensity_count[w['intensity']] = intensity_count.get(w['intensity'], 0) + 1
            
            for intensity, count in sorted(intensity_count.items()):
                st.markdown(f"""
                <div class="activity-card">
                    <div class="activity-title">⚡ {intensity}</div>
                    <div class="activity-meta">{count} sessions</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.divider()
        
        # Detailed workout history
        st.markdown("<h4 style='color: #00ccff;'>Detailed Workout History</h4>", unsafe_allow_html=True)
        
        for workout in reversed(activities["workouts"]):
            st.markdown(f"""
            <div class="activity-card">
                <div class="activity-title">{workout['type']} • {workout['intensity']}</div>
                <div class="activity-meta">⏱️ {workout['duration']} min | 🔥 {workout['calories']} cal | 🎯 {workout.get('notes', 'No notes')}</div>
                <div class="activity-stats">{workout['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📭 No workouts logged yet. Log your first workout to see analytics!")
    
    st.divider()
    
    st.markdown("<h3 style='color: #00ccff; font-family: Orbitron, monospace;'>🥗 Nutrition Summary</h3>", unsafe_allow_html=True)
    
    if activities["nutrition_logs"]:
        total_cals = sum([m['calories'] for m in activities["nutrition_logs"]])
        total_protein = sum([m['protein'] for m in activities["nutrition_logs"]])
        total_carbs = sum([m['carbs'] for m in activities["nutrition_logs"]])
        total_fats = sum([m['fats'] for m in activities["nutrition_logs"]])
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="premium-stat-card">
                <div class="stat-number">{total_cals}</div>
                <div class="stat-label">🔥 Total Calories</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="premium-stat-card">
                <div class="stat-number">{total_protein:.0f}g</div>
                <div class="stat-label">🥚 Protein</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="premium-stat-card">
                <div class="stat-number">{total_carbs:.0f}g</div>
                <div class="stat-label">🌾 Carbs</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="premium-stat-card">
                <div class="stat-number">{total_fats:.0f}g</div>
                <div class="stat-label">🧈 Fats</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("<h4 style='color: #00ccff;'>Recent Meals</h4>", unsafe_allow_html=True)
        
        for meal in reversed(activities["nutrition_logs"]):
            st.markdown(f"""
            <div class="activity-card">
                <div class="activity-title">{meal['meal_type']} • {meal['name']}</div>
                <div class="activity-meta">🔥 {meal['calories']} cal | P: {meal['protein']}g | C: {meal['carbs']}g | F: {meal['fats']}g</div>
                <div class="activity-stats">{meal['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📭 No nutrition logs yet. Start logging meals to see your nutrition analytics!")
    
    st.divider()
    
    st.markdown("<h3 style='color: #00ccff; font-family: Orbitron, monospace;'>😴 Recovery Insights</h3>", unsafe_allow_html=True)
    
    if activities["recovery_sessions"]:
        avg_sleep = sum([r['hours'] for r in activities["recovery_sessions"]]) / len(activities["recovery_sessions"])
        
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{avg_sleep:.1f}h</div>
            <div class="stat-label">😴 Average Sleep</div>
            <div class="stat-delta">{len(activities['recovery_sessions'])} nights logged</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h4 style='color: #00ccff;'>Sleep History</h4>", unsafe_allow_html=True)
        
        for sleep in reversed(activities["recovery_sessions"]):
            st.markdown(f"""
            <div class="activity-card">
                <div class="activity-title">Sleep • {sleep['quality']}</div>
                <div class="activity-meta">⏱️ {sleep['hours']:.1f} hours</div>
                <div class="activity-stats">{sleep['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📭 No sleep logs yet. Track your sleep to monitor recovery!")

# ============ HELP PAGE ============
def help_page():
    """Help and support center"""
    
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>💬 Support Center</h2>", unsafe_allow_html=True)
    
    help_topics = {
        "🏋️ How to use Workouts?": "The Workout tab helps you generate personalized 6-week training plans. Select your sport, position, age, and intensity level. Describe your training goal and the AI will create a detailed progressive plan with exercises, sets, reps, and recovery protocols.",
        "🏥 Recovery & Injury Help": "Use the Recovery tab to get personalized injury management plans. Select your sport, describe the injury, and choose the recovery stage. The AI provides phase-specific exercises and return-to-sport guidance.",
        "⚡ Tactical Development": "The Tactics tab helps improve specific skills. Choose your position, select a skill to work on (shooting, passing, defense, etc.), and describe your challenge. Get detailed drills and game scenarios.",
        "🥗 Nutrition Guide": "Get a personalized nutrition plan based on your sport, goals, age, and dietary preferences. The plan includes daily macros, meal plans, pre-match nutrition, and hydration strategies.",
        "📊 Performance Tracking": "Track your athletic performance metrics over time. Set goals and monitor progress with detailed analytics.",
        "🔐 API Quota Issues": "Free tier has limited requests. To avoid quota errors, upgrade your Google API plan at https://ai.google.dev/pricing",
        "❔ Ask Custom Question": "Ask anything about using CoachBot AI or get sports coaching advice!"
    }
    
    selected_topic = st.selectbox(
        "📚 Select a topic or ask a question:",
        list(help_topics.keys())
    )
    
    if selected_topic:
        if selected_topic == "❔ Ask Custom Question":
            st.markdown("<h3 style='color: #00ccff;'>Ask AI Coach</h3>", unsafe_allow_html=True)
            user_question = st.text_input(
                "Your question:",
                placeholder="e.g., What's the best warm-up routine?"
            )
            
            if user_question and st.session_state.api_key:
                if st.button("🔍 Get AI Answer"):
                    with st.spinner("Thinking..."):
                        try:
                            model = genai.GenerativeModel('gemini-2.0-flash')
                            prompt = f"""You are a helpful sports coaching assistant for CoachBot AI app.
Answer this user question briefly and practically:

Question: {user_question}

Provide a concise, helpful answer focused on youth sports coaching."""
                            
                            response = model.generate_content(prompt)
                            st.success("✅ AI Response:")
                            st.markdown(response.text)
                        except Exception as e:
                            error_msg = str(e)
                            if "429" in error_msg or "quota" in error_msg.lower():
                                st.error("⚠️ **API Quota Exceeded**\n\nPlease upgrade your Google API plan.")
                            else:
                                st.error(f"Error: {error_msg}")
            elif user_question and not st.session_state.api_key:
                st.error("❌ Please configure API Key in sidebar first!")
        else:
            st.markdown(f"<h3 style='color: #00ccff;'>{selected_topic}</h3>", unsafe_allow_html=True)
            st.markdown(help_topics[selected_topic])
    
    st.divider()
    
    st.markdown("<h3 style='color: #00ff88;'>📚 Documentation</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Getting Started**
        - Create Profile
        - Set Your Goals
        - Configure API
        """)
    
    with col2:
        st.markdown("""
        **Features**
        - Generate Plans
        - Track Progress
        - Get Analytics
        """)
    
    with col3:
        st.markdown("""
        **Resources**
        - API Docs
        - Rate Limits
        - Upgrade Plans
        """)

# ============ ACHIEVEMENTS & BADGES PAGE ============
def achievements_page():
    """Gamification with badges, achievements, and progress tracking"""
    
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>🏆 Achievements & Badges</h2>", unsafe_allow_html=True)
    
    badges = st.session_state.user_badges
    activities = st.session_state.user_activities
    
    # Update badges based on activities
    if len(activities["workouts"]) >= 1 and not badges["first_workouts"]:
        badges["first_workouts"] = True
        st.balloons()
    
    if len(activities["workouts"]) >= 7 and not badges["week_warrior"]:
        badges["week_warrior"] = True
    
    if activities["stats"]["total_calories_burned"] >= 5000 and not badges["calorie_crusher"]:
        badges["calorie_crusher"] = True
    
    if len(activities["nutrition_logs"]) >= 10 and not badges["nutrition_master"]:
        badges["nutrition_master"] = True
    
    if activities["stats"]["current_streak"] >= 7 and not badges["streak_champion"]:
        badges["streak_champion"] = True
    
    if len(activities["recovery_sessions"]) >= 5 and not badges["recovery_king"]:
        badges["recovery_king"] = True
    
    st.markdown("<h3 style='color: #00ccff;'>🎖️ Your Badges</h3>", unsafe_allow_html=True)
    
    badge_list = [
        {"name": "🚀 First Workout", "unlocked": badges["first_workouts"], "desc": "Complete your first workout"},
        {"name": "⚡ Week Warrior", "unlocked": badges["week_warrior"], "desc": "Complete 7 workouts"},
        {"name": "🔥 Calorie Crusher", "unlocked": badges["calorie_crusher"], "desc": "Burn 5,000+ calories"},
        {"name": "🥗 Nutrition Master", "unlocked": badges["nutrition_master"], "desc": "Log 10 meals"},
        {"name": "🔥 Streak Champion", "unlocked": badges["streak_champion"], "desc": "7-day streak"},
        {"name": "😴 Recovery King", "unlocked": badges["recovery_king"], "desc": "Log 5 sleep sessions"},
    ]
    
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    for idx, badge in enumerate(badge_list):
        with cols[idx % 3]:
            status = "✅ UNLOCKED" if badge["unlocked"] else "🔒 LOCKED"
            color = "#00ff88" if badge["unlocked"] else "#666"
            
            st.markdown(f"""
            <div class="activity-card" style="border-color: {color};">
                <div class="activity-title">{badge['name']}</div>
                <div class="activity-meta">{badge['desc']}</div>
                <div style="color: {color}; font-weight: bold; margin-top: 8px; font-size: 12px;">{status}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # Stats Overview
    st.markdown("<h3 style='color: #00ccff;'>📈 Your Milestones</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{len(activities['workouts'])}</div>
            <div class="stat-label">💪 Workouts</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{activities['stats']['total_calories_burned']}</div>
            <div class="stat-label">🔥 Calories</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{len(activities['nutrition_logs'])}</div>
            <div class="stat-label">🥗 Meals</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="premium-stat-card">
            <div class="stat-number">{len(activities['recovery_sessions'])}</div>
            <div class="stat-label">😴 Sleep</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Goals Prediction (ML-based)
    st.markdown("<h3 style='color: #00ff88;'>🎯 Smart Goal Predictions</h3>", unsafe_allow_html=True)
    
    if len(activities["workouts"]) > 0:
        avg_calories = activities["stats"]["total_calories_burned"] / len(activities["workouts"])
        predicted_weekly_burn = avg_calories * 7
        
        st.markdown(f"""
        <div class="activity-card">
            <div class="activity-title">📊 Weekly Projection</div>
            <div class="activity-meta">Based on your current pace</div>
            <div style="color: #00ff88; font-size: 20px; font-weight: bold; margin-top: 10px;">
                {predicted_weekly_burn:.0f} calories/week
            </div>
            <div style="color: #00ccff; font-size: 12px; margin-top: 8px;">
                Average per workout: {avg_calories:.0f} cal
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============ COMMUNITY PAGE ============
def community_page():
    """Social features, leaderboards, and community challenges"""
    
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>👥 Community & Challenges</h2>", unsafe_allow_html=True)
    
    community_tabs = st.tabs(["🏆 Leaderboard", "🎯 Challenges", "👥 Friends"])
    
    with community_tabs[0]:
        st.markdown("<h3 style='color: #00ccff;'>⭐ Global Leaderboard</h3>", unsafe_allow_html=True)
        
        # Simulated leaderboard
        leaderboard = [
            {"rank": 1, "name": "Elite Athlete", "workouts": 47, "calories": 28500, "streak": 45},
            {"rank": 2, "name": "Fitness Master", "workouts": 42, "calories": 25300, "streak": 38},
            {"rank": 3, "name": st.session_state.user_name, "workouts": len(st.session_state.user_activities["workouts"]), "calories": st.session_state.user_activities["stats"]["total_calories_burned"], "streak": st.session_state.user_activities["stats"]["current_streak"]},
            {"rank": 4, "name": "Power Lifter", "workouts": 25, "calories": 18200, "streak": 22},
            {"rank": 5, "name": "Marathon Runner", "workouts": 38, "calories": 32100, "streak": 35},
        ]
        
        for athlete in leaderboard:
            medal = "🥇" if athlete["rank"] == 1 else "🥈" if athlete["rank"] == 2 else "🥉" if athlete["rank"] == 3 else "⭐"
            highlight = "border: 2px solid #00ff88;" if athlete["name"] == st.session_state.user_name else ""
            
            st.markdown(f"""
            <div class="activity-card" style="{highlight}">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div class="activity-title">{medal} #{athlete['rank']} {athlete['name']}</div>
                        <div class="activity-meta">💪 {athlete['workouts']} | 🔥 {athlete['calories']} cal | 🔥 {athlete['streak']}d</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with community_tabs[1]:
        st.markdown("<h3 style='color: #00ccff;'>🎯 Active Challenges</h3>", unsafe_allow_html=True)
        
        challenges = st.session_state.community_challenges
        
        challenges_list = [
            {"name": "Step Master Challenge", "icon": "🚶", "goal": 100000, "key": "monthly_step", "unit": "steps"},
            {"name": "Calorie Blitz", "icon": "🔥", "goal": 50000, "key": "calorie_burn", "unit": "calories"},
            {"name": "Hydration Hero", "icon": "💧", "goal": 240, "key": "hydration_hero", "unit": "cups"},
            {"name": "Sleep Master", "icon": "😴", "goal": 56, "key": "sleep_master", "unit": "hours"},
        ]
        
        col1, col2 = st.columns(2)
        
        for idx, challenge in enumerate(challenges_list):
            with [col1, col2][idx % 2]:
                progress = 0
                if challenge["key"] == "monthly_step":
                    progress = len(st.session_state.user_activities["workouts"]) * 5000
                elif challenge["key"] == "calorie_burn":
                    progress = st.session_state.user_activities["stats"]["total_calories_burned"]
                elif challenge["key"] == "hydration_hero":
                    progress = st.session_state.user_activities["stats"]["hydration_cups"]
                elif challenge["key"] == "sleep_master":
                    progress = st.session_state.user_activities["stats"]["avg_sleep_hours"] * 7
                
                percent = min(100, int((progress / challenge["goal"]) * 100))
                
                st.markdown(f"""
                <div class="activity-card">
                    <div class="activity-title">{challenge['icon']} {challenge['name']}</div>
                    <div class="activity-meta">{progress:.0f} / {challenge['goal']} {challenge['unit']}</div>
                    <div style="background: linear-gradient(90deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 204, 255, 0.1) 100%); height: 8px; border-radius: 4px; margin: 10px 0; overflow: hidden;">
                        <div style="width: {percent}%; height: 100%; background: linear-gradient(90deg, #00ff88 0%, #00ccff 100%); border-radius: 4px;"></div>
                    </div>
                    <div style="color: #00ff88; font-weight: bold; font-size: 12px;">{percent}% Complete</div>
                </div>
                """, unsafe_allow_html=True)
    
    with community_tabs[2]:
        st.markdown("<h3 style='color: #00ccff;'>👥 Friends Leaderboard</h3>", unsafe_allow_html=True)
        
        st.info("👋 Add friends to see their activity and compete together!")
        
        col1, col2 = st.columns(2)
        with col1:
            friend_name = st.text_input("Friend Username", placeholder="e.g., John_Fitness", key="friend_add")
        with col2:
            if st.button("➕ Add Friend", use_container_width=True):
                st.success(f"✅ Friend request sent to {friend_name}!")
        
        st.divider()
        
        st.markdown("<h4 style='color: #00ff88;'>Your Friends</h4>", unsafe_allow_html=True)
        
        friends = [
            {"name": "Champion", "workouts": 35, "streak": 28},
            {"name": "Fitness Pro", "workouts": 31, "streak": 21},
        ]
        
        for friend in friends:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                <div class="activity-card">
                    <div class="activity-title">👤 {friend['name']}</div>
                    <div class="activity-meta">💪 {friend['workouts']} workouts | 🔥 {friend['streak']}d streak</div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                if st.button("💬", key=f"msg_{friend['name']}", help="Send message"):
                    st.success("Message sent!")

# ============ AI COACH PAGE ============
def ai_coach_page():
    """Advanced AI coaching assistant that learns from user data"""
    
    st.markdown("<h2 style='color: #00ff88; font-family: Orbitron, monospace;'>🤖 Advanced AI Coach</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card" style="text-align: center;">
        <div style="font-size: 60px; margin-bottom: 10px;">🏋️‍♂️</div>
        <div style="color: #00ff88; font-size: 18px; font-weight: bold;">Your Personal AI Training Partner</div>
        <div style="color: #00ccff; font-size: 13px; margin-top: 5px;">Learns from your data. Adapts to your performance.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # AI Coach Analysis
    activities = st.session_state.user_activities
    
    if len(activities["workouts"]) > 0:
        st.markdown("<h3 style='color: #00ccff;'>💬 Coach Insights</h3>", unsafe_allow_html=True)
        
        # Generate AI insights based on user data
        total_workouts = len(activities["workouts"])
        avg_duration = sum([w["duration"] for w in activities["workouts"]]) / len(activities["workouts"])
        avg_intensity = "High" if len([w for w in activities["workouts"] if w["intensity"] == "High"]) > len(activities["workouts"]) / 2 else "Moderate"
        
        insights = [
            f"🔥 You've completed {total_workouts} workouts! That's excellent progress.",
            f"⏱️ Your average workout duration is {avg_duration:.0f} minutes. Great consistency!",
            f"💪 You're training at {avg_intensity} intensity. Perfect for building strength.",
            f"🎯 Keep your streak alive! You're on a {activities['stats']['current_streak']}-day streak.",
            f"💡 Pro tip: Mix up your workout types to prevent plateaus and stay motivated."
        ]
        
        for insight in insights:
            st.markdown(f"""
            <div class="activity-card">
                <div style="color: #00ff88; font-weight: bold;">{insight}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("<h3 style='color: #00ccff;'>🎙️ Ask Your AI Coach</h3>", unsafe_allow_html=True)
        
        coach_question = st.text_input(
            "Ask anything about your training, nutrition, or recovery:",
            placeholder="e.g., Should I rest today or workout?",
            key="coach_question"
        )
        
        if coach_question and st.session_state.api_key:
            if st.button("🤖 Get AI Advice", use_container_width=True):
                with st.spinner("🤔 AI Coach thinking..."):
                    try:
                        model = genai.GenerativeModel('gemini-2.0-flash')
                        
                        # Include user context in prompt
                        user_context = f"""
The user has completed {total_workouts} workouts with average duration {avg_duration:.0f} minutes.
They've logged {len(activities['nutrition_logs'])} meals and have a {activities['stats']['current_streak']}-day streak.
They've burned {activities['stats']['total_calories_burned']} calories total.
Current question: {coach_question}
"""
                        
                        prompt = f"""You are an elite sports coach with deep knowledge of fitness, training, nutrition, and recovery. 
Based on this athlete's data:
{user_context}

Provide personalized, actionable advice. Be encouraging and specific to their situation."""
                        
                        response = model.generate_content(prompt)
                        
                        st.markdown(f"""
                        <div class="activity-card" style="border-color: #00ff88;">
                            <div class="activity-title">🏆 Coach's Advice</div>
                            <div style="color: #e0e0e0; margin-top: 10px;">{response.text}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Add to memory
                        st.session_state.ai_coach_memory.append({
                            "question": coach_question,
                            "answer": response.text
                        })
                        
                    except Exception as e:
                        error_msg = str(e)
                        if "429" in error_msg or "quota" in error_msg.lower():
                            st.error("⚠️ API quota exceeded. Please upgrade or try later.")
                        else:
                            st.error(f"Error: {error_msg}")
        elif coach_question and not st.session_state.api_key:
            st.error("❌ Please configure API Key in sidebar first!")
    
    else:
        st.info("📭 Log some workouts first for personalized coaching!")

# ============ PAGE ROUTING ============
if st.session_state.current_page == "Dashboard":
    dashboard_page()
elif st.session_state.current_page == "Plans":
    plans_page()
elif st.session_state.current_page == "Performance":
    performance_page()
elif st.session_state.current_page == "Achievements":
    achievements_page()
elif st.session_state.current_page == "Community":
    community_page()
elif st.session_state.current_page == "AICoach":
    ai_coach_page()
elif st.session_state.current_page == "Help":
    help_page()

# ============ FOOTER ============
st.divider()
st.markdown("""
<div style="text-align: center; padding: 20px; margin-top: 40px;">
<h3 style="font-family: Orbitron, monospace; color: #00ff88; text-transform: uppercase; letter-spacing: 2px;">⚽ COACHBOT AI ⚽</h3>
<p style="color: #00ccff; font-size: 14px;">Professional AI-Powered Youth Sports Training System</p>
<p style="color: rgba(224, 224, 224, 0.6); font-size: 12px; margin-top: 15px;">⚠️ <strong>DISCLAIMER:</strong> General guidance only. Always consult professional coaches and healthcare providers.</p>
<p style="color: #00ff88; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-top: 10px;">Version 2.0 • Powered by Google Gemini AI</p>
</div>
""", unsafe_allow_html=True)

