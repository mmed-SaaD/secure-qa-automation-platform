import pytest, psycopg2

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("query, params", [
    ("INSERT INTO actor(actor_id, first_name, last_name) VALUES (%s, %s, %s)", (1, "JOHN", "DOE")),
    ("INSERT INTO film(film_id, title, language_id) VALUES (%s, %s, %s)", (1, "RUSH HOUR", 2)),
    ("INSERT INTO city(city_id, city, country_id) VALUES (%s, %s, %s)", (1, "WASHINGTON", 4))
])
def test_db_duplicated_pkey(db_cursor, query, params):
    cur = db_cursor
    with pytest.raises(psycopg2.errors.UniqueViolation):
        cur.execute(query, params)

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("query, params", [
    ("INSERT INTO film(film_id, title) VALUES (%s, %s)", (1, "RUSH HOUR")),
    ("INSERT INTO city(city_id, city) VALUES (%s, %s)", (1, "WASHINGTON"))
])
def test_db_missing_required_fields(db_cursor, query, params):
    '''
    MISSING REQUIRED FIELDS ARE :
    film => language_id
    city => country_id
    '''
    cur = db_cursor
    with pytest.raises(psycopg2.errors.NotNullViolation):
        cur.execute(query, params)

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("query, params", [
    ("INSERT INTO film(film_id, title) VALUES (%s, %s)", ("str as id", "RUSH HOUR")),
    ("INSERT INTO city(city_id, city) VALUES (%s, %s)", ("str as id", "WASHINGTON"))
])
def test_db_wrong_data_type(db_cursor, query, params):
    cur = db_cursor
    with pytest.raises(psycopg2.errors.InvalidTextRepresentation ):
        cur.execute(query, params)

@pytest.mark.db
@pytest.mark.smoke
def test_db_missing_record(db_cursor):
    cur = db_cursor
    cur.execute("SELECT * FROM actor WHERE actor_id = %s", (9999999,))
    results = cur.fetchone()
    assert results is None, "The fetched record do not exist, and yet it was fetched"
    