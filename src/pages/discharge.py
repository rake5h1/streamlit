import pathlib
import utils.display as udisp

import streamlit as st
import requests as rs
from tinydb import TinyDB, Query
import random


def write():
    db=TinyDB('patients.json')
    udisp.title_awesome("Patient Discharge")
    id=st.number_input('Patient Id')
    dis_date=st.date_input('Discharge Date')
    if st.button('Button'):
        Find=Query()
        db.update({'id':id,'dis_date':str(dis_date)},Find.id==id)
    
    