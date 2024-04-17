from transformers import BertTokenizer, BertModel
import torch
from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()


tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")


def get_pinecone_connection():
    print(os.getenv('PINECONE_API_KEY'))
    return Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

def get_bert_embeddings(text):
    inputs = tokenizer(
        text, return_tensors="pt", padding=True, truncation=True, max_length=512
    )
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.pooler_output[0].numpy()

def get_model():
    return model

