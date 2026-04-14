import pytest, psycopg2

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("query , params, authorized" , [
    ("SELECT * FROM actor", None, True),
    ("INSERT INTO actor(first_name, last_name) VALUES(%s, %s)", ("JOHN", "DOE"), False),
    ("UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s", ("JANE", "DONNA", 7), False),
    ("DELETE FROM actor WHERE actor_id = %s", (7,), False)
])
def test_db_read_only_user_permissions(db_readonly_connection, query, params, authorized):
    cur = db_readonly_connection.cursor()
    if authorized == False:
        with pytest.raises(psycopg2.errors.InsufficientPrivilege):
            cur.execute(query, params)
        db_readonly_connection.rollback()
    else:
        cur.execute(query, params)
        rows = cur.fetchall()
        assert rows is not None, f"Query{query} is not supposed to be unauthorized"

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("query , params" , [
    ("SELECT * FROM actor", None),
    ("INSERT INTO actor(first_name, last_name) VALUES(%s, %s)", ("JOHN", "DOE")),
    ("UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s", ("JANE", "DONNA", 7)),
    ("DELETE FROM actor WHERE actor_id = %s", (7,))
])
def test_db_unpriviliged_user_permissions(db_unpriviliged_connection, query, params):
    cur = db_unpriviliged_connection.cursor()
    with pytest.raises(psycopg2.errors.InsufficientPrivilege):
            cur.execute(query, params)
    db_unpriviliged_connection.rollback()
    
