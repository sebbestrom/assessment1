import psycopg2
def connectdb():
    conn = psycopg2.connect(
        host="localhost",
        database="assessmentdb.sql",
        user="postgres",
        password="sudden21")
    return conn

def list(conn):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute("SELECT*FROM contacts")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    return rows

keep_going = True
while keep_going:
    commands = input("Following commands are available: list, insert, delete: ").strip().lower()
    if commands == "list":
        conn = connectdb()
        print("\nThis is the list:")
        listrows = list(conn)
        for listrow in listrows:
            print(listrow[0], "\t", listrow[1])
        print("\n")
