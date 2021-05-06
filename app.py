import streamlit as st
import classify_page as cp
import explore_tweet_train_page as ettp
import explore_tweet_predict_page as etpp

# page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
#
# if page == "Predict":
#     print()
#     # show_predict_page()
# else:
#     df = ep.load_data()
#     ep.show_explore_page(df)

import pickle as pkle
import os.path

st.sidebar.title('ANTISOCIALINA APP')

next = st.sidebar.button('Choose Next Menu')

new_choice = ['Explore Data Labelling','Explore Data Testing','Classifying','About']

if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    if next_clicked == len(new_choice):
        next_clicked = 0
else:
    next_clicked = 0

if next:
    next_clicked = next_clicked +1

    if next_clicked == len(new_choice):
        next_clicked = 0

choice = st.sidebar.radio("Go to Page:",('Explore Data Labelling','Explore Data Testing','Classifying','About'), index=next_clicked)

pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

if choice == 'Explore Data Labelling':
    df = ettp.load_data()
    ettp.show_explore_page(df)
elif choice == 'Explore Data Testing':
    df = etpp.load_data()
    etpp.show_explore_page(df)
elif choice == 'Classifying':
    data = ettp.load_data()
    cp.show_classify_predict_page(data['formalizing'])
elif choice == 'About':
    st.title("About")

    st.write(
        """
    ### Aplikasi ini merupakan salah satu frontend dari aplikasi monitoring perilaku antisosial berdasarkan data dari Twitter di Indonesia.
    ### Aplikasi ini juga merupakan tugas akhir mata kuliah Sistem Intelijen dari Fitri Andri Astuti/ 23220030@std.stei.itb.ac.id
    """
    )