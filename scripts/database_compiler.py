import os
import csv
import sqlite3

# define path to my CSV file
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'construction_data', 'question_answer.csv'))

# open and read the CSV file
with open(csv_path, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)