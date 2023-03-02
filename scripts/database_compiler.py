import os
import csv
import sqlite3

# move to subfolder and open/read the data
with open('construction_data/question_answer.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(readr)