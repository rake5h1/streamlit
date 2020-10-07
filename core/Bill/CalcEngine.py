import streamlit as st
from datetime import datetime

import numpy as np

import utils.display as display
import utils.globalDefine as globalDefine
import tinydb

db=tinydb.TinyDB('meds.json')



def calc_main(title, subtitle):
    st.sidebar.title(title)
    st.sidebar.info(
        subtitle
    )
    id=st.number_input('Patient Id')
    if st.button('Clear Bill DB'):
    
        db.truncate()
    if (st.button('Button')):
        acc=db.search(tinydb.Query().id==id)
        st.header('Bill')
        st.write(f'Registration Charges:Rs500')
        st.write(f'Med A Charges:Rs{int(acc[0]["A"])* 100}')
        st.write(f'Med B Charges:Rs{int(acc[0]["B"])* 200}')
        st.write(f'Med C Charges:Rs{int(acc[0]["C"])* 300}')
        Total=500+(int(acc[0]["A"])* 100)+(int(acc[0]["B"])* 200)+(int(acc[0]["C"])* 300)
        st.write(f'Total:Rs{Total}')