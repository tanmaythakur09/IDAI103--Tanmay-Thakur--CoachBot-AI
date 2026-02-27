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
<img width="1913" height="992" alt="1_login_dashboard" src="https://github.com/user-attachments/assets/a085c35e-0b07-4f72-a591-df6da5106537" />


### 2. Home Page
<img width="1919" height="970" alt="2_home_page" src="https://github.com/user-attachments/assets/c1a9a2a3-57ca-496e-9ae6-f87554da143d" />


### 3. Plan Generator
<img width="1919" height="1002" alt="3_plan_generator" src="https://github.com/user-attachments/assets/2c7bcd3b-a86e-494d-9680-e7997f979d85" />


### 4. Performance Analytics
<img width="1916" height="994" alt="4_performance_analytics" src="https://github.com/user-attachments/assets/61e23cae-88f5-4fe2-ac76-99d960b6b0e9" />


### 5. Achievements & Badges
<img width="1918" height="936" alt="5_achievements_and_badges" src="https://github.com/user-attachments/assets/41a9e98c-fbb2-4221-b901-307dfe19e69a" />


### 6. Community & Challenges
<img width="1913" height="994" alt="6_community_and_challenges" src="https://github.com/user-attachments/assets/ff5c25d6-1c7f-42a7-887b-804ac7c634f2" />


### 7. Advanced AI Coach
<img width="1919" height="987" alt="7_advanced_AI_coach" src="https://github.com/user-attachments/assets/900ea734-ea5f-4d60-971b-a6a5892698cb" />


### 8. Support Center
<img width="1919" height="967" alt="8_support_center" src="https://github.com/user-attachments/assets/30bbc527-74df-4acd-9738-c6bae887159c" />


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
