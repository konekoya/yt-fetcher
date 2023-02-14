from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")
youtube = build('youtube', 'v3', developerKey=API_KEY)

# TODO: This should be read from CLI or UI
video_id = '0sOvCWFmrtA'

# Retrieve the comments for the specified video
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

# Print out the comments for the video
index = 0
for comment in comments:
    index += 1
    print(f'{index}: {comment}')
