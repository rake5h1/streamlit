import pathlib
import utils.display as udisp

import streamlit as st
import requests as rs
from tinydb import TinyDB, Query
import random


def write():
    udisp.title_awesome("Patient Registration")
    # udisp.render_md("resources/home_info.md")
    name = st.text_input("Name")
    age = st.text_input("Age")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    address=st.text_input('Address')
    date=st.date_input('Date')
    time=st.time_input('Time')
    report=st.text_input('Test Result')
    id=random.getrandbits(30)
    # doc=st.radio('Doctor',['Dr. A','Dr. B'])
    db=TinyDB('patients.json')
  
   
    if st.checkbox('Has Fever ?'):
        fever=True
    if st.checkbox('Has Cough ?'):
        cough=True
    if st.checkbox('Breathing Problem ?'):
        breathingproblem=True
    if st.checkbox('Has Diarrohea ?'):
        diarrohea=True
    if st.checkbox('Tiredness ?'):
        tiredness=True
    if st.button('Clear Patient DB'):
        db.truncate()
    if st.button('Button'):
        # res=rs.get("https://jsonplaceholder.typicode.com/posts")
        # st.write(res.text)
        db.insert({'id':id,'name': name, 'age': int(age),'phone':int(phone),'email':str(email),'date':str(date),'time':str(time)})
        for item in db:
            st.write(f'Patient Id:{id}')
            
    