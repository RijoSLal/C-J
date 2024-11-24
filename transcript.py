from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import re
import streamlit as st

def idea(tr):
    script="""You are Yotube video summarizer. You will be taking the transcript text
    and summarizing the entire video within 100 words. Please provide the summary of the text given here:  """
    if tr is not None:
        try:
            key = st.secrets["api_keys"]["API_KEY_T"]
            genai.configure(api_key=key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"{script+tr}")
            return response.text
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

        
