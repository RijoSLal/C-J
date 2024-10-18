from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv
import streamlit as st


api_key = st.secrets["api_keys"]["API_KEY_Y"]

def video_comments(video_id):

    all_comments = []
    
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id
        ).execute()

        while video_response:
            for item in video_response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                all_comments.append(comment)

            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    pageToken=video_response['nextPageToken']
                ).execute()
            else:
                break

    except HttpError:
        return []

    return all_comments


