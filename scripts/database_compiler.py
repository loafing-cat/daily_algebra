import os
import csv
import sqlite3
import pandas as pd

# define path to my CSV file
# csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'construction_data', 'question_answer.csv'))

# Get the path to the directory containing the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the CSV file relative to the script directory
csv_path = os.path.join(script_dir, '..', 'construction_data', 'questions_answers.csv')

# open and read the CSV file
with open(csv_path, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    
df = pd.read_csv(csv_path)

print(df)