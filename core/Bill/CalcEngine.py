import streamlit as st
from datetime import datetime

import numpy as np

import utils.display as display
import utils.globalDefine as globalDefine

def calc_main(title, subtitle):
    st.sidebar.title(title)
    st.sidebar.info(
        subtitle
    )
    id=st.number_input('Patient Id')
    if (st.button('Button')):
        
        st.write('Bill')