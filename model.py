import torch
import numpy as np
from scipy.special import softmax
from transformers import AutoTokenizer,AutoModelForSequenceClassification,AutoConfig
import re

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def preprocess(text):
    text = re.sub(r'@\w+', '@user', text) 
    text = re.sub(r'http\S+', 'http', text) 
    return text

def iteration(list_com, batch_size=32):
    evaluation = []
    model.eval() 

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    for i in range(0, len(list_com), batch_size):
        batch = list_com[i:i + batch_size]  
        processed_batch = [preprocess(text) for text in batch]

        encoded_input = tokenizer(processed_batch, return_tensors='pt', padding=True, truncation=True, max_length=512)
    
        input_ids = encoded_input['input_ids'].to(device)
        attention_mask = encoded_input['attention_mask'].to(device)
        
        with torch.no_grad():
            output = model(input_ids=input_ids, attention_mask=attention_mask)

   
        scores = output.logits.detach().cpu().numpy()
        probabilities = softmax(scores, axis=1)

        evaluation.extend(probabilities) 
    
    total_scores=np.sum(evaluation,axis=0)
    total_summation=np.sum(evaluation)

    freq={"Negative":round((total_scores[0]/total_summation)*100,2),
          "Neutral": round((total_scores[1]/total_summation)*100,2),
          "Positive" :round((total_scores[2]/total_summation)*100,2)}
    
    return freq