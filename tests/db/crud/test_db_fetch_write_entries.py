import pytest, psycopg2

@pytest.mark.db
@pytest.mark.smoke
def test_db_insert_verify_record(db_connection, db_cursor):
    conn = db_connection
    cur = db_cursor
    cur.execute("INSERT INTO actor(first_name, last_name) values (%s, %s)", ("ENZO" , "DADAS"))
    conn.commit()
    cur.execute("SELECT * FROM actor WHERE first_name = %s and last_name = %s", ("ENZO" , "DADAS"))
    row = cur.fetchone()
    assert row is not None

@pytest.mark.db
@pytest.mark.smoke
def test_db_fetch_record_by_id(db_connection, db_cursor, actorID : int = 107):
    cur = db_cursor
    cur.execute("SELECT * FROM actor WHERE actor_id = %s" , (actorID,))
    row = cur.fetchone()
    assert row is not None , f"No entry in the DB matches an actor with the id {actorID}"

@pytest.mark.db
@pytest.mark.smoke
def test_db_update_record(db_connection, db_cursor, actorID : int = 116):
    conn = db_connection
    cur = db_cursor
    cur.execute("SELECT * FROM actor WHERE actor_id = %s" , [actorID])
    row = cur.fetchone()
    cur.execute("UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s", ("John" , "MARSTON" , actorID))
    conn.commit()
    cur.execute("SELECT * FROM actor WHERE actor_id = %s" , [actorID])
    row = cur.fetchone()
    assert row[1] == "John" , f"Expected the actor's first_name to be JOHN, got {row[1]} instead"
    assert row[2] == "MARSTON" , f"Expected the actor's last_name to be MARSTON, got {row[2]} instead"

@pytest.mark.db
@pytest.mark.smoke
def test_db_delete_record(db_connection, db_cursor, actorID : int = 8):
    conn = db_connection
    cur = db_cursor
    cur.execute("DELETE FROM film_actor WHERE actor_id = %s", (actorID,))
    cur.execute("DELETE FROM actor WHERE actor_id = %s", (actorID,))
    conn.commit()

    cur.execute("SELECT * FROM actor WHERE actor_id = %s", (actorID,))
    assert cur.fetchone() is None , "This record is supposed to be deleted but it is still available"


    