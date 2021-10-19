import mysql.connector


def create_database():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1')

    # Creating a cursor obeject using cursor() method
    cursor = conn.cursor()

    # Doping database YouTube if already exists.
    cursor.execute("DROP database IF EXISTS YouTube")

    # Creating a database and executing it.
    cursor.execute("CREATE database YouTube")

    conn.close()


def addDatabase():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1', database="YouTube")

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE details (video_id VARCHAR(11) PRIMARY KEY)")

    query = """ALTER TABLE details
            ADD COLUMN video_title text NOT NULL,
            ADD COLUMN video_author text NOT NULL
            """
    cursor.execute(query)
    print("hiiiiiiiiiiiiiiiii")
    cursor.execute("DESCRIBE details")
    # Fetch and print the meta-data of the table
    indexList = cursor.fetchall()
    print(indexList)
    print(type(indexList))

    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO details(video_id, video_title, video_author)
    VALUES ('fhEqtynX_xc', 'Drake - TSU (Audio)', 'Drake'), ('XNpGNykVZ6U', 'Nonstop', 'Drake - Topic')"""

    try:
        # Executing the SQL command
        cursor.execute(sql)
        print("Data inserted")

        # Commit your changes in the database
        conn.commit()

    except:
        # Rolling back in case of error
        conn.rollback()
        print("Data insert fail")

    conn.close()


def fetch_all_databases():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1', database="YouTube")

    cursor = conn.cursor()

    # Retrieving the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())
    conn.close()


def fetch_all_tables():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1', database="YouTube")

    cursor = conn.cursor()

    cursor.execute("Show tables;")

    table_names = cursor.fetchall()
    print("Showing all tables")
    for table in table_names:
        print(table)
    conn.close()


def fetch_all_rows():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1', database="YouTube")

    cursor = conn.cursor()

    # execute your query
    cursor.execute("SELECT * FROM details")

    # fetch all the matching rows
    result = cursor.fetchall()
    print("Showing all entries in the table (rows)")
    for row in result:
        print(row)
    conn.close()
