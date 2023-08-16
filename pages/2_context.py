import configparser
from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
import pandas as pd
import streamlit as st
st.title('User Management')
def role_selection(_session):
    role_df = _session.sql('show roles;').collect()
    role_df = pd.DataFrame(role_df)
    role_list = role_df['name']
    role_select = st.sidebar.selectbox('Select a Role', role_list)
    if st.sidebar.button('Use Role'):
        set_role = _session.sql(f'''USE ROLE {role_select} ;''').collect()
        return set_role

def warehouse_selection(_session):
    warehouse_df = _session.sql('show warehouses;').collect()
    warehouse_df = pd.DataFrame(warehouse_df)
    warehouse_df
    warehouse_list = warehouse_df['name']
    warehouse_select = st.sidebar.selectbox('Select a Role', warehouse_list)
    if st.sidebar.button('Use Warehouse'):
        set_warehouse = _session.sql(f'''USE WAREHOUSE {warehouse_select} ;''').collect()
try:
    session = st.session_state['Session']
    set_role = role_selection(session)
    if set_role != '':
        warehouse_selection(session)
    
    current_role = session.sql('select current_role();').collect()
    current_role
    current_warehouse = session.sql('select current_warehouse();').collect()
    current_warehouse

