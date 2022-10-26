# Simple_chatbot
build c hatbot model and deploy it with a Gradio interface

#A chatbot is a computer program that uses artificial intelligence (AI) and natural language processing (NLP) to understand

customer questions and automate responses to them, simulating human conversation

 in this project you tried to make a simple chatbot with hagginface transformes(an immensely popular Python library providing pretrained models 
 
 that are extraordinarily useful for a variety of natural language processing (NLP) tasks.
 
 It previously supported only PyTorch, but, as of late 2019, TensorFlow 2 is supported as well)
 
 #First, download a pretrained model, we  used a pretrained chatbot model, DialoGPT, BlenderBot
 and its tokenizer from the Hugging Face Hub, also  you can replace this with your own model
 
 #Next,  defined a function(predect) that takes in the user input as well as the previous chat history to generate a response.
 
history: which represents the state, consisting of the list of user and bot responses.
To create a stateful Gradio demo, we must pass in a parameter to represent the state, and we set the default value of this parameter to be the initial 
value of the state (in this case, the empty list since this is what we would like the chat history to be at the start).
Then, the function tokenizes the input and concatenates it with the tokens corresponding to the previous user and bot responses.
Then, this is fed into the pretrained model to get a prediction. Finally, we do some cleaning up so that we can return two values from our function:

response: which is a list of tuples of strings corresponding to all of the user and bot responses. This will be rendered as the output in the Gradio demo.
history variable, which is the token representation of all of the user and bot responses. 
In stateful Gradio demos, we must return the updated state at the end of the function.

FINALLy,create a Gradio Interface around it.
for more details :
   https://www.gradio.app/creating_a_chatbot/
   
  
   
    
   
   
