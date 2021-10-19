from __future__ import unicode_literals
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import helper
import logging
from pytube import YouTube
import youtube_db

application = app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def converter():
    # Needs to be global for the /download route
    global youtube_url, video_details
    user_url = ""
    youtube_url = ""
    video_details = {}
    helper.delete()

    youtube_db.create_database()
    print(f"Created successfully")

    # Adding data to the database
    youtube_db.addDatabase()

    # Fetch all the databases
    youtube_db.fetch_all_databases()

    # Fetching all the tables in the database
    youtube_db.fetch_all_tables()

    # Fetching all the rows from the table
    youtube_db.fetch_all_rows()

    if request.method == "POST" and "youtube_link" in request.form:
        user_url = str(request.form.get("youtube_link")).strip()

        video_details = helper.webscrapper(user_url)
        youtube_url = video_details.get("video_url")

    return render_template(
        "index.html",
        video_details=video_details
    )


@app.route("/download", methods=["GET", "POST"])
def download():
    try:
        try:
            download_path = (
                YouTube(youtube_url)
                .streams.get_audio_only()
                .download(filename=f"{video_details.get('video_title')}.mp3")
            )
        except:
            download_path = (
                YouTube(youtube_url)
                .streams.get_audio_only()
                .download(filename=f"{video_details.get('video_id')}.mp3")
            )

        fname = download_path.split("//")[-1]

        return send_file(
            fname,
            as_attachment=True,
        )

    except:
        logging.exception("Failed download")
        return "Video download failed!"
