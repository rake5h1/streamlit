import pathlib
import utils.display as udisp

import streamlit as st
import core.expenses.CalcEngine as CalcEngine

def write():
    udisp.title_awesome("Expenses")
    CalcEngine.calc_main("Billing", "Billing Section")

