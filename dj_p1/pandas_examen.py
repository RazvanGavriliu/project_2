
import pandas as pd

import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    df = pd.read_sql_query("SELECT * from app_1_person", conn)

df['full name'] = df['first_name'] + ' ' + df['last_name']

print(df)
df.to_csv('persons.csv')
