import pathlib
import utils.display as udisp

import streamlit as st
import core.Bill.CalcEngine as CalcEngine

def write():
    udisp.title_awesome("Generate Bill")
    CalcEngine.calc_main("Bill", "Generate Bill")

