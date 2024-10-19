import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS responses (
            id integer PRIMARY KEY,
            query text NOT NULL,
            response text NOT NULL
        ); """
        conn.execute(sql_create_table)
    except sqlite3.Error as e:
        print(e)

def insert_response(conn, query, response):
    sql = ''' INSERT INTO responses(query, response)
              VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (query, response))
    conn.commit()
    return cur.lastrowid

def fetch_response(conn, user_query):
    cur = conn.cursor()
    cur.execute("SELECT response FROM responses WHERE query LIKE ?", (f'%{user_query}%',))
    rows = cur.fetchall()
    if rows:
        return rows[0][0]
    else:
        return None
