import numpy as np
import albumentations as albu
import streamlit as st
import torch
from PIL import Image

import model

MAX_SIZE = 512

def cached_model():
    model = create_model('Unet_2020-07-20')
    model.eval()
    return model

model = cached_model()

st.title('app for removing background')

file = st.file_uploader('사람 사진을 선택해주세요', type=['jpg', 'jpeg', 'png'])

if file is not None:
    img_ori = np.array(Image.open(file).convert('RGB'))
    st.image(img_ori, caption="original img")