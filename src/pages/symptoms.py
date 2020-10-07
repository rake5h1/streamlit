import pathlib
import utils.display as udisp

import streamlit as st
import requests as rs
from tinydb import TinyDB, Query
import random


def write():
    udisp.title_awesome("Patient Symptoms")
    db=TinyDB('patients.json')
    id=st.number_input('Patient Id')
    Find=Query()
    if st.button('Button'):
        sym=db.search(Find.id==id)
        st.write(sym[0]['symptoms'])