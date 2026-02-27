# 🏆 CoachBot AI  
Smart Fitness Assistance Web App Powered by Generative AI  

---

## 📌 Project Overview

CoachBot AI is a Generative AI-powered sports performance web application developed under the CRS Artificial Intelligence (IDAI103) Summative Assessment.

This project aligns with **Scenario 2: Smart Fitness Assistance Web App Powered by Generative AI**.

The system bridges the gap in professional coaching access by providing:

- Personalized training plans
- Injury-aware recovery routines
- Tactical advice
- Nutrition guidance
- Mental conditioning support

The application integrates **Google Gemini 1.5 API** with a Streamlit-based web interface to generate structured, age-appropriate, and safe performance plans for youth athletes.

---

## 🎯 Problem Definition & Research

Many young athletes lack access to personalized coaching, especially in under-resourced regions. Generic training programs often ignore:

- Player position differences
- Injury history
- Age-specific training needs
- Nutrition customization

Research conducted included:

- Sport-specific conditioning models (football, cricket, athletics)
- Youth injury prevention frameworks
- AI-assisted personalized fitness systems
- Generative AI prompt design strategies

The objective was to design a structured AI assistant capable of acting as a virtual youth performance coach.

---

## 🧠 Model Integration & Configuration

### API Used
- Google Gemini 1.5 (via `google-generativeai`)

### Integration
- Python-based Streamlit web app
- Structured prompt engineering
- Dynamic user input capture

### Hyperparameter Tuning

| Parameter | Value Used | Purpose |
|------------|------------|----------|
| Temperature | 0.4–0.7 | Balance safety & creativity |
| Top_p | Default | Maintain coherent structure |

Lower temperature used for:
- Injury recovery plans
- Safety-focused outputs

Higher temperature used for:
- Tactical creativity
- Nutrition variations

---

## 🧩 Prompt Engineering (10 Core Features)

Below are the primary prompts implemented:

1. Generate a full weekly training plan for a [position] in [sport].
2. Create a safe recovery routine for an athlete with [injury].
3. Provide tactical advice to improve [specific skill].
4. Suggest a week-long nutrition plan for a 15-year-old [diet type].
5. Design a personalized warm-up and cooldown sequence.
6. Generate hydration and electrolyte strategy for training days.
7. Provide pre-match mental conditioning routine.
8. Suggest mobility exercises for injury prevention.
9. Generate stamina-building drills for tournament preparation.
10. Create low-impact conditioning program for post-injury athletes.

Prompts were refined through testing for:
- Clarity
- Safety
- Structured output formatting

---

## 🧪 Model Testing, Validation & Optimization

Testing was conducted across:

- Multiple sports (Football, Cricket, Athletics)
- Different positions (Goalkeeper, Striker, Bowler)
- Injury combinations
- Youth age variations

Validation Methods:
- Cross-checking with sports science sources
- Comparing recovery advice to known safe practices
- Refining prompts for clearer structure

Optimization Steps:
- Adjusted temperature for stability
- Added structured section headings
- Improved injury-awareness phrasing

---

## 💻 Web Application Features

- Login & Register Interface (Session-based)
- Interactive Dashboard
- Sidebar Navigation
- Expandable Output Sections
- Performance Metrics Display
- Help Assistant Chatbot
- Sports-Tech Themed UI
- Fully deployed via Streamlit Cloud

---

## 🌐 Deployment Details

GitHub Repository:  
https://github.com/tanmaythakur09/IDAI103--Tanmay-Thakur--CoachBot-AI  

Streamlit App:  
https://idai103--tanmay-thakur--coachbot-ai.streamlit.app/  

Deployment Steps:
1. Created app.py
2. Generated requirements.txt
3. Pushed to GitHub
4. Deployed via Streamlit Cloud
5. Tested across desktop & mobile

---

## 📚 References

- Gemini API Documentation – https://ai.google.dev
- AI in Fitness Applications – https://www.ijisrt.com/artificial-intelligence-powered-fitness-web-app
- Youth Injury Prevention Research – NCBI Sports Medicine Resources
- Generative AI Prompt Engineering Strategies – Google AI Documentation

---

## 📸 Application Screenshots

### 1. Login & Dashboard Page
![Login & Dashboard](screenshots/1_login_dashboard.png)

### 2. Home Page
![Workout Plans](screenshots/2_home_page.png)

### 3. Plan Generator
![Recovery Tab](screenshots/3_plan_generator.png)

### 4. Performance Analytics
![Help Chatbot](screenshots/4_performance_analytics.png)

### 5. Achievements & Badges
![Nutrition & Profile](5_achievements_and_badges.png)

### 6. Community & Challenges
![Recovery Tab](6_community_and_challenges.png)

### 7. Advanced AI Coach
![Help Chatbot](7_advanced_AI_coach.png)

### 8. Support Center
![Nutrition & Profile](8_support_center.png)

---

## 👨‍🎓 Student Information

Name: Tanmay Thakur  
Student ID: 1000389  
CRS: Artificial Intelligence  
Course: Generative A.I (IDAI103)  
School: Viraj International School  

---

## ✅ Conclusion

CoachBot AI demonstrates real-world application of Generative AI in sports performance planning. The project integrates structured prompt engineering, model configuration, testing, and deployment into a functional and user-friendly web platform.

This solution promotes inclusive access to AI-powered coaching tools for youth athletes and aligns with the objectives of the IDAI103 Summative Assessment.

---