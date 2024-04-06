"""Implements the TypeFlash app to test the speed of your typing"""
import streamlit as st
import time


def streamlit_typing_speed_test():
    """Contributes to the process of identifying the speed of your typed text"""
    
    st.set_page_config(
        page_title="Typing Speed Test",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    st.markdown("""
        Welcome to the Typing Speed Test! 🚀

        Here's how it works:

        1. Click on the **Start Typing** button when you're ready.
        2. Type in the provided text box.
        3. Click **Done Typing** once you finish.
        4. Get your words-per-minute (WPM) speed!
        """)

    st.title("🚀 Typing Speed Test")
    st.subheader("⚡ Find out how fast you can type!")
    st.write("---")

    if 'start_time' not in st.session_state:
        st.session_state.start_time = 0
    
    if 'end_time' not in st.session_state:
        st.session_state.end_time = 0

    if st.button('Start Typing '):
        st.session_state.start_time = time.time()

    user_input = st.text_area("Type the sentence:")

    if st.button('Done Typing'):
        st.session_state.end_time = time.time()
        if st.session_state.start_time:
            elapsed_time = st.session_state.end_time - st.session_state.start_time
            typing_speed = len(user_input.split()) / elapsed_time * 60
            st.balloons()
            st.write(f"Your typing speed is {typing_speed:.2f} words per minute.")
    st.write("---")
    st.markdown(
        """<div style="display: flex; justify-content: center; align-items: center; padding: 1rem;">
               Made with ❤️ by Anirudh
           </div>""",
        unsafe_allow_html=True
    )


streamlit_typing_speed_test()
