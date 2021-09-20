from __future__ import unicode_literals
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import helper
import logging
from pytube import YouTube

application = app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def converter():
    # Needs to be global for the /download route
    global youtube_url, youtube_id
    youtube_url = ""
    youtube_id = ""
    video_details = []

    if request.method == "POST" and "youtube_link" in request.form:
        youtube_url = str(request.form.get("youtube_link")).strip()
        youtube_id = str(helper.id_grabber(youtube_url))

        video_details = helper.webscrapper(youtube_url)

    return render_template(
        "index.html",
        youtube_url=youtube_url,
        youtube_id=youtube_id,
    )


@app.route("/download", methods=["GET", "POST"])
def download():
    try:
        download_path = (
            YouTube(youtube_url)
            .streams.get_audio_only()
            .download(filename=f"{youtube_id}.mp3")
        )
        fname = download_path.split("//")[-1]

        # This sends a file from locally downloaded to the web browser to download.
        # Files are stored on /var/app/current in the EC2 instance
        return send_file(
            fname,
            as_attachment=True,
        )

    except:
        logging.exception("Failed download")
        return "Video download failed!"
