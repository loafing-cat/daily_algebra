from flask import Flask, render_template, session, redirect, url_for
import sqlite3
from datetime import datetime

# create a new instance of the Flask class
app = Flask(__name__)

# used to verify 24 hour waiting period
app.secret_key = 'mysecretkey'

# define function to pull question and answers from database
@app.route('/')
def index():
    # verify if user has already seen today's question
    if 'last_question_seen' in session and session['last_question_seen'] == datetime.today().strftime('%Y-%m-%d'):
        # if user has already seen the question today, redirect them to the answer page
        return redirect(url_for('answer'))
    
    # Retrieve question from database
    conn = sqlite3.connect('app_data/questions.db')
    c = conn.cursor()
    c.execute('select question from questions where id = 1')
    question = c.fetchone()[0]
    conn.close()
    
    # Store today's date in session
    session['last_question_seen'] = datetime.today().strftime('%Y-%m-%d')
    
    # render the index.html template with the question variable
    return render_template('index.html', question=question)


@app.route('/answer')
def answer():
    # Retrieve answer from database
    conn = sqlite3.connect('app_data/questions.db')
    c = conn.cursor()
    c.execute('SELECT answer FROM questions WHERE id = 1')
    answer = c.fetchone()[0]
    conn.close()
    
    # render the answer.html template with the answer variable
    return render_template('answer.html', answer=answer)

if __name__ == '__main__':
    # run the Flask application in debug mode
    app.run(debug=True)
