import streamlit as st
def wh_list(session):
    warehouse_list_df = session.sql("show warehouses ;").collect()
    warehouse_list_df =  pd.DataFrame(warehouse_list_df)
    warehouse_list_df = warehouse_list_df["name"]
    return warehouse_list_df


def data_selector():
    session = st.session_state['Session']
    warehouse = wh_list(session)
    wh_select = st.selectbox('Choose warehouse',(warehouse))
    tables = tables_list(wh_select, session)
    if list(tables) != []:
        table_select = st.selectbox('Choose table',(tables))
        return session, db_select,table_select

