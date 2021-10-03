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

def database():
    conn = mysql.connector.connect(user='root', password='', host='127.0.0.1')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Doping database MYDATABASE if already exists.
    cursor.execute("DROP database IF EXISTS MyDatabase")

    #Preparing query to create a database
    sql = "CREATE database YouTube";

    #Creating a database
    cursor.execute(sql)

    #Retrieving the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())

    #Closing the connection
    conn.close()