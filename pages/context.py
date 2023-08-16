import streamlit as st

# Initialize session-level variables
selected_role = st.session_state.selected_role if 'selected_role' in st.session_state else '<default_role>'
selected_warehouse = st.session_state.selected_warehouse if 'selected_warehouse' in st.session_state else '<default_warehouse>'
