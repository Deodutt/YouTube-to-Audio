from bs4 import BeautifulSoup
import requests
import os
from os import listdir
import mysql.connector


def webscrapper(user_url):
    video_details = {}
    req = requests.get(user_url)
    soup = BeautifulSoup(req.content, 'html.parser')

    video_details['video_title'] = soup.find(
        "meta", itemprop="name").attrs.get('content')

    video_details['video_author'] = soup.find(
        "link", itemprop="name").attrs.get('content')

    video_details['video_views'] = "{:,}".format(int(soup.find(
        "meta", itemprop="interactionCount").attrs.get('content')))

    video_details['video_published'] = soup.find(
        "meta", itemprop="datePublished").attrs.get('content')

    video_details['video_duration'] = soup.find(
        "meta", itemprop="duration").attrs.get('content')

    video_details['video_id'] = soup.find(
        "meta", itemprop="videoId").attrs.get('content')

    video_details['video_thumbnail'] = soup.find(
        "link", itemprop="thumbnailUrl").attrs.get('href')

    video_details[
        'video_url'] = f"https://www.youtube.com/watch?v={video_details.get('video_id')}"

    # print(video_details)

    return video_details


def delete():
    folder_path = './'
    for file_name in listdir(folder_path):
        if file_name.endswith('.mp3'):
            os.remove(folder_path + file_name)


def createDatabase():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1')

    # Creating a cursor obeject using cursor() method
    cursor = conn.cursor()

    # Doping database YouTube if already exists.
    cursor.execute("DROP database IF EXISTS YouTube")

    # Creating a database and executing it.
    cursor.execute("CREATE database YouTube")

    # Retrieving the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())

    conn.close()


def database():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1', database="YouTube")

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")
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

    cursor.execute("DESCRIBE details")
    # Fetch and print the meta-data of the table
    indexList = cursor.fetchall()
    print(indexList)

    # Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO details(video_id, video_title, video_author)
    VALUES ('fhEqtynX_xc', 'Drake - TSU (Audio)', 'Drake')"""

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


def fetchDatabase():
    conn = mysql.connector.connect(
        user='root', password='kuralabs123', host='127.0.0.1', database="YouTube")

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    print("Showing tables")
    cursor.execute("Show tables;")
    table_names = cursor.fetchall()
    for x in table_names:
        print(x)

    # execute your query
    cursor.execute("SELECT * FROM details")

    # fetch all the matching rows
    result = cursor.fetchall()

    # loop through the rows
    for row in result:
        print(row, '\n')
        print("Showing row")
    conn.close()
