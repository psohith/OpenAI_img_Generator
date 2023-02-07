#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:26:50 2023
@author: Pamu sohith
email : pamusohith@gmail.com
"""

import openai
import urllib.request
from PIL import Image
import streamlit as st

# fuction to generate img using OpenAI
openai.api_key = 'API_KEY'

def generate_img(description):
    img_response = openai.Image.create(
        prompt = description,
        n =1,
        size = '512x512'
        )
    img_link = img_response['data'][0]['url']
    urllib.request.urlretrieve(img_link, 'img.png')
    img = Image.open('img.png')
    return img

# streamlit UI
st.title('DALL E - Image Generation ')

#input
desc = st.text_input('Image Description')

if st.button('Generate'):
    img = generate_img(desc)
    st.image(img)
