from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re
import streamlit as st


def extract_video_id(url):
 
    regex = (
        r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/|v/|shorts/|.+\?v=)|youtu\.be/)' +
        r'([a-zA-Z0-9_-]{11})'
    )
    match = re.search(regex, url)
    if match:
        return match.group(1)  
    return None


def video_comments(video_id):
    
    all_comments = []

    try:
        api_key = st.secrets["api_keys"]["API_KEY_Y"]
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100  
        ).execute()

        while video_response:
            for item in video_response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                all_comments.append(comment)

            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    pageToken=video_response['nextPageToken'],
                    maxResults=100
                ).execute()
            else:
                break

    except HttpError as e:
        print(f"An error occurred: {e}")
        return []

    return all_comments



