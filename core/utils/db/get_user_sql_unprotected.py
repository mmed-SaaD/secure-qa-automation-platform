def get_user_sql_unprotected(db_cursor, table_name, params):
    cur = db_cursor
    cur.execute(f"SELECT * FROM {table_name} WHERE username = '{params['username']}' and password = '{params['password']}'")
    results = cur.fetchall()
    return results