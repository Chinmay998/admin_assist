import streamlit as st

apps = {
    "App 1": "https://github.com/Chinmay998/admin_assist/raw/main/pages/2_Context.py",
    "App 2": "https://raw.githubusercontent.com/Chinmay998/admin_assist/main/pages/4_Over_Under_Size_File_Identifier.py",
    "App 3": "https://raw.githubusercontent.com/Chinmay998/admin_assist/main/pages/3_File_Upload_Utility.py",
    "App 4": "URL_TO_APP_4_RAW",
    "App 5": "URL_TO_APP_5_RAW",
}

selected_app = st.selectbox("Select an Application", list(apps.keys()))
selected_app_url = apps[selected_app]
