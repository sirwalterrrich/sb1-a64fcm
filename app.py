from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from training_plans import generate_plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_plan', methods=['POST'])
def create_plan():
    goal = request.form.get('goal')
    weeks = int(request.form.get('weeks', 4))
    level = request.form.get('level', 'beginner')
    
    training_plan = generate_plan(goal, weeks, level)
    return render_template('plan.html', plan=training_plan)

if __name__ == '__main__':
    app.run(debug=True)