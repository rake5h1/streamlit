import streamlit as st
import pathlib
import utils.display as udisp

import requests as rs
from tinydb import TinyDB, Query
import random


def write():
    udisp.title_awesome("Show Expenses")
    db=TinyDB('meds.json')
    id=st.number_input('Patient Id')
    Find=Query()
    if st.button('Button'):
        exp=db.search(Find.id==id)
        st.write(exp)
    