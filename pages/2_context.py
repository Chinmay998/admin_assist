# Query for roles
role_query = "SHOW ROLES"
roles_result = conn.cursor().execute(role_query).fetchall()
available_roles = [role[1] for role in roles_result]

# Query for warehouses
warehouse_query = "SHOW WAREHOUSES"
warehouses_result = conn.cursor().execute(warehouse_query).fetchall()
available_warehouses = [warehouse[0] for warehouse in warehouses_result]
selected_role = st.selectbox('Select Role', available_roles)
selected_warehouse = st.selectbox('Select Warehouse', available_warehouses)
conn.cursor().execute(f'USE ROLE {selected_role}')
conn.cursor().execute(f'USE WAREHOUSE {selected_warehouse}')

