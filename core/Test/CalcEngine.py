import streamlit as st
from datetime import datetime

import numpy as np

import utils.display as display
import utils.globalDefine as globalDefine
from tinydb import TinyDB, Query

db=TinyDB('reports.json')


def calc_main(title, subtitle):
    st.sidebar.title(title)
    st.sidebar.info(
        subtitle
    )
    id=st.number_input('Patient Id')
    result=st.text_input('Test Result')
    date=st.date_input('Date')
    if st.button('Clear Test DB'):
        db.truncate()
    if st.button('Set Test Result'):
        db.insert({'report':result,'id':int(id),'date':str(date)})

    