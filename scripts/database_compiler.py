import os
import csv
import sqlite3
import pandas as pd

# establish absolute path to root project : in order to run the script as a main file, the absolute path must be defined...if ran in interactive window, it gets imported as a module and can run 
cwd = os.path.abspath(os.getcwd())

# define path to my CSV file
csv_path = os.path.join(cwd, 'construction_data', 'question_answer.csv')

# open and read the CSV file
with open(csv_path, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    
df = pd.read_csv(csv_path)

print(df)