
from youtube_transcript_api import YouTubeTranscriptApi
import re
import streamlit as st
from transformers import LEDTokenizer, LEDForConditionalGeneration
import torch

model_name = "allenai/led-base-16384"  
tokenizer = LEDTokenizer.from_pretrained(model_name)
model = LEDForConditionalGeneration.from_pretrained(model_name)


model.gradient_checkpointing_enable()

def idea(tr):
   
    if tr is None or not tr.strip():
        return "Please share the video link, and I'll create a brief description."
    
    try:
        
        inputs = tokenizer(
            tr,
            return_tensors="pt",
            max_length=4096,  
            truncation=True
        )
        
     
        global_attention_mask = torch.zeros_like(inputs['input_ids'])
        global_attention_mask[:, 0] = 1
        
     
        summary_ids = model.generate(
            inputs['input_ids'],
            global_attention_mask=global_attention_mask,
            num_beams=4,
            max_length=150, 
            early_stopping=True
        )
        
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    
    except Exception as e:
        return f"Oops, something went wrong: {str(e)}"




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

        
