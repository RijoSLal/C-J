from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai


key="AIzaSyDjsNjiubGnjk3dxpBdHoY6b3qQ9W26EKE"

class Description:
    def __init__(self,transcripted,prompted):
        self.transcripted=transcripted
        self.prompted=prompted

    def idea(self):
        if self.transcripted is not None:
            try:
                genai.configure(api_key=key)
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(f"{self.prompted+self.transcripted}")
                return response.text
            except Exception:
                return f"Oops, something went wrong"
        return "Please share the video link, and I'll create a brief summary"




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

def transcripted_data(prompt):
    trans=extract_transcript_details(prompt)
    script="""You are Yotube video summarizer. You will be taking the transcript text
    and summarizing the entire video within 100 words. Please provide the summary of the text given here:  """
    describe = Description(trans,script)
    talk = describe.idea()
    return talk

        
