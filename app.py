import streamlit as st
from fastai.vision.all import *
import pathlib
import plotly.express as px


pathlib.PosixPath = pathlib.PosixPath
    
st.title('Qushlarni Klassifikatsiya qiluvchi model')
file=st.file_uploader('Rasmni yuklash',type=['png','jpg','jpeg','gif','svg'])
if file:
    st.image(file)
    model=load_learner('Birds_classification_model.pkl')
    img=PILImage.create(file)
    pred,pred_id,probs=model.predict(img)
    st.success(f'Bashorat : {pred}')
    st.info(f'Ehtimollik : {probs[pred_id]*100:.1f}')
    fig=px.bar(x=probs*100,y=model.dls.vocab)
    st.plotly_chart(fig)
