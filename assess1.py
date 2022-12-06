import psycopg2
def connectdb():
    conn = psycopg2.connect(
        host="localhost",
        database="assessmentdb.sql",
        user="postgres",
        password="sudden21")
    return conn
