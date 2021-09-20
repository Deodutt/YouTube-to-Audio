from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import requests


def id_grabber(youtube_url):
    youtube_id = None
    # reference: https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python/54383711#54383711
    query = urlparse(youtube_url)

    if query.hostname == "youtu.be":
        youtube_id = query.path[1:]

    elif query.hostname in {"www.youtube.com", "youtube.com"}:
        if query.path == "/watch":
            youtube_id = parse_qs(query.query)["v"][0]

        elif query.path[:7] == "/watch/":
            youtube_id = query.path.split("/")[1]

        elif query.path[:7] == "/embed/":
            youtube_id = query.path.split("/")[2]

        elif query.path[:3] == "/v/":
            youtube_id = query.path.split("/")[2]

        # below is optional for playlists
        elif query.path[:9] == "/playlist":
            youtube_id = parse_qs(query.query)["list"][0]

    return youtube_id


def webscrapper(youtube_url):
    video_details = {}
    # print(youtube_url)
    req = requests.get(youtube_url)
    soup = BeautifulSoup(req.content, 'html.parser')

    video_details['video_title'] = soup.find(
        "meta", itemprop="name").attrs.get('content')

    video_details['video_author'] = soup.find(
        "link", itemprop="name").attrs.get('content')

    video_details['video_views'] = soup.find(
        "meta", itemprop="interactionCount").attrs.get('content')

    video_details['video_published'] = soup.find(
        "meta", itemprop="datePublished").attrs.get('content')

    video_details['video_duration'] = soup.find(
        "meta", itemprop="duration").attrs.get('content')

    video_details['video_id'] = soup.find(
        "meta", itemprop="videoId").attrs.get('content')

    video_details['video_thumbnail'] = soup.find(
        "link", itemprop="thumbnailUrl").attrs.get('href')

    print(video_details)

    return video_details
