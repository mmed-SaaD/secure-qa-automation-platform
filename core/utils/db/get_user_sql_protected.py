def get_user_sql_protected(db_cursor, table_name, params):
    cur = db_cursor
    cur.execute(f"SELECT * FROM {table_name} WHERE username = %s and password = %s", (params["username"], params["password"]))
    results = cur.fetchall()
    return results