from bs4 import BeautifulSoup
import requests


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

    return