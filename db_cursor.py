
import psycopg2

try:
    conn = psycopg2.connect(host='localhost', database='GuiDB', user='postgres', password='bel054bel')
    cursor = conn.cursor()
    print("Database connection was successful!")

except Exception as error:
    print("Connection to database.py failed")
    print("error :", error)
