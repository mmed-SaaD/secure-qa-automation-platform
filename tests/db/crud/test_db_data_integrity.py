import pytest, psycopg2

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("table , column" , [
    ("actor" , "actor_id"),
    ("city" , "city_id"),
    ("category" , "category_id"),
    ("country" , "country_id")
])
def test_db_pmkey_uniqueness(db_cursor, table, column):
    cur = db_cursor
    cur.execute(f"SELECT {column} FROM {table}")
    rows = cur.fetchall()
    assert len(rows) == len(set(rows)) , "Actors ids are supposed to be unique !"

@pytest.mark.db
def test_db_foreign_key_constraints(db_cursor):
    cur = db_cursor
    with pytest.raises(psycopg2.errors.ForeignKeyViolation):
        cur.execute("INSERT INTO film_actor(actor_id , film_id) VALUES(%s , %s)" , (17777777 , 99999999))

@pytest.mark.db
def test_db_not_null_constraints(db_cursor):
    cur = db_cursor
    with pytest.raises(psycopg2.errors.NotNullViolation ):
        cur.execute("INSERT INTO actor(first_name, last_name) values (%s, %s)" , (None, None))

@pytest.mark.db
def test_db_unique_constraints(db_cursor):
    cur = db_cursor
    with pytest.raises(psycopg2.errors.UniqueViolation):
        cur.execute("INSERT INTO actor(actor_id, first_name, last_name) values (%s, %s, %s)" , (1, "JOHN", "SMITTY"))

@pytest.mark.db
@pytest.mark.smoke
def test_db_default_values(db_connection, db_cursor):
    # We will be using both rental_duration and rental_rate from film table
    conn = db_connection
    cur = db_cursor
    cur.execute("INSERT INTO film(title, description, language_id, release_year) values (%s, %s, %s, %s)" , ("SAW IV", "Description goes here !", 2, "2011"))
    conn.commit()
    cur.execute("SELECT * FROM film WHERE title = %s and description = %s and release_year = %s" , ("SAW IV", "Description goes here !", "2011"))
    row = cur.fetchone()
    assert row[6] is not None, "The field [real_duration] is not supposed to be none"
    assert row[7] is not None, "The field [real_rate] is not supposed to be none" 

    cur.execute("DELETE FROM film WHERE title = %s", ("SAW IV",))
    conn.commit()