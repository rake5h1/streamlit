import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.about
import src.pages.Test
import src.pages.compound
import src.pages.scikit_image

MENU = {
    "Register": src.pages.home,
    "Lab Report": src.pages.Test,
    "Patient Expenses": src.pages.compound,
    "Generate Bill": src.pages.scikit_image,
    "Available Beds": src.pages.about,
}


def main():
    st.sidebar.title("Navigate yourself...")
    menu_selection = st.sidebar.radio("Choice your option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)


if __name__ == "__main__":
    main()
