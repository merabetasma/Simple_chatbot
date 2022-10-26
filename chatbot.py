# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11GgHhHEk4KER1AtkHdumDGBRy-Q8gK50

#Import Hugging Face transformers
"""

!pip install transformers

"""# Pretrained model"""

from transformers import AutoModelForCausalLM, AutoTokenizer, BlenderbotTokenizer, TFBlenderbotForConditionalGeneration
import tensorflow as tf
import torch

chat_bots = {
    'BlenderBot': [BlenderbotTokenizer.from_pretrained('facebook/blenderbot-400M-distill'), TFBlenderbotForConditionalGeneration.from_pretrained('facebook/blenderbot-400M-distill')],
    'DialoGPT': [AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium"), AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")],
} 
key = 'DialoGPT'
tokenizer, model = chat_bots[key]

def predict(input, history=[]):
    # tokenize the new input sentence
    new_user_input_ids = tokenizer.encode(input + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
   
    bot_input_ids = torch.cat([torch.LongTensor(history), new_user_input_ids], dim=-1)
    # generate a response 
    history = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id).tolist()

    # convert the tokens to text, and then split the responses into lines
    response = tokenizer.decode(history[0]).split("<|endoftext|>")
    response = [(response[i], response[i+1]) for i in range(0, len(response)-1, 2)]  # convert to tuples of list
    return response, history
    

    #html
    #html="<div class='chatbot'>"
    #for m,msg in enumerate(response):
      #cls= "user" if m%2 == 0 else "bot "
      #html+="<div class='msg {}'> {}</div>".format(cls,msg)
    #html+= "</div>"
    #return html , history

"""# Creating a Gradio Interface"""

import gradio as gr

gr.Interface(fn=predict,
             inputs=["text", "state"],
             outputs=["chatbot", "state"]).launch(debug=True)