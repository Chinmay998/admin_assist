import configparser
from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
import pandas as pd
import streamlit as st
# st.title('User Management')
# def role_selection(session):
#     role_df = session.sql('show roles;').collect()
#     role_df = pd.DataFrame(role_df)
#     role_list = role_df['name']
#     role_select = st.sidebar.selectbox('Select a Role', role_list)
#     if st.sidebar.button('Use Role'):
#         set_role = session.sql(f'''USE ROLE {role_select} ;''').collect()
#         st.session_state.selected_role = role_select
        

# def warehouse_selection(session):
#     warehouse_df = session.sql('show warehouses;').collect()
#     warehouse_df = pd.DataFrame(warehouse_df)
    
#     warehouse_list = warehouse_df['name']
#     warehouse_select = st.sidebar.selectbox('Select a Role', warehouse_list)
#     if st.sidebar.button('Use Warehouse'):
#         set_warehouse = session.sql(f'''USE WAREHOUSE {warehouse_select} ;''').collect()
#         st.session_state.selected_warehouse = warehouse_select

def warehouse_selection(session):
    warehouse_df = session.sql('show warehouses;').collect()
    warehouse_df = pd.DataFrame(warehouse_df)
    
    print("Warehouse DataFrame:")
    print(warehouse_df)
    
    warehouse_list = warehouse_df['name']  # Make sure 'name' is the correct column name
    print("Warehouse List:")
    print(warehouse_list)
    
    warehouse_select = st.sidebar.selectbox('Select a Warehouse', warehouse_list)
    if st.sidebar.button('Use Warehouse'):
        set_warehouse = session.sql(f'USE WAREHOUSE {warehouse_select};').collect()
        st.session_state.selected_warehouse = warehouse_select




if __name__ == "__main__":
    session = st.session_state['Session'] 
    # role_selection(session)
    warehouse_selection(session)



