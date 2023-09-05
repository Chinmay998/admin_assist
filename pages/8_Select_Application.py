import streamlit as st
from st.components.v1 import iframe

apps = {
    "App 1": "https://github.com/Chinmay998/admin_assist/raw/main/pages/2_Context.py",
    "App 2": "https://raw.githubusercontent.com/Chinmay998/admin_assist/main/pages/4_Over_Under_Size_File_Identifier.py",
    "App 3": "https://raw.githubusercontent.com/Chinmay998/admin_assist/main/pages/3_File_Upload_Utility.py",
    "App 4": "https://raw.githubusercontent.com/Chinmay998/admin_assist/main/pages/5_User_Management.py",
    "App 5": "https://raw.githubusercontent.com/Chinmay998/admin_assist/main/pages/6_Log_Out.py",
}

selected_app = st.selectbox("Select an Application", list(apps.keys()))
selected_app_url = apps[selected_app]

st.write(f"Displaying {selected_app}")
st.iframe(selected_app_url, width=800, height=600)
