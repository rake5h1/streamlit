import pathlib
import utils.display as udisp

import streamlit as st
import core.calculator.CalcEngine as CalcEngine

def write():
    udisp.title_awesome("Test Result")
    CalcEngine.calc_main('Test Result','Test Results')

