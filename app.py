from flask import Flask, render_template
import sqlite3
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# run in production
os.environ['FLASK_ENV'] = 'production'

# Define the route for the index page
@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('app_data/questions.db')
    c = conn.cursor()

    # Get the current date
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Get the ID of the next question to display
    c.execute("SELECT id FROM questions ORDER BY id DESC LIMIT 1")
    last_question_id = c.fetchone()[0]
    question_id = (last_question_id % 2) + 1

    # Get the question and answer from the database
    c.execute(f"SELECT question, answer FROM questions WHERE id = {question_id}")
    question, answer = c.fetchone()

    # Close the database connection
    conn.close()

    # Render the index.html template with the question and answer
    return render_template('index.html', question=question, answer=answer)

# turn off debug mode
if __name__ == '__main__':
    app.run(debug=False)