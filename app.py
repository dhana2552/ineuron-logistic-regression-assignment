import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open('model.pkl', 'rb'))

st.title('Logistic Regression Assignment')

#rate_marriage
rate_marriage = st.selectbox('Select the rating: ', [1., 2., 3., 4., 5.])

#age
age = st.selectbox('Select the age: ', [17., 22., 27., 32., 37., 42.])

#yrs_married
yrs_married = st.selectbox('Select married years: ', [0., 2., 6., 9., 13., 16., 23.])

#children
children = st.selectbox('Select children count: ', [0., 1., 2., 3., 4., 5.])

#religious
religious = st.selectbox('Select the rating for being religious', [1., 2., 3., 4.])

#educ
educ = st.selectbox('Select level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)', [9., 12., 14., 16., 17., 20.])

#occupation
occupation = st.selectbox('Select occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = white collar, 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)', [1., 2., 3., 4., 5., 6.])

#occupation_husb
occupation_husb= st.selectbox("Select husband's occupation (coding same as above): ", [1., 2., 3., 4., 5., 6.])

#affairs
affairs = st.number_input("Select the time spent in extra-marital affairs (0.0 to 60.0): ")

query = np.array([rate_marriage, age, yrs_married, children, religious, educ, occupation, occupation_husb, affairs]).reshape(1, 9)

if st.button('Predict'):
    prediction = model.predict(query)[0]
    if prediction == 1:
        st.title('This women is predicted to have another affair')
    else:
        st.title('This women is predicted NOT to have an extra marital affair')