import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

nb_model_loaded = data['nb_model']
lr_model_loaded = data['lr_model']
dt_model_loaded = data['dt_model']
rf_model_loaded = data['rf_model']
svm_model_loaded = data['svm_model']
le_classname = data['le_classname']
le_idClass = data['le_idClass']

def show_classify_predict_page(data):
    st.title("Text Classify Prediction")

    st.write("""##### Test some text to predict the classification of antisocial model machine learning""")

    text = st.text_input('Text','')

    classname_label = {
        5: 'Non-Antisosial / Umum',
        1: 'Kegagalan untuk menyesuaikan diri dengan norma-norma sosial tentang perilaku yang sah',
        2: 'Iritabilitas dan Agresivitas',
        3: 'Pengabaian yang gegabah untuk Keamanan',
        4: 'Kurangnya Penyesalan',
    }

    ok = st.button("Classify Text!")
    #if click ok button value is true, else is false
    if ok or text:
        vect = TfidfVectorizer()
        vector_output = vect.fit_transform(data)
        classify = rf_model_loaded.predict(vect.transform([text]).toarray())
        st.subheader(f"The estimated result of this text \"{text}\" is: \n idClass: {classify[0]}, \n classname: {classname_label[classify[0]]}")

