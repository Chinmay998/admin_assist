# import configparser
# from snowflake.snowpark import Session
# from snowflake.snowpark.functions import *
# import pandas as pd
# import streamlit as st
# st.title('User Management')
# def role_selection(_session):
#     role_df = _session.sql('show roles;').collect()
#     st.write(role_df)
#     role_df = pd.DataFrame(role_df)
#     role_list = role_df['name']
#     st.write('role_list')
#     role_select = st.sidebar.selectbox('Select a Role', role_list)
#     if st.sidebar.button('Use Role'):
#         set_role = _session.sql(f'''USE ROLE {role_select} ;''').collect()
#         return set_role

# def warehouse_selection(_session):
#     warehouse_df = _session.sql('show warehouses;').collect()
#     warehouse_df = pd.DataFrame(warehouse_df)
#     warehouse_df
#     warehouse_list = warehouse_df['name']
#     warehouse_select = st.sidebar.selectbox('Select a Role', warehouse_list)
#     if st.sidebar.button('Use Warehouse'):
#         set_warehouse = _session.sql(f'''USE WAREHOUSE {warehouse_select} ;''').collect()

import configparser
from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
import pandas as pd
import streamlit as st

# ... (other imports and code)

def role_selection():
    session = st.session_state['session']  # Retrieve the session from session_state
    role_df = session.sql('show roles;').collect()
    role_df = pd.DataFrame(role_df)
    role_list = role_df['name']
    st.write(role_list)  # Display the role list
    role_select = st.sidebar.selectbox('Select a Role', role_list)
    if st.sidebar.button('Use Role'):
        set_role = session.sql(f'''USE ROLE {role_select};''').collect()
        return set_role

def warehouse_selection():
    session = st.session_state['session']  # Retrieve the session from session_state
    warehouse_df = session.sql('show warehouses;').collect()
    warehouse_df = pd.DataFrame(warehouse_df)
    st.write(warehouse_df)  # Display the warehouse DataFrame
    warehouse_list = warehouse_df['name']
    warehouse_select = st.sidebar.selectbox('Select a Warehouse', warehouse_list)
    if st.sidebar.button('Use Warehouse'):
        set_warehouse = session.sql(f'''USE WAREHOUSE {warehouse_select};''').collect()
        return set_warehouse

# Call the functions to display the content
if __name__ == "__main__":
    role_selection()
    warehouse_selection()



