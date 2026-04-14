def get_explain_plan(db_cursor, query, params = None):
    cur = db_cursor
    cur.execute(f"""
        EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) 
    """ + query, params
    )
    result = cur.fetchone()[0]
    return result[0]