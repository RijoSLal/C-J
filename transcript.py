from youtube_transcript_api import YouTubeTranscriptApi
import re
import streamlit as st
from transformers import pipeline

def idea(tr):
    if tr is not None:
        try:
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  
            summary = summarizer(tr, max_length=130, min_length=30, do_sample=False)
            return summary[0]["summary_text"]
        except Exception:
            return f"Oops, something went wrong"
    return "Please share the video link, and I'll create a brief description"



def extract_video_id(url):
   
    regex = (
        r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/|v/|shorts/|.+\?v=)|youtu\.be/)' +
        r'([a-zA-Z0-9_-]{11})'
    )
    match = re.search(regex, url)
    if match:
        return match.group(1)  
    return None


def extract_transcript_details(youtube_video_url):
    try:
        video_id=extract_video_id(youtube_video_url)
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception:
        return None



def transcripted_data(prompt):
    trans=extract_transcript_details(prompt)
    talk = idea(trans)
    return talk

        
