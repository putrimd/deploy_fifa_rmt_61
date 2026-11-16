import streamlit as st
import pages.eda as eda
import pages.prediction as prediction

st.sidebar.title('Navigation')
navigation = st.sidebar.selectbox('Pilih Halaman: ',('EDA', 'Prediction'))

if navigation == 'EDA':
    eda.run()
elif navigation == 'Prediction':
    prediction.run()

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
display: none;
}
</style>
""", unsafe_allow_html=True)