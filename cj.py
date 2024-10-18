import streamlit as st
import pandas as pd
import altair as alt
import time
import model
import yt_api
import transcript



st.title("ᒡ◯ᵔ◯ᒢ")

class Progress:
    def progress(self,rate,text,color):
        progress_placeholder = st.empty()

        for percent_complete in range(rate):
            time.sleep(0.04) 

            progress_html = f"""
            <div style='width: 100%;'>
                <div style='margin-bottom: 5px; color: white; text-align: left; font-size:15px; font-weight: bold; font-family: monospace;'>{text} : {percent_complete + 1}%</div>
                <div style='width: 100%; background-color: rgb(38, 39, 48); border-radius: 100px;'>
                    <div style='width: {percent_complete + 1}%; background-color: {color}; height: 6px; border-radius: 100px;'></div>
                </div>
                <div style='margin-bottom: 20px;margin-top: 30px;'></div> 
            </div>
            """
            
            progress_placeholder.markdown(progress_html, unsafe_allow_html=True)

    def dummy(self,rate,text,color):
        progress_placeholder = st.empty()

        for percent_complete in range(rate):
            time.sleep(0.01) 
            
            progress_html = f"""
            <div style='width: 100%;'>
                <div style='margin-bottom: 5px; color: white; text-align: left; font-size:15px ; font-weight: bold; font-family: monospace;'>{text} : {percent_complete + 1}%</div>
                <div style='width: 100%; background-color: rgb(38, 39, 48); border-radius: 100px;'>
                    <div style='width: {percent_complete + 1}%; background-color: {color}; height: 6px; border-radius: 100px;'></div>
                </div>
                <div style='margin-bottom: 20px;margin-top: 30px;'></div>  
            </div>
            """
            progress_placeholder.markdown(progress_html, unsafe_allow_html=True)

        for percent_complete in range(rate, -1, -1):
            time.sleep(0.01)
            progress_html = f"""
            <div style='width: 100%;'>
                <div style='margin-bottom: 5px; color: white; text-align: left; font-size:15px ; font-weight: bold; font-family: monospace;'>{text} : {percent_complete}%</div>
                <div style='width: 100%; background-color: rgb(38, 39, 48); border-radius: 100px;'>
                    <div style='width: {percent_complete}%; background-color: {color}; height: 6px; border-radius: 100px;'></div>
                </div>
                <div style='margin-bottom: 20px;margin-top: 30px;'></div> 
            </div>
            """
            progress_placeholder.markdown(progress_html, unsafe_allow_html=True)


class module:
    def __init__(self,video_url):
        self.video_url=video_url
    
    def dictionary(self):
        if self.video_url:
            try:
                video_id = self.video_url.split("v=")[-1].split("&")[0]
                comments_data = yt_api.video_comments(video_id)
                some=model.iteration(comments_data) 
                return some
            except IndexError:
                st.error("𝙾𝚘𝚙𝚜! 𝚃𝚑𝚎 𝚟𝚒𝚍𝚎𝚘 𝚄𝚁𝙻 𝚏𝚘𝚛𝚖𝚊𝚝 𝚊𝚙𝚙𝚎𝚊𝚛𝚜 𝚝𝚘 𝚋𝚎 𝚒𝚗𝚟𝚊𝚕𝚒𝚍 𝚘𝚛 𝚗𝚘 𝚌𝚘𝚖𝚖𝚎𝚗𝚝𝚜")
                return None
        else:
            return None
        



class display:
    def __init__(self,prog,lines,talk):
        self.prog=prog
        self.lines=lines
        self.talk=talk
    
        
    def get_chart_19651(self):
    
        if self.lines is None:
            pos,neu,neg=0,0,0
        else:
            pos=round(self.lines["Positive"])
            neu=round(self.lines["Neutral"])
            neg=round(self.lines["Negative"])

        source = pd.DataFrame({"𝚃𝚎𝚗𝚎𝚝": ["𝙿𝚘𝚜𝚒𝚝𝚒𝚟𝚎", "𝙽𝚎𝚞𝚝𝚛𝚊𝚕", "𝙽𝚎𝚐𝚊𝚝𝚒𝚟𝚎"], "Value": [pos, neu, neg]})


        base = alt.Chart(source).encode(
        theta=alt.Theta("Value:Q", stack=True),
        radius=alt.Radius("Value", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
        color=alt.Color("𝚃𝚎𝚗𝚎𝚝:N", scale=alt.Scale(domain=["𝙿𝚘𝚜𝚒𝚝𝚒𝚟𝚎", "𝙽𝚎𝚞𝚝𝚛𝚊𝚕","𝙽𝚎𝚐𝚊𝚝𝚒𝚟𝚎"],
                                                    range=["#AAFF00", "yellow", "red"])))

        c1 = base.mark_arc(innerRadius=100, stroke="#fff")

        c2 = base.mark_text(radiusOffset=10).encode(text="Value:Q")

        chart = c1 + c2
        tab1, tab2 = st.tabs(["𝚅𝙸𝙱𝙴-𝙾-𝙼𝙴𝚃𝙴𝚁", "𝚁𝙰𝙳𝙸𝙰𝙻-𝙲𝙷𝙰𝚁𝚃"])

        with tab2:
            st.write("𝚃𝚘𝚛𝚞𝚜")
            st.altair_chart(chart, theme="streamlit", use_container_width=True)
        with tab1:
            time.sleep(0.5)  
            for value, label, color in zip([pos, neu, neg], ["Positive", "Neutral", "Negative"], ["#AAFF00", "yellow", "red"]):
                if value == 0:
                    self.prog.dummy(50, label, color)
                else:
                    self.prog.progress(value, label, color)
            st.write("𝙳𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗")
            st.markdown(f'<p style="font-size: 14px; color: white; font-family: Courier New;">{self.talk}</p>', unsafe_allow_html=True)
            

def final(prompt,color):
    prog=Progress()
    prog.progress(100,"Loading",color)
    mode=module(prompt)
    lines=mode.dictionary()
    talk=transcript.transcripted_data(prompt)
    dis=display(prog,lines,talk)
    dis.get_chart_19651()




if __name__=="__main__":
    prompt = st.chat_input("𝙸𝚗𝚜𝚎𝚛𝚝 𝙻𝚒𝚗𝚔")
    final(prompt, "blue")

