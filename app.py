import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.beds
import src.pages.Test
import src.pages.expenses
import src.pages.billing
import src.pages.symptoms
import src.pages.discharge
import src.pages.showexpenses
import src.pages.getresult

MENU = {
    "Register": src.pages.home,
    "Lab Report": src.pages.Test,
    "Available Beds": src.pages.beds,
    "Get Test Results": src.pages.getresult,
    "Patient Symptoms": src.pages.symptoms,
    "Patient Expenses": src.pages.expenses,
    "Generate Bill": src.pages.billing,
    "Discharge": src.pages.discharge,
    "Show Expenses": src.pages.showexpenses,
}


def main():
    st.sidebar.title("Navigate yourself...")
    menu_selection = st.sidebar.radio("Choice your option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)


if __name__ == "__main__":
    main()
