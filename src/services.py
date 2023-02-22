import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.environ.get("API_KEY")
youtube = build('youtube', 'v3', developerKey=API_KEY)


# Retrieve the comments for the specified video
def fetch_comments(video_id: str):
    comments = []
    next_page_token = ''
    while next_page_token is not None:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            order='relevance',
            pageToken=next_page_token
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        next_page_token = response.get('nextPageToken')

    return comments
