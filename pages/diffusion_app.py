import streamlit as st
import requests
from PIL import Image
from io import BytesIO

IMG_GEN_URL = 'http://stardust-ai.asuscomm.com:9021/generate'
IMG2IMG_URL = 'http://stardust-ai.asuscomm.com:9021/img2img'

st.set_page_config(page_title="图像生成", page_icon="🤡", layout="wide",)

st.title('文本图像生成')

st.sidebar.info('👉🏻可配置参数，不懂勿动')
steps = st.sidebar.slider('迭代次数', 15, 100, 50)
scale = st.sidebar.slider('文本强度', 5.0, 10.0, 7.5)

# file = st.file_uploader('请上传图片', type=['jpg', 'png'])
default_prompt = 'a photo of a self-driving car on the street'
img0 = None
prompt = st.text_input('请输入提示文本', default_prompt)
with st.expander("（可选）基于初始图片+文本进行生成，不选则仅适用文本进行生成"):
    img0 = st.file_uploader('请上传图片', type=['jpg', 'png', 'jpeg'])
    if img0 is not None:
        st.image(img0, caption='初始图片', use_column_width=True)
        strength = st.sidebar.slider('初始图片随机度', 0.0, 1.0, 0.75)

if prompt and not img0:
    if prompt == default_prompt:
        st.text('default image')
        image = Image.open('pages/assets/default.png')
    else:
        st.text('text only')
        r = requests.get(
            IMG_GEN_URL, 
            params={'prompt': prompt, 'steps': steps, 'scale': scale}, 
        )
        assert r.status_code == 200
        image = Image.open(BytesIO(r.content))
elif prompt and img0:
    st.text('text + image')
    r = requests.get(
        IMG2IMG_URL, 
        params={'prompt': prompt, 'steps': steps, 'scale': scale, 'strength': strength}, 
        files={'image': img0}
    )
    assert r.status_code == 200
    image = Image.open(BytesIO(r.content))
st.image(image, caption=prompt)

st.header('')
st.header('')
st.header('')
st.header('')
st.header('')
st.image(
    'http://work.startask.net/static/media/logo2.0b1967eb.png',
    caption='Copyright Stardust @2022',
    width=200
)
