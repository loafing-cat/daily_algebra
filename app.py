from flask import Flask, render_template
import sqlite3
import os
import json
import datetime

app = Flask(__name__)

# run in production mode
os.environ['FLASK_ENV'] = 'production'

# initialize global variables to track time
current_qa = None
current_qa_set_time = None

def get_new_qa():
    conn = sqlite3.connect('app_data/questions.db')
    c = conn.cursor()
    c.execute('select question, answer from questions order by random() limit 1')
    question, answer = c.fetchone()
    conn.close()
    return question, answer

def should_refresh_qa():
    global current_qa_set_time
    if current_qa_set_time is None:
        return True
    now = datetime.datetime.now()
    time_passed = now - current_qa_set_time
    return time_passed > datetime.timedelta(minutes = 5)

@app.route('/')
def index():
    global current_qa, current_qa_set_time
    if should_refresh_qa():
        current_qa = get_new_qa()
        current_qa_set_time = datetime.datetime.now()
    
    question, answer = current_qa
    return render_template('index.html', question = question, answer = answer)

if __name__ == '__main__':
    app.run(debug = False)