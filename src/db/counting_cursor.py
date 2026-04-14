class CountingCursor:
    def __init__(self, real_cursor):
        self.real_cursor = real_cursor
        self.query_count = 0
        self.queries = []

    def execute(self, query, params = None):
        self.query_count += 1
        self.queries.append((query, params))
        return self.real_cursor.execute(query, params)

    def executemany(self, query, list_params):
        self.query_count += 1
        self.queries.append((query, list_params))
        return self.real_cursor.executemany(query, list_params)

    def fetchall(self):
        return self.real_cursor.fetchall()
    
    def fetchone(self):
        return self.real_cursor.fetchone()
    
    def close(self):
        return self.real_cursor.close()