import streamlit as st
from datetime import datetime

import numpy as np

import utils.display as display
import utils.globalDefine as globalDefine
import tinydb

db=tinydb.TinyDB('meds.json')
pat_db=tinydb.TinyDB('patients.json')



def calc_main(title, subtitle):
    st.sidebar.title(title)
    st.sidebar.info(
        subtitle
    )
    id=st.number_input('Patient Id')
    # date1=datetime.strptime("12-12-2020",'%d-%m-%Y')
    # date2=datetime.strptime("13-12-2020",'%d-%m-%Y')

    # st.write((date2-date1).days)
    if st.button('Clear Bill DB'):
    
        db.truncate()
    if (st.button('Button')):
        acc=db.search(tinydb.Query().id==id)
        pat=pat_db.search(tinydb.Query().id==id)
        # st.write(pat)
        date1=datetime.strptime(pat[0]['date'],'%Y-%m-%d')
        date2=datetime.strptime(pat[0]['dis_date'],'%Y-%m-%d')
        days=(date2-date1).days
        other_charges=int(days)*500
        st.header('Bill')
        st.write(f'Registration Charges:Rs500')
        st.write(f'Med A Charges:Rs{int(acc[0]["A"])* 100}')
        st.write(f'Med B Charges:Rs{int(acc[0]["B"])* 200}')
        st.write(f'Med C Charges:Rs{int(acc[0]["C"])* 300}')
        st.write(f'Other Charges:Rs{other_charges}')
        Total=500+(int(acc[0]["A"])* 100)+(int(acc[0]["B"])* 200)+(int(acc[0]["C"])* 300)
        st.write(f'Total:Rs{Total}')