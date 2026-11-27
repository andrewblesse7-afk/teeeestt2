import streamlit as st

st.set_page_config(page_title="BugRadar AI", page_icon="🐞")


def show_code_analysis_page():
    st.header("Code Analysis")
    st.write("Upload a Python file to find potential bugs.")


def show_bug_analyzer_page():
    st.header("AI Bug Analyzer")
    st.write("Describe a bug to predict its severity.")


def show_bug_reports_page():
    st.header("Bug Reports")
    st.write("View and manage saved bugs.")


st.title("BugRadar AI")
st.write("Find, analyze and manage software bugs with the help of AI.")

page = st.sidebar.radio("Navigation", ["Code Analysis", "AI Bug Analyzer", "Bug Reports"])

if page == "Code Analysis":
    show_code_analysis_page()
elif page == "AI Bug Analyzer":
    show_bug_analyzer_page()
else:
    show_bug_reports_page()
