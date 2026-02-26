import streamlit as st
import google.generativeai as genai

# Configure page
st.set_page_config(
    page_title="CoachBot AI - Youth Sports Assistant",
    page_icon="⚽",
    layout="wide"
)

# Initialize login session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}

# ============ SIGNUP PAGE ============
def signup_page():
    """Display the fancy signup page"""
    # Custom CSS for signup page
    st.markdown("""
    <style>
    .signup-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 60px 80px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        text-align: center;
        max-width: 500px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="signup-box">', unsafe_allow_html=True)
        
        # Logo/Title
        st.markdown('<h1 style="text-align: center; color: transparent; background: linear-gradient(135deg, #00ff88 0%, #ffff00 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 48px; margin-bottom: 5px;">⚽ CoachBot AI</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: rgba(255, 255, 255, 0.8); font-size: 14px; margin-bottom: 40px;">Create Your Account</p>', unsafe_allow_html=True)
        
        st.divider()
        
        # Signup form
        new_username = st.text_input(
            "👤 Choose Username",
            placeholder="At least 3 characters",
            key="signup_username"
        )
        
        new_email = st.text_input(
            "📧 Email",
            placeholder="your@email.com",
            key="signup_email"
        )
        
        new_password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="At least 4 characters",
            key="signup_password"
        )
        
        confirm_password = st.text_input(
            "🔐 Confirm Password",
            type="password",
            placeholder="Re-enter password",
            key="signup_confirm_password"
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("✅ Sign Up", key="signup_btn", use_container_width=True):
                if not new_username or not new_email or not new_password or not confirm_password:
                    st.error("❌ Please fill all fields!")
                elif len(new_username) < 3:
                    st.error("❌ Username must be at least 3 characters!")
                elif "@" not in new_email:
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
                    st.success("✅ Account created successfully! Please login.")
                    st.session_state.show_signup = False
                    st.rerun()
        
        with col_b:
            if st.button("🔙 Back to Login", key="back_to_login", use_container_width=True):
                st.session_state.show_signup = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# ============ LOGIN PAGE ============
def login_page():
    """Display the fancy login page"""
    # Custom CSS for login page
    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }
    .login-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 60px 80px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        text-align: center;
        max-width: 500px;
    }
    .login-title {
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #00ff88 0%, #ffff00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .login-subtitle {
        font-size: 16px;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 50px;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 12px;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #00ff88;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        font-weight: bold;
        background: linear-gradient(135deg, #00ff88 0%, #00ccff 100%);
        color: black;
        border: none;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 255, 136, 0.4);
    }
    .signup-link {
        margin-top: 20px;
        font-size: 14px;
        color: rgba(255, 255, 255, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create centered login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # Left side sports symbols
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 40px 10px; font-size: 50px;">
            <div>🏀</div>
            <div style="margin: 30px 0;">🏈</div>
            <div style="margin: 30px 0;">⚾</div>
            <div style="margin: 30px 0;">🎾</div>
            <div style="margin: 30px 0;">🏐</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Center login form
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        
        # Fitness image on top
        st.markdown("""
        <div style="text-align: center; font-size: 80px; margin-bottom: 20px; animation: bounce 2s infinite;">
            💪
        </div>
        <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Logo/Title
        st.markdown('<h1 style="text-align: center; color: transparent; background: linear-gradient(135deg, #00ff88 0%, #ffff00 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 48px; margin-bottom: 5px;">⚽ CoachBot AI</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: rgba(255, 255, 255, 0.8); font-size: 14px; margin-bottom: 40px;">Your Personal Youth Sports Coach</p>', unsafe_allow_html=True)
        
        st.divider()
        
        # Login form
        username = st.text_input(
            "👤 Username",
            placeholder="Enter your username",
            key="login_username"
        )
        
        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🚀 Login", key="login_btn", use_container_width=True):
                if username and password:
                    # Check if user is registered
                    if username in st.session_state.registered_users:
                        if st.session_state.registered_users[username]["password"] == password:
                            st.session_state.logged_in = True
                            st.session_state.user_name = username
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            st.error("❌ Incorrect password!")
                    else:
                        st.error("❌ User not found! Please sign up first.")
                else:
                    st.warning("⚠️ Please enter both username and password!")
        
        with col_b:
            if st.button("📝 Sign Up", key="signup_link_btn", use_container_width=True):
                st.session_state.show_signup = True
                st.rerun()
        
        st.markdown('<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 12px; margin-top: 30px;">Demo: Create new account or use test/test1234</p>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Right side sports symbols
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 40px 10px; font-size: 50px;">
            <div>🏒</div>
            <div style="margin: 30px 0;">🏑</div>
            <div style="margin: 30px 0;">🏓</div>
            <div style="margin: 30px 0;">⛳</div>
            <div style="margin: 30px 0;">🥊</div>
        </div>
        """, unsafe_allow_html=True)

# Show login/signup page if not logged in
if not st.session_state.logged_in:
    if st.session_state.show_signup:
        signup_page()
    else:
        login_page()
    st.stop()

# ============ MAIN APP (shown after login) ============

# Title
st.title("⚽ CoachBot AI - Personalized Youth Sports Assistant")
st.markdown("**Empowering young athletes with AI-driven coaching** 🚀")

# Initialize session state for api_key
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# Logout button in sidebar and API configuration
with st.sidebar:
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
    st.divider()
    
    # API Key Configuration (compact)
    st.subheader("🔑 API Configuration")
    api_key = st.text_input(
        "Google API Key",
        type="password",
        placeholder="Paste your API key here",
        help="Get from https://aistudio.google.com/app/apikey",
        key="sidebar_api_key"
    )
    
    if api_key:
        st.session_state.api_key = api_key
        try:
            genai.configure(api_key=api_key)
            st.success("✅ API Key configured!")
        except:
            st.error("❌ Invalid API Key")
    
    st.divider()
    
    # ============ AI HELP ASSISTANT ============
    st.header("💬 AI Help Assistant")
    
    # Initialize chat history for help assistant
    if "help_chat_history" not in st.session_state:
        st.session_state.help_chat_history = []
    
    # Help topics
    help_topics = {
        "🏋️ How to use Workouts?": "The Workout tab helps you generate personalized 6-week training plans. Select your sport, position, age, and intensity level. Describe your training goal and the AI will create a detailed progressive plan with exercises, sets, reps, and recovery protocols.",
        "🏥 Recovery & Injury Help": "Use the Recovery tab to get personalized injury management plans. Select your sport, describe the injury, and choose the recovery stage. The AI provides phase-specific exercises and return-to-sport guidance.",
        "⚡ Tactical Development": "The Tactics tab helps improve specific skills. Choose your position, select a skill to work on (shooting, passing, defense, etc.), and describe your challenge. Get detailed drills and game scenarios.",
        "🥗 Nutrition Guide": "Get a personalized nutrition plan based on your sport, goals, age, and dietary preferences. The plan includes daily macros, meal plans, pre-match nutrition, and hydration strategies.",
        "📊 Profile Setup": "Save your athlete profile with basic info, physical metrics, goals, and injury history. This helps personalize all recommendations across the app.",
        "🔧 How to get API Key?": "Visit https://aistudio.google.com/app/apikey, sign in with your Google account, create a new API key, and paste it in the Settings section above.",
        "❔ Ask Custom Question": "Ask anything about using CoachBot AI or get sports coaching advice!"
    }
    
    # Display quick help buttons
    st.subheader("Quick Help Topics")
    selected_topic = st.selectbox(
        "Need help with something?",
        list(help_topics.keys()),
        label_visibility="collapsed"
    )
    
    # Show answer for selected topic
    if selected_topic:
        if selected_topic == "❔ Ask Custom Question":
            user_question = st.text_input(
                "Ask your question:",
                placeholder="e.g., What's the best warm-up routine?"
            )
            
            if user_question and st.session_state.api_key:
                if st.button("🔍 Get AI Answer", key="custom_help"):
                    with st.spinner("Finding answer..."):
                        try:
                            model = genai.GenerativeModel('gemini-pro')
                            prompt = f"""You are a helpful sports coaching assistant for CoachBot AI app.
Answer this user question briefly and practically:

Question: {user_question}

Provide a concise, helpful answer focused on youth sports coaching."""
                            
                            response = model.generate_content(prompt)
                            
                            # Add to chat history
                            st.session_state.help_chat_history.append(("user", user_question))
                            st.session_state.help_chat_history.append(("assistant", response.text))
                            
                            st.markdown("### 💡 Answer")
                            st.markdown(response.text)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        else:
            st.info(help_topics[selected_topic])

# Set default values
temperature = 0.7

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💪 Workouts",
    "🏥 Recovery",
    "⚡ Tactics",
    "🥗 Nutrition",
    "📊 Profile"
])

# ============ TAB 1: WORKOUTS ============
with tab1:
    st.header("💪 Custom Workout Plans")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sport = st.selectbox(
            "Your Sport",
            ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"]
        )
        position = st.text_input("Your Position", placeholder="e.g., Midfielder, Fast Bowler")
    
    with col2:
        age = st.number_input("Age", 10, 25, 16)
        intensity = st.select_slider(
            "Intensity",
            ["Light", "Moderate", "High", "Very High"],
            value="Moderate"
        )
    
    goal = st.text_area(
        "Training Goal",
        placeholder="e.g., Build stamina, improve speed, increase strength",
        height=80
    )
    
    if st.button("🎯 Generate Workout Plan"):
        if goal.strip():
            with st.spinner("Generating workout plan..."):
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
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(
                        prompt,
                        generation_config=genai.types.GenerationConfig(
                            temperature=temperature,
                            max_output_tokens=1000,
                        )
                    )
                    st.markdown("### 📋 Your Workout Plan")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter your training goal!")

# ============ TAB 2: RECOVERY ============
with tab2:
    st.header("🏥 Recovery & Injury Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sport_injury = st.selectbox(
            "Your Sport",
            ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"],
            key="recovery_sport"
        )
        recovery_stage = st.selectbox(
            "Recovery Stage",
            ["Acute (0-3 days)", "Early Sub-acute (4-14 days)", "Late Sub-acute (2-8 weeks)", "Remodeling (8+ weeks)"]
        )
    
    with col2:
        injury = st.text_input("Injury Type", placeholder="e.g., Knee sprain, ankle strain")
        previous = st.text_input("Previous injuries? (optional)", placeholder="e.g., Sprained same ankle before")
    
    if st.button("🔧 Get Recovery Plan"):
        if injury.strip():
            with st.spinner("Generating recovery plan..."):
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
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(
                        prompt,
                        generation_config=genai.types.GenerationConfig(
                            temperature=0.5,
                            max_output_tokens=1000,
                        )
                    )
                    st.markdown("### 🏃 Recovery Plan")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please describe your injury!")

# ============ TAB 3: TACTICS ============
with tab3:
    st.header("⚡ Tactical & Skills Development")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sport_tactic = st.selectbox(
            "Your Sport",
            ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"],
            key="tactic_sport"
        )
        position_tactic = st.text_input("Your Position", placeholder="e.g., Centre-back, Fast bowler")
    
    with col2:
        skill = st.selectbox(
            "Skill to Improve",
            ["Ball Control", "Shooting", "Defense", "Passing", "Speed", "Decision Making", "Game IQ", "Set Plays"]
        )
        level = st.select_slider(
            "Current Level",
            ["Beginner", "Intermediate", "Advanced", "Elite"],
            value="Intermediate"
        )
    
    challenge = st.text_area(
        "Specific Challenge",
        placeholder="e.g., Struggling with low crosses, footwork against faster defenders",
        height=80
    )
    
    if st.button("📊 Get Tactical Analysis"):
        if challenge.strip():
            with st.spinner("Generating tactical advice..."):
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
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(
                        prompt,
                        generation_config=genai.types.GenerationConfig(
                            temperature=temperature,
                            max_output_tokens=1000,
                        )
                    )
                    st.markdown("### ⚡ Tactical Development Plan")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please describe your challenge!")

# ============ TAB 4: NUTRITION ============
with tab4:
    st.header("🥗 Personalized Nutrition Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sport_nut = st.selectbox(
            "Your Sport",
            ["Football", "Cricket", "Basketball", "Tennis", "Athletics", "Volleyball", "Hockey", "Other"],
            key="nut_sport"
        )
        position_nut = st.text_input("Your Position", placeholder="e.g., Striker, Fast bowler")
        age_nut = st.number_input("Your Age", 10, 25, 16, key="nut_age")
    
    with col2:
        diet = st.selectbox(
            "Diet Type",
            ["Vegetarian", "Non-vegetarian", "Vegan", "Pescatarian", "No preference"]
        )
        allergies = st.text_input("Allergies/Intolerances (optional)")
    
    nut_goal = st.selectbox(
        "Nutrition Goal",
        ["Build muscle", "Increase endurance", "Weight management", "Speed & power", "Recovery", "General health"]
    )
    
    if st.button("🍎 Generate Nutrition Plan"):
        with st.spinner("Generating nutrition plan..."):
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
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.6,
                        max_output_tokens=1000,
                    )
                )
                st.markdown("### 🥗 Nutrition Plan")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")

# ============ TAB 5: PROFILE ============
with tab5:
    st.header("📊 Athlete Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Info")
        name = st.text_input("Name", placeholder="Your name")
        age_prof = st.number_input("Age", 10, 25, 16, key="prof_age")
        sport_prof = st.text_input("Sport")
        position_prof = st.text_input("Position")
    
    with col2:
        st.subheader("Physical Metrics")
        height = st.number_input("Height (cm)", 130, 210, 170)
        weight = st.number_input("Weight (kg)", 40, 150, 65)
        fitness = st.select_slider(
            "Fitness Level",
            ["Beginner", "Intermediate", "Advanced", "Elite"],
            value="Intermediate"
        )
    
    st.divider()
    
    col3, col4 = st.columns(2)
    
    with col3:
        goals = st.text_area("3-month Goals", placeholder="e.g., Improve fitness, make the team", height=100)
    
    with col4:
        injuries = st.text_area("Past Injuries (last 2 years)", placeholder="e.g., Ankle sprain, knee soreness", height=100)
    
    if st.button("💾 Save Profile"):
        profile_data = {
            "Name": name,
            "Age": age_prof,
            "Sport": sport_prof,
            "Position": position_prof,
            "Height": height,
            "Weight": weight,
            "Fitness Level": fitness,
            "Goals": goals,
            "Injuries": injuries
        }
        st.success("✅ Profile saved!")
        st.json(profile_data)

# Footer
st.divider()
st.markdown("""
    **CoachBot AI** - Empowering Young Athletes with AI Coaching
    
    ⚠️ **Disclaimer:** This app provides general guidance. Always consult professional coaches and healthcare providers.
    
    📧 Need help? Check out the setup guide!
""")

