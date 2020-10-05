import pathlib
import utils.display as udisp

import streamlit as st


def write():
    udisp.title_awesome("Patient Registration")
    # udisp.render_md("resources/home_info.md")
    name = st.text_input("Name")
    age = st.text_input("Age")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    address=st.text_input('Address')
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