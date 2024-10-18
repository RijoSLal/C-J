from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv
import streamlit as st
import re

api_key = st.secrets["api_keys"]["API_KEY_Y"]

def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL or short link.
    """
    regex = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(regex, url)
    return match.group(1) if match else None

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



# api_key = st.secrets["api_keys"]["API_KEY_Y"]

# def video_comments(video_id):
  
#     all_comments = []
    
#     try:
#         youtube = build('youtube', 'v3', developerKey=api_key)
#         video_response = youtube.commentThreads().list(
#             part='snippet',
#             videoId=video_id
#         ).execute()

#         while video_response:
#             for item in video_response['items']:
#                 comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#                 all_comments.append(comment)

#             if 'nextPageToken' in video_response:
#                 video_response = youtube.commentThreads().list(
#                     part='snippet',
#                     videoId=video_id,
#                     pageToken=video_response['nextPageToken']
#                 ).execute()
#             else:
#                 break

#     except HttpError:
#         return []

#     return all_comments


