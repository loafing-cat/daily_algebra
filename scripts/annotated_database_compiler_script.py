import os
import csv
import sqlite3

# establish root project folder
cwd = os.path.abspath(os.getcwd())

# define path to the csv file that contains my question-answer pairs
csv_path = os.path.join(cwd, 'construction_data', 'question_answer.csv')

# define path to where my SQLite database file is to be created
db_path = os.path.join(cwd, 'app_data', 'questions.db')

# connect to database file, and creates the table called `questions` if it doesn't exist
conn = sqlite3.connect(db_path) # this creates a new database if it doesn't already exists : DB name will be what you provided in db_path ... '<name>/db'
c = conn.cursor() # allows user to execute SQL statements on the database
c.execute('create table if not exists questions (id integer primary key, question text unique, answer text)') # cheap way of preventing duplicates
conn.commit() # saves changes to database (cursor, execute, commit, and close are methods)
conn.close() # close database connection 

# open csv file and create al ist of dictionaries: each key-value pair will be one row
with open(csv_path, newline = '') as csvfile:
    '''
    construct object of the `DictReader` class by calling the `csv.DictReader()` constructor : used to read and convert CSV into dictionaries
    '''
    reader = csv.DictReader(csvfile) # create an instance of `csv.DictReader` class : reads csv line-by-line converting each to dictionary (an iterator over the csv)
    rows = list(reader) # convert `reader` object into a list of dictionaries : each dictionary is a separate question-answer pair and assign it to variable `rows`
    
# adds the data into the database by iterating over the rows object (list of dictionaries)
conn = sqlite3.connect(db_path)
c = conn.cursor()
for i in rows:
    c.execute('insert or ignore into questions (question, answer) values (?, ?)', (i['questions'], i['answers']))
conn.commit()
conn.close()