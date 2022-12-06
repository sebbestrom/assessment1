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

def insert(conn,first_name):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO contacts (first_name) VALUES ('{first_name}')")
    conn.commit()
    cur.close()
    
def delete(conn,first_name):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM contacts WHERE first_name = '{first_name}'")
    conn.commit()
    cur.close()

keep_going = True
while keep_going:
    commands = input("Following commands are available: list, insert, delete: ").strip().lower()
    if commands == "list":
        conn = connectdb()
        print("\nList of names:")
        listrows = list(conn)
        for listrow in listrows:
            print(listrow[0], "\t", listrow[1])
        print("\n")

    elif commands == "insert":
        conn = connectdb()
        first_name = input("Your first name: ").strip().title()
        insert(conn,first_name)
        print(f"{first_name} has been added to the list.")
    elif commands == "delete":
        conn = connectdb()
        first_name = input("Your first name: ").strip().title()
        delete(conn,first_name)
        print(f"{first_name} has been deleted from the list.")
    elif commands == "quit":
        quit()
        keep_going = False
    else:
        print("Invalid option, maybe you typed wrong?")
