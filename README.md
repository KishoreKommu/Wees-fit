Wees Fit – Fitness Tracking and Personalized Fitness Platform
1. Project Overview

Wees Fit is a web-based fitness platform designed to help users track their fitness progress, monitor body metrics, and personalize workout and diet plans according to their fitness goals.
It acts as a digital fitness companion, enabling users to log their daily routines, weight progress, and BMI, while receiving AI-driven insights and motivational feedback.

The platform focuses on user engagement, data visualization, and goal personalization, helping users stay consistent with their fitness journey.

2. Objectives

To provide users with a personalized and interactive fitness dashboard.

To allow users to log weight and daily routines easily.

To calculate and visualize BMI (Body Mass Index) dynamically.

To analyze user habits and generate progress insights.

To motivate users through an AI-based fitness assistant.

To offer a simple yet aesthetic UI that feels like a smart fitness journal.

3. Technologies Used
Component	Technology
Frontend	HTML5, CSS3, Bootstrap 5, JavaScript
Backend	Django (Python Web Framework)
Database	SQLite (for local development)
Design & Styling	TailwindCSS / Custom CSS
Charts / Visualization	Chart.js
Authentication	Django User Model (Login, Signup)
Deployment Ready	Heroku / PythonAnywhere compatible

5. Functional Modules
User Authentication

Users can sign up, log in, and log out securely.

Authentication handled via Django’s built-in User model.

Each user gets a personalized dashboard linked to their fitness data.

Fitness Profile Setup

Each user creates a FitnessProfile with details:

Age Range

Weight Range

Height Range

Fitness Goal (e.g., Weight Loss, Muscle Gain, Maintain Fitness)

Profession (for activity level estimation)

BMI Calculation

The platform automatically computes BMI from the user’s height and weight.

Users get health insights (e.g., “Underweight”, “Healthy”, “Overweight”).

Visual feedback using progress bars or charts.

Daily Routine Tracking

Users log daily activities:

Steps walked

Workout duration

Water intake

Sleep hours

Each entry is stored in the DailyRoutine model.

The dashboard displays progress for each metric per day/week.

Weight Logging

Users can add new weight entries periodically.

A WeightLog model stores the user’s progress history.

A graph visualizes progress over time (using Chart.js).

AI Fitness Insights

Provides smart suggestions based on logged data.

Example: “You’ve maintained a steady weight for 2 weeks — great consistency!”

“Sleep duration is low. Try to get at least 7 hours for better recovery.”

Encourages users with positive reinforcement.

Progress Dashboard

The dashboard combines all metrics visually:

Current weight

BMI value

Weekly activity summary

Calorie tracking (optional future module)

Theme switcher (Light / Dark / Fitness Mode) for personalization.

5. Database Models
FitnessProfile
Field	Type	Description
user	OneToOneField(User)	Links to Django user
age_range	CharField	Age group of the user
weight_range	CharField	User’s current weight range
height_range	CharField	Height range
fitness_goal	CharField	e.g., Fat Loss, Muscle Gain
profession	CharField	e.g., Student, IT Professional
WeightLog
Field	Type	Description
user	ForeignKey(User)	Associated user
date	DateField	Date of log
weight	FloatField	Weight in kg
DailyRoutine
Field	Type	Description
user	ForeignKey(User)	Associated user
date	DateField	Log date
steps	IntegerField	Steps walked
workout_minutes	IntegerField	Duration of workout
water_intake	IntegerField	Water in ml
sleep_hours	FloatField	Sleep duration
6. File Structure
weesfit/
│
├── weesfit/                → Django project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── fitness/                → Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/fitness/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── weight_log.html
│   │   └── daily_routine.html
│   └── static/fitness/
│       ├── css/
│       ├── js/
│       └── images/
│
└── manage.py

7. Workflow

User Registration / Login

User signs up → Profile created automatically.

Redirected to dashboard.

Dashboard Overview

Displays BMI, progress charts, and motivational tips.

Data Input

Users can log weight, routines, and habits.

Visualization

Dynamic charts show user’s fitness trends.

Insights

AI module analyzes progress → displays messages like:

“🔥 You improved your consistency this week!”

“💧 Drink more water for better hydration.”

8. User Interface Design

Header/Navbar: Shows Wees Fit logo + user profile dropdown.

Sidebar (optional): Quick access to Weight Logs, Daily Routine, BMI Calculator.

Dashboard Cards: Summarized metrics in clean cards.

Theme Switcher: Toggle between modes (Light/Dark/Fitness Glow).

Graphs: Smooth animated line and bar charts.

Color Palette:

Primary: #00C49A (Fresh Green)

Secondary: #212529 (Dark Gray)

Accent: #FFB703 (Motivational Yellow)

Background: #F8F9FA (Light mode)

9. Charts and Visualization

Uses Chart.js for real-time graphs:

Weight Progress (Line Chart)

Daily Routine Summary (Bar Chart)

Sleep and Hydration Trends (Pie Chart)

Animations give a motivational “progress feel”.

10. AI & Smart Recommendations (Future Module)

In future updates, Wees Fit can integrate:

AI Goal Adjustments: Auto-adjust goals based on progress trends.

Chatbot Fitness Assistant: AI-powered virtual trainer for daily guidance.

Smart Meal Planner: Suggest meals based on calorie targets and preferences.

11. Features Summary

User Authentication
Fitness Profile Setup
BMI Calculation
Daily Routine Logging
Weight Tracking
Progress Visualization (Charts)
Motivational AI Insights
Responsive and Interactive UI

12. Future Enhancements

Integration with wearable fitness devices (e.g., Smart Bands).

Real-time activity monitoring through IoT integration.

Personalized nutrition recommendations.

Gamified achievements and community features (friends leaderboard).

Mobile App version using React Native or Flutter.

13. Testing & Validation
Feature	Test Case	Status
User Signup/Login	Credentials validation	✅
BMI Calculation	Correct formula & results	✅
Data Logging	Stored in DB & displayed	✅
Graph Visualization	Displays accurate data	✅
Theme Switching	Works on all pages	✅
Logout	Session ends properly	✅

14. Conclusion

Wees Fit is a step toward combining fitness awareness, motivation, and technology in a single user-friendly platform.
By integrating data visualization, smart recommendations, and personalization, it transforms raw fitness data into actionable insights.

The project demonstrates solid understanding of:

Full-stack web development (Django + JS)

Data analytics and user experience design

Health-tech innovation potential

Wees Fit is not just a website — it’s a personal fitness companion that grows with you.

15. Developer Details

Developer: Kishore Kommu
Role: Full Stack Developer
Project: Wees Fit – Fitness Tracking Web App
Technologies: Django, Python, HTML, CSS, JS, Chart.js
GitHub: github.com/KishoreKommu

LinkedIn: linkedin.com/in/kishore-kommu
