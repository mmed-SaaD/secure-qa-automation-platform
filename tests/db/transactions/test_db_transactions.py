import pytest, psycopg2, os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.db
@pytest.mark.smoke
def test_db_commit(db_connection, db_cursor):
    conn = db_connection
    cur = db_cursor
    cur.execute("INSERT INTO actor(first_name, last_name) VALUES(%s, %s)" , ("COMMIT_USER_FIRSTNAME" , "COMMIT_USER_LASTNAME"))
    conn.commit()
    cur.execute("SELECT * FROM actor WHERE first_name = %s and last_name = %s", ("COMMIT_USER_FIRSTNAME" , "COMMIT_USER_LASTNAME"))
    row = cur.fetchone()
    assert row is not None, "Inserted record has not been commited !"
    assert row[1] == "COMMIT_USER_FIRSTNAME" , f"Expected record first_name to be COMMIT_USER_FIRSTNAME, got {row[1]} instead"
    assert row[2] == "COMMIT_USER_LASTNAME", f"Expected record first_name to be COMMIT_USER_LASTNAME, got {row[2]} instead"

    cur.execute("DELETE FROM actor WHERE first_name = %s and last_name = %s", ("COMMIT_USER_FIRSTNAME", "COMMIT_USER_LASTNAME"))
    conn.commit()

@pytest.mark.db
@pytest.mark.smoke
def test_db_rollback(db_connection, db_cursor):
    conn = db_connection
    cur = db_cursor
    cur.execute("INSERT INTO actor(first_name, last_name) VALUES(%s, %s)" , ("COMMIT_USER_FIRSTNAME" , "COMMIT_USER_LASTNAME"))
    conn.rollback()
    cur.execute("SELECT * FROM actor WHERE first_name = %s and last_name = %s", ("COMMIT_USER_FIRSTNAME" , "COMMIT_USER_LASTNAME"))
    row = cur.fetchone()
    assert row is None, "Inserted record must not be commited !"

@pytest.mark.db
@pytest.mark.smoke
def test_db_isolated_transactions(db_connection, db_cursor):
    conn1 = db_connection
    conn2 = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )  

    cur1 = conn1.cursor()
    cur2 = conn2.cursor()

    cur1.execute("UPDATE actor SET first_name = %s WHERE actor_id = %s", ("GHOST", 1))

    cur2.execute("SELECT first_name FROM actor WHERE actor_id = %s" , (1,))
    row = cur2.fetchone()

    assert row[0] != "GHOST", "Chnages have not been commited yet ! value must not yet be changed"

    conn1.rollback()
    conn2.close()

