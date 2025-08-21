def get_workout_plan(goal):
    plans = {
        'Fat Loss': 'Do cardio 5x/week, strength 3x/week, 30 min walk daily.',
        'Muscle Gain': 'Strength train 5x/week, focus on compound lifts.',
        'Weight Gain': 'Strength 3x/week, moderate cardio, calorie surplus.',
        'Stay Fit': 'Yoga, walking, 3-day full-body routine.',
    }
    return plans.get(goal, 'Stay active with regular movement.')

def get_diet_plan(goal):
    diets = {
        'Fat Loss': 'Low-carb, high protein. Drink lots of water.',
        'Muscle Gain': 'High protein, moderate carbs and fats.',
        'Weight Gain': 'Calorie surplus, high carbs, healthy fats.',
        'Stay Fit': 'Balanced diet, fruits, veggies, lean protein.',
    }
    return diets.get(goal, 'Eat balanced meals daily.')

def get_schedule(profession):
    if 'student' in profession.lower():
        return 'Morning walk + evening workout after classes.'
    elif 'developer' in profession.lower():
        return 'Break walks every 2 hrs + post-work strength session.'
    elif 'teacher' in profession.lower():
        return 'Midday walks + yoga in evening.'
    elif 'freelancer' in profession.lower():
        return 'Flexible schedule: workout in early morning.'
    else:
        return 'Find 1 hour/day for activity. Prioritize movement.'
