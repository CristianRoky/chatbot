import streamlit as st
from streamlit_option_menu import option_menu
from src.pages.chatbot import chatbot
from src.pages.map import map

def main():
    with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Chatbot", "Map"],
                icons=["robot", "geo-alt"],
                menu_icon="cast",
                default_index=0
            )

    if selected == "Chatbot":
        chatbot()
    elif selected == "Map":
        map()

if __name__ == "__main__":
    main()