import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

with open('./src/model_lin_reg.pkl', 'rb') as file_1:
    model_lin_reg = pickle.load(file_1)

with open('./src/model_scaler.pkl', 'rb') as file_2:
    model_scaler = pickle.load(file_2)

with open('./src/model_encoder.pkl', 'rb') as file_3:
    model_encoder = pickle.load(file_1)

with open('./src/list_num_cols.txt', 'r') as file_4:
    list_num_cols = json.load(file_4)

with open('./src/list_cat_cols.txt', 'r') as file_5:
    list_cat_cols = json.load(file_5)

def run():
    st.title('Mari kita prediksi rating pemain FIFA...')
    st.subheader('Silahkan lengkapi form di bawah ini:')

    with st.form(key='Form Parameters'):
        Name = st.text_input('Name', value='John Doe')
        Age = st.slider('Age', min_value=16, max_value=54, value=26, help='Silahkan ') # pakai angka min dan max age, menghindari outlier
        Height= st.number_input('Height', min_value=155, max_value=206, value=172)
        Weight= st.number_input('Weight',value=70)
        # break dulu
        st.markdown('---')
        # lengkapi list form berdasarkan columns
        AttackingWorkRate= st.selectbox('AttackingWorkRate',['Low', 'Medium', 'High'], index=1)
        DefensiveWorkRate= st.radio('DefensiveWorkRate', ['Low', 'Medium', 'High'], index=1)

        st.markdown('---')
        # lengkapi list form berdasarkan columns

        submit= st.form_submit_button('Predict')

    data_inf = {
        'Name': Name,
        'Age': Age,
        'Height': Height,
        'Weight': Weight # lengkapi kolom
        #'Price': ValueEUR
        }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submit:
        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # feature scaling
        data_inf_num_scaled = model_scaler.transform(data_inf_num)

        # feature encoding
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)

        # concat data
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded])
        data_inf_final

        # predict
        y_pred_inf = model_lin_reg.predict(data_inf_final)
        st.markdown(f'##  Rating prediction of {Name}: {round(y_pred_inf[0],2)}')
if __name__ == '__main__':
    run()