import numpy as np
import streamlit as st
import albumentations as albu
from PIL import Image

st.title('app for removing background')

file = st.file_uploader('사람 사진을 선택해주세요', type=['jpg', 'jpeg', 'png'])