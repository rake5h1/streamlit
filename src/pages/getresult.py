import pathlib
import utils.display as udisp

import streamlit as st
from tinydb import TinyDB,Query

def write():
    udisp.title_awesome("Test Result")
    id=st.number_input('Patient Id')
    db=TinyDB('reports.json')
    Find=Query()
    if st.button('Button'):
        res=db.search(Find.id==id)
        st.write(res)
    
    
    

