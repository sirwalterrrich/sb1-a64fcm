def generate_plan(goal, weeks, level):
    workouts = {
        'beginner': {
            'strength': ['Push-ups 3x10', 'Squats 3x12', 'Planks 3x30s'],
            'cardio': ['20min Walk/Jog', '15min Cycling', '10min Jump Rope'],
            'recovery': ['Light Stretching', 'Yoga Basics', 'Mobility Work']
        },
        'intermediate': {
            'strength': ['Push-ups 4x12', 'Weighted Squats 4x10', 'Pull-ups 3x8'],
            'cardio': ['30min Run', '25min HIIT', '40min Cycling'],
            'recovery': ['Dynamic Stretching', 'Yoga Flow', 'Foam Rolling']
        },
        'advanced': {
            'strength': ['Weighted Push-ups 4x15', 'Barbell Squats 5x5', 'Pull-ups 5x10'],
            'cardio': ['45min Run', '35min HIIT', '60min Cycling'],
            'recovery': ['Advanced Yoga', 'Mobility Work', 'Active Recovery']
        }
    }

    plan = []
    for week in range(weeks):
        week_plan = {
            'week': week + 1,
            'days': []
        }
        
        # Generate daily workouts
        for day in range(7):
            if day in [0, 2, 4]:  # Monday, Wednesday, Friday
                workout_type = 'strength'
            elif day in [1, 5]:  # Tuesday, Saturday
                workout_type = 'cardio'
            else:  # Thursday, Sunday
                workout_type = 'recovery'
                
            week_plan['days'].append({
                'day': day + 1,
                'type': workout_type,
                'exercises': workouts[level][workout_type]
            })
            
        plan.append(week_plan)
    
    return plan