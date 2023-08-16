def wh_list(session):
    warehouse_list_df = session.sql("show warehouses ;").collect()
    warehouse_list_df =  pd.DataFrame(warehouse_list_df)
    warehouse_list_df = warehouse_list_df["name"]
    return warehouse_list_df

