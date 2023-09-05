import streamlit as st

apps = {
    "App 1": "URL_TO_APP_1_RAW",
    "App 2": "URL_TO_APP_2_RAW",
    "App 3": "URL_TO_APP_3_RAW",
    "App 4": "URL_TO_APP_4_RAW",
    "App 5": "URL_TO_APP_5_RAW",
}

selected_app = st.selectbox("Select an Application", list(apps.keys()))
selected_app_url = apps[selected_app]
