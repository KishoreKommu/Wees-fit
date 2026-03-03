from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.text import slugify

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in after registration
            return redirect("home")  # change "home" to your homepage route name
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def daily_routines_view(request):
    return render(request, "daily_routines.html")

def bmi_form(request):
    return render(request, 'fitness/bmi_form.html')

def bmi_result(request):
    if request.method == "POST":
        height = float(request.POST['height']) / 100  # cm → m
        weight = float(request.POST['weight'])
        bmi = round(weight / (height * height), 1)

        if bmi < 18.5:
            plan = "You are underweight. Focus on a healthy diet and strength training."
        elif 18.5 <= bmi < 24.9:
            plan = "Great! You are in the normal range. Maintain a balanced lifestyle."
        elif 25 <= bmi < 29.9:
            plan = "You are overweight. Regular exercise and healthy eating are recommended."
        else:
            plan = "You are obese. Consider a strict fitness and diet plan."

        return render(request, "fitness/bmi_result.html", {"bmi": bmi, "plan": plan})
    

def bmi_plan(request):
    # Get BMI from query parameter
    bmi = request.GET.get('bmi')
    if bmi:
        bmi = float(bmi)
        # Create customized plan
        if bmi < 18.5:
            plan_text = "Underweight Plan: Focus on calorie-rich meals and strength training 3–4 times a week."
        elif 18.5 <= bmi < 24.9:
            plan_text = "Normal Plan: Maintain balanced diet and moderate exercise to stay fit."
        elif 25 <= bmi < 29.9:
            plan_text = "Overweight Plan: Focus on cardio, low-calorie diet, and exercise 5 times a week."
        else:
            plan_text = "Obese Plan: Strict fitness regime, diet monitoring, and professional guidance recommended."
    else:
        plan_text = "BMI not found."

    return render(request, "fitness/bmi_plan.html", {"bmi": bmi, "plan_text": plan_text})


def weight_monitor(request):
    return render(request, "weight_monitor.html")

def personal_plans(request):
    return render(request, "personal_plans.html")

def track_features(request):
    return render(request, "track_features.html")


from django.shortcuts import render

def track_progress(request):
    
    daily_routines = [
        "Morning: 10 min stretching + 20 min walk",
        "Afternoon: Light workout or yoga",
        "Evening: 30 min cardio or strength training",
        "Sleep: Aim for 7-8 hours of sleep"
    ]

    health_tips = [
        "Drink at least 2 liters of water daily",
        "Maintain a balanced diet rich in proteins and vegetables",
        "Take short breaks during work to stretch",
        "Track your calories and maintain a consistent schedule"
    ]

    context = {
        'daily_routines': daily_routines,
        'health_tips': health_tips
    }

    return render(request, 'fitness/track_progress.html', context)



def home(request):
    return render(request, "fitness/home.html")


@login_required
def start_journey(request):
    return render(request, "fitness/start_journey.html")


@login_required
def dashboard(request):
    return render(request, "fitness/dashboard.html")



@login_required
def bmi_calculator(request):
    if request.method == "POST":
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height")) / 100  # cm to meters
        bmi = round(weight / (height ** 2), 2)

        context = {
            "weight": weight,
            "height": height * 100,
            "bmi": bmi,
            "status": (
                "Underweight" if bmi < 18.5 else
                "Normal" if bmi < 24.9 else
                "Overweight" if bmi < 29.9 else
                "Obese"
            )
        }
        return render(request, "fitness/bmi_result.html", context)

    return render(request, "fitness/bmi_calculator.html")


@login_required
def weight_log(request):
 
    return render(request, "fitness/weight_log.html")


@login_required
def daily_routine(request):
   
    return render(request, "fitness/daily_routine.html")


@login_required
def community(request):
    return render(request, "fitness/community.html")


@login_required
def profile(request):
    return render(request, "fitness/profile.html")


GOALS = [
    "Weight Loss / Fat Reduction",
    "Muscle Building / Strength Gain",
    "Improve Cardiovascular Endurance",
    "Increase Flexibility & Mobility",
    "Improve Core Strength & Stability",
    "Boost Overall Energy Levels",
    "Improve Athletic Performance",
    "Better Mental Health & Stress Relief",
    "Consistency & Habit Formation",
    "Longevity & Healthy Lifestyle",
]


def personal_plans(request):
    goal_list = [(goal, slugify(goal)) for goal in GOALS]
    return render(request, 'fitness/personal_plans.html', {'goal_list': goal_list})
    


PLANS = {
    'weight-loss-fat-reduction': {
        'title': 'Weight Loss / Fat Reduction',
        'intro': 'Reduce body fat and achieve a leaner, healthier body.',
        'nutrition': 'Focus on a calorie deficit with high-protein meals, plenty of vegetables, moderate healthy fats, and minimal processed sugar.',
        'workout_intro': 'Combine cardio and strength training for maximum fat burn.',
        'workout': [
            'Monday: HIIT cardio + Core',
            'Tuesday: Upper Body Strength',
            'Wednesday: Cardio (Running or Cycling)',
            'Thursday: Lower Body Strength',
            'Friday: Full-body Circuit',
            'Saturday: Yoga or Stretching',
            'Sunday: Rest'
        ],
        'weekly_schedule': {
            'Monday': 'HIIT + Core (30-45 min)',
            'Tuesday': 'Upper Body Strength (45 min)',
            'Wednesday': 'Cardio (30-40 min)',
            'Thursday': 'Lower Body Strength (45 min)',
            'Friday': 'Full-body Circuit (50 min)',
            'Saturday': 'Yoga or Stretching (30 min)',
            'Sunday': 'Rest'
        },
        'tips': [
            'Track your calories daily.',
            'Stay hydrated.',
            'Sleep at least 7 hours.',
            'Consistency is key.',
            'Mix up workouts to avoid plateau.'
        ]
    },

    'muscle-building-strength-gain': {
        'title': 'Muscle Building / Strength Gain',
        'intro': 'Increase lean muscle mass and overall strength.',
        'nutrition': 'Eat a calorie surplus with high protein, complex carbs, and healthy fats. Include post-workout protein shakes.',
        'workout_intro': 'Focus on progressive overload and compound exercises for optimal growth.',
        'workout': [
            'Monday: Chest & Triceps',
            'Tuesday: Back & Biceps',
            'Wednesday: Rest or Active Recovery',
            'Thursday: Legs & Glutes',
            'Friday: Shoulders & Abs',
            'Saturday: Full-body Strength',
            'Sunday: Rest'
        ],
        'weekly_schedule': {
            'Monday': 'Bench press, Push-ups, Tricep dips (45 min)',
            'Tuesday': 'Pull-ups, Rows, Bicep curls (45 min)',
            'Wednesday': 'Active recovery or light cardio',
            'Thursday': 'Squats, Lunges, Leg press (50 min)',
            'Friday': 'Shoulder press, Lateral raises, Plank (45 min)',
            'Saturday': 'Compound circuits (50 min)',
            'Sunday': 'Rest'
        },
        'tips': [
            'Increase weights gradually.',
            'Prioritize protein intake.',
            'Track your progress weekly.',
            'Ensure proper form to avoid injuries.',
            'Rest muscles to grow effectively.'
        ]
    },

    'improve-cardiovascular-endurance': {
        'title': 'Improve Cardiovascular Endurance',
        'intro': 'Boost stamina and heart health with cardio-focused workouts.',
        'nutrition': 'Balanced diet with complex carbs for energy, moderate protein, and healthy fats.',
        'workout_intro': 'Mix steady-state cardio and high-intensity sessions to increase endurance.',
        'workout': [
            'Monday: Long-distance running',
            'Tuesday: Cycling or elliptical',
            'Wednesday: HIIT intervals',
            'Thursday: Swimming or rowing',
            'Friday: Tempo run',
            'Saturday: Outdoor sports',
            'Sunday: Rest or light walk'
        ],
        'weekly_schedule': {
            'Monday': '5km run at moderate pace',
            'Tuesday': '30 min cycling',
            'Wednesday': 'HIIT: 30 sec sprint / 90 sec walk x 10',
            'Thursday': 'Swimming 30-40 min',
            'Friday': 'Tempo run 4km',
            'Saturday': 'Play basketball or football 45 min',
            'Sunday': 'Light walk or stretching'
        },
        'tips': [
            'Monitor heart rate zones.',
            'Stay hydrated and fuel with carbs before workouts.',
            'Progress gradually to avoid fatigue.',
            'Include rest days to recover.',
            'Track distance and time to measure improvements.'
        ]
    },

    'increase-flexibility-mobility': {
        'title': 'Increase Flexibility & Mobility',
        'intro': 'Improve joint health, reduce stiffness, and enhance overall movement quality.',
        'nutrition': 'Balanced diet with anti-inflammatory foods like turmeric, berries, leafy greens, and omega-3s.',
        'workout_intro': 'Focus on dynamic stretches, yoga flows, and mobility drills daily.',
        'workout': [
            'Daily: Morning dynamic stretches',
            '3x/week: Yoga session (30-60 min)',
            '3x/week: Mobility drills (hips, shoulders, ankles)',
            'Evening: Light foam rolling or stretching'
        ],
        'weekly_schedule': {
            'Monday': 'Yoga flow 45 min',
            'Tuesday': 'Mobility drills 20 min',
            'Wednesday': 'Yoga flow 45 min',
            'Thursday': 'Mobility drills 20 min',
            'Friday': 'Yoga flow 45 min',
            'Saturday': 'Light stretching 20 min',
            'Sunday': 'Rest or gentle walk'
        },
        'tips': [
            'Breathe deeply during stretches.',
            'Never force a stretch.',
            'Consistency is key.',
            'Combine mobility with strength exercises for balance.',
            'Use foam rollers to release tension.'
        ]
    },

    'improve-core-strength-stability': {
        'title': 'Improve Core Strength & Stability',
        'intro': 'Strengthen abs, obliques, and lower back for better posture and balance.',
        'nutrition': 'Protein-rich diet with healthy fats to support muscle growth and recovery.',
        'workout_intro': 'Engage in targeted core exercises and integrate functional movements.',
        'workout': [
            'Plank variations',
            'Russian twists',
            'Dead bugs',
            'Leg raises',
            'Stability ball exercises',
            'Medicine ball slams'
        ],
        'weekly_schedule': {
            'Monday': 'Planks, Side planks (15 min)',
            'Tuesday': 'Russian twists + Leg raises (20 min)',
            'Wednesday': 'Stability ball exercises (20 min)',
            'Thursday': 'Dead bugs + Bird-dogs (20 min)',
            'Friday': 'Medicine ball slams + Core circuits (25 min)',
            'Saturday': 'Yoga for core (30 min)',
            'Sunday': 'Rest'
        },
        'tips': [
            'Focus on proper form.',
            'Engage your core on all exercises.',
            'Increase difficulty gradually.',
            'Combine with cardio and strength training.',
            'Stretch lower back after workouts.'
        ]
    },

    'boost-overall-energy-levels': {
        'title': 'Boost Overall Energy Levels',
        'intro': 'Feel more active and alert throughout the day with regular fitness.',
        'nutrition': 'Balanced diet with complex carbs, lean protein, and micronutrient-rich foods.',
        'workout_intro': 'Short, energizing workouts and morning routines can boost vitality.',
        'workout': [
            'Morning bodyweight circuit',
            'Short brisk walks post-meals',
            'Light strength training 3x/week',
            'Yoga or stretching daily',
            'Cardio intervals 2x/week'
        ],
        'weekly_schedule': {
            'Monday': 'Morning circuit 15-20 min',
            'Tuesday': 'Brisk walk 20 min',
            'Wednesday': 'Strength training 30 min',
            'Thursday': 'Yoga 30 min',
            'Friday': 'Cardio intervals 20 min',
            'Saturday': 'Outdoor activity (hiking, cycling) 40 min',
            'Sunday': 'Rest'
        },
        'tips': [
            'Take short movement breaks during work.',
            'Stay hydrated.',
            'Get sunlight exposure.',
            'Eat energy-sustaining foods.',
            'Maintain consistent sleep patterns.'
        ]
    },

    'improve-athletic-performance': {
        'title': 'Improve Athletic Performance',
        'intro': 'Enhance speed, agility, and power for better sports performance.',
        'nutrition': 'Protein for muscle repair, carbs for energy, and electrolytes for endurance.',
        'workout_intro': 'Sport-specific drills, plyometrics, and functional strength exercises.',
        'workout': [
            'Agility ladder drills',
            'Plyometric jumps',
            'Sprint intervals',
            'Sport-specific skill training',
            'Core and stability exercises'
        ],
        'weekly_schedule': {
            'Monday': 'Agility + Plyometrics 30 min',
            'Tuesday': 'Sprint intervals 20 min',
            'Wednesday': 'Skill training 45 min',
            'Thursday': 'Strength training 45 min',
            'Friday': 'Core & stability 30 min',
            'Saturday': 'Mixed cardio + skills 40 min',
            'Sunday': 'Rest'
        },
        'tips': [
            'Warm-up thoroughly.',
            'Cool down after training.',
            'Track your progress metrics.',
            'Focus on technique over speed.',
            'Include rest for recovery.'
        ]
    },

   'better-mental-health-stress-relief': {
        'title': 'Better Mental Health & Stress Relief',
        'intro': 'Use fitness to manage stress, anxiety, and improve mood.',
        'nutrition': 'Include omega-3s, fruits, vegetables, and whole grains to support brain health.',
        'workout_intro': 'Low-impact exercise, mindfulness, yoga, and light cardio to reduce stress.',
        'workout': [
            'Yoga or Tai Chi 3x/week',
            'Brisk walking or light jogging 4x/week',
            'Meditation 10-15 min daily',
            'Stretching routines daily'
        ],
        'weekly_schedule': {
            'Monday': 'Yoga 30-40 min',
            'Tuesday': 'Brisk walk 30 min + Meditation 10 min',
            'Wednesday': 'Tai Chi 30 min + Stretching 10 min',
            'Thursday': 'Yoga 30-40 min',
            'Friday': 'Light jogging 30 min + Meditation 10 min',
            'Saturday': 'Outdoor activity / Gentle walk 40 min',
            'Sunday': 'Rest or gentle stretching'
        },
        'tips': [
            'Practice mindfulness daily.',
            'Breathe deeply during workouts.',
            'Avoid overtraining; focus on relaxation.',
            'Maintain a balanced diet.',
            'Get sufficient sleep for mental recovery.'
        ]
    },

    'consistency-habit-formation': {
        'title': 'Consistency & Habit Formation',
        'intro': 'Build healthy habits and stay consistent with your fitness and lifestyle goals.',
        'nutrition': 'Focus on balanced meals and portion control. Keep meal timing consistent to support habit formation.',
        'workout_intro': 'Start small, stay consistent, and gradually increase intensity.',
        'workout': [
            'Daily: Short morning stretch or walk',
            '3x/week: Light strength training',
            '3x/week: Cardio (running, cycling, or brisk walk)',
            'Daily: Mindfulness or meditation 5-10 min'
        ],
        'weekly_schedule': {
            'Monday': 'Morning walk 20 min + Stretch 10 min',
            'Tuesday': 'Strength training 30 min',
            'Wednesday': 'Cardio 30 min',
            'Thursday': 'Strength training 30 min',
            'Friday': 'Cardio 30 min',
            'Saturday': 'Outdoor activity or active hobby 40 min',
            'Sunday': 'Rest or light walk'
        },
        'tips': [
            'Start with small, manageable goals.',
            'Track your progress daily.',
            'Set reminders for workouts and meals.',
            'Reward yourself for consistency.',
            'Don’t be discouraged by occasional slip-ups.'
        ]
    },

    'longevity-healthy-lifestyle': {
        'title': 'Longevity & Healthy Lifestyle',
        'intro': 'Adopt habits that promote long-term health, vitality, and wellness.',
        'nutrition': 'Eat nutrient-rich foods, focus on whole grains, fruits, vegetables, lean protein, and healthy fats.',
        'workout_intro': 'Incorporate a mix of cardio, strength, flexibility, and balance exercises for overall wellness.',
        'workout': [
            'Daily: Light cardio (walking, cycling) 20-30 min',
            '3x/week: Strength or resistance training',
            '3x/week: Yoga or stretching',
            'Daily: Mindfulness or meditation 10-15 min'
        ],
        'weekly_schedule': {
            'Monday': 'Cardio 30 min + Stretch 10 min',
            'Tuesday': 'Strength training 30-40 min',
            'Wednesday': 'Yoga 30 min',
            'Thursday': 'Cardio 30 min + Stretch 10 min',
            'Friday': 'Strength training 30-40 min',
            'Saturday': 'Yoga or outdoor activity 30-40 min',
            'Sunday': 'Rest or gentle walk'
        },
        'tips': [
            'Prioritize sleep and recovery.',
            'Stay hydrated throughout the day.',
            'Include stress management techniques.',
            'Keep active throughout the day (walk, take stairs).',
            'Avoid smoking and excessive alcohol.'
        ]
    }
}

# View function
def plan_detail(request, goal_slug):
    plan = PLANS.get(goal_slug)
    if not plan:
        return render(request, '404.html')  
    return render(request, 'fitness/plan_detail.html', {
        'goal_title': plan['title'],
        'goal_intro': plan['intro'],
        'nutrition_plan': plan['nutrition'],
        'workout_intro': plan['workout_intro'],
        'workout_plan': plan['workout'],
        'weekly_schedule': plan['weekly_schedule'],
        'tips': plan['tips'],
    })

