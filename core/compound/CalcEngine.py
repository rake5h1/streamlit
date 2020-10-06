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
    med_a=st.text_input('Med A Quantity')
    med_b=st.text_input('Med B Quantity')
    med_c=st.text_input('Med C Quantity')
    if st.button('Button'):
        st.write('Saved')
    
    