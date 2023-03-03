import os
import csv
import sqlite3

# define root project folder
cwd = os.path.abspath(os.getcwd())

# define path to csv file
csv_path = os.path.join(cwd, 'construction_data', 'question_answer.csv')

# define path to SQLite database
db_path = os.path.join(cwd, 'app_data', 'questions.db')

# establish connection to SQLite database and create table if exists with column requirements
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('create table if not exists questions (id integer primary key, question text unique, answer text)')
conn.commit()
conn.close()

# open and read csv file : create a list of dictionaries (each dictionary is a question-answer pair)
with open(csv_path, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader) 

# writes to table i.e., adding in the data from csv files by iterating over the list of dictionaries
conn = sqlite3.connect(db_path)
c = conn.cursor()
for i in rows:
    c.execute('insert or ignore into questions (question, answer) values (?, ?)', (i['questions'], i['answers']))
conn.commit()
conn.close()