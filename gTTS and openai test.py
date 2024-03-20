import serial
import time
from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import openai
import os

openai.api_key = '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'
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

try:
    while True:
        message = input("User: ")
        if message:
                messages.append({"role": "user", "content": message})
                chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)      
                reply = chat.choices[0].message.content
                print(f"ChatGPT: {reply}")
                messages.append({"role": "assistant", "content": reply})  
                text = reply
                tts = gTTS(text, slow=False, pre_processor_funcs = [abbreviations, end_of_line]) # Save the audio in a mp3 file
                tts.save('hello.mp3')# Play the audio
                mixer.init()
                mixer.music.load("hello.mp3")
                mixer.music.play()# Wait for the audio to be played
                time.sleep(2)
                
except KeyboardInterrupt:
    print("End")
    