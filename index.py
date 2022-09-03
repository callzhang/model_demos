import streamlit as st

st.set_page_config(page_title="Model Gallery", page_icon="🛣️", layout="wide",)

st.title('模型展示目录')

st.header('车道线识别')
st.text('使用CLRNet模型进行车道线识别')
st.header('图像生成')
st.text('使用Stable Diffusion模型进行图像生成')