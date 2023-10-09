import os
import psycopg2
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the connection string from the environment variable
connection_string = os.getenv('DATABASE_URL')

# Connect to the Postgres database
conn = psycopg2.connect(connection_string)
conn.autocommit = True

# Create a cursor object
cur = conn.cursor()
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#    INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')

# Execute SQL commands to retrieve the current time and version from PostgreSQL
cur.execute("INSERT INTO playing_with_neon(\"id\", \"name\", \"value\") VALUES(12, 'd3d995642', 0.74695);")
# # time = cur.fetchone()[0]
# first_query = cur.fetchall()
# # cur.execute('SELECT version();')
# # version = cur.fetchone()[0]

# # Close the cursor and connection
conn.commit()
conn.close()
# print("my first query is: ", first_query)
# # Print the results
# # print('Current time:', time)
# # print('PostgreSQL version:', version)

