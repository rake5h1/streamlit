import streamlit as st
from datetime import datetime

import numpy as np

import utils.display as display
import utils.globalDefine as globalDefine

from tinydb import TinyDB
db=TinyDB('meds.json')


def calc_main(title, subtitle):
    st.sidebar.title(title)
    st.sidebar.info(
        subtitle
    )
    id=st.text_input('Patient Id')
    date=st.date_input('Date')
    time=st.time_input('Time')
    med_a=st.text_input('Med A Quantity')
    med_b=st.text_input('Med B Quantity')
    med_c=st.text_input('Med C Quantity')
    if st.button('Clear Meds DB'):
        db.truncate()
    if st.button('Button'):
        db.insert({'A':med_a,'B':med_b,'C':med_c,'date':str(date),'id':int(id),'time':str(time)})
        st.write('Saved')
    
    