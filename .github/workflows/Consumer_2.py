# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:21:25 2024

@author: USER
"""

import requests

url = "http://127.0.0.1:8000/text_to_speech/"

# Enter the text and language code
text = "This is a sample text."
text1 = "সুপ্রভাত! আমি আশা করি আপনার দিন ভালো কাটবে"
text2 = " रोज़ कोई नया कदम उठाएं, और ज़िन्दगी का आनंद लें।"
language = "en"
language1 = "bn"
language2 = "hi"

# Send POST request to the producer API
response = requests.post(url, json={"text": text2, "language": language2})

if response.status_code == 200:
    print("Text to speech conversion started successfully.")
else:
    print("Error:", response.status_code)
