import os
import csv
import sqlite3

cwd = os.path.abspath(os.getcwd())

csv_path = os.path.join(cwd, 'construction_data', 'question_answer.csv')

db_path = os.path.join(cwd, 'app_data', 'questions.db')

conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('create table if not exists questions (id integer primary key, question text, answer text)')
conn.commit()
conn.close()

with open(csv_path, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader) 
    
# add data to databse
conn = sqlite3.connect(db_path)
c = conn.cursor()
for i in rows:
    c.execute('insert into questions (question, answer) values (?, ?)', (i['questions'], i['answers']))
conn.commit()
conn.close()