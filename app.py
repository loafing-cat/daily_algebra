from flask import Flask, render_template, session, url_for
import sqlite3
from datetime import datetime, timedelta

# create a new instance of the Flask class
app = Flask(__name__)

# used to verify 24 hour waiting period
app.secret_key = 'mysecretkey'

# define function to pull question and answers from database
@app.route('/')
def index():
    # check if user has already seen today's question
    if 'last_question_seen' in session and session['last_question_seen'] == datetime.today().strftime('%Y-%m-%d'):
        question = None
    else:
        # retrieve question from database
        conn = sqlite3.connect('app_data/questions.db')
        c = conn.cursor()
        c.execute('SELECT question FROM questions WHERE id = 1')
        question = c.fetchone()[0]
        conn.close()

        # store today's date in session
        session['last_question_seen'] = datetime.today().strftime('%Y-%m-%d')

    # retrieve answer from database for the previous day
    conn = sqlite3.connect('app_data/questions.db')
    c = conn.cursor()
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    c.execute(f"SELECT answer FROM questions WHERE id = (SELECT MAX(id) FROM questions) - 1")
    last_answer = c.fetchone()[0] if c.fetchone() else None
    conn.close()

    # store last answer seen date in session
    session['last_answer_seen'] = yesterday

    return render_template('index.html', question=question, last_answer=last_answer, last_answer_seen=session.get('last_answer_seen'))


if __name__ == '__main__':
    app.run(debug=True)
