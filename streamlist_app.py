import streamlit as st
import pages.eda as eda
import pages.prediction as prediction

navigation = st.sidebar.selectbox('Pilih Halaman: '('EDA', 'Prediction'))

if navigation == 'EDA':
    eda.run()
elif navigation == 'Prediction':
    prediction.run()