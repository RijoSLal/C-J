from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st


key = st.secrets["api_keys"]["API_KEY_T"]

def idea(tr,scr):
    
    if tr is not None:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"{scr+tr}")
            return response.text
        except Exception:
            return f"Oops, something went wrong"
    return "Please share the video link, and I'll create a brief description"




def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception:
        return None


# def extract_transcript_details(youtube_video_url):
#     try:
#         video_id = youtube_video_url.split("v=")[-1].split("&")[0]
#         transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
#         transcript = " ".join([i["text"] for i in transcript_text])
#         return transcript

#     except Exception as e:
#         return None

def transcripted_data(prompt):
    trans=extract_transcript_details(prompt)
    script="""You are Yotube video summarizer. You will be taking the transcript text
    and summarizing the entire video within 100 words. Please provide the summary of the text given here:  """
    talk = idea(trans,script)
    return talk

        
