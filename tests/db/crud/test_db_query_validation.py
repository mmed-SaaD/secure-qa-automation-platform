import pytest, psycopg2

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("order_by" , [
    "DESC",
    "ASC"
])
def test_db_sort(db_cursor, order_by):
    ids = []
    cur = db_cursor
    cur.execute(f"SELECT * FROM actor ORDER BY actor_id {order_by}")
    rows = cur.fetchall()
    for row in rows:
        ids.append(row[0])
    if order_by == "DESC":
        assert all(ids[i] > ids[i + 1] for i in range(len(ids) - 1)) , "The list is supposed to be sorted (Option : DESC)"
    else:
        assert all(ids[i] < ids[i + 1] for i in range(len(ids) - 1)) , "The list is supposed to be sorted (Option : ASC)"

@pytest.mark.db
@pytest.mark.smoke
def test_db_where(db_cursor):
    cur = db_cursor
    cur.execute("SELECT * FROM actor WHERE actor_id = %s", (5,))
    actor_id = cur.fetchone()
    assert actor_id is not None, "No record returned !"
    assert actor_id[0] == 5, f"Expected actor_id to be 5, got {actor_id[0]} instead"

@pytest.mark.db
@pytest.mark.smoke
def test_db_limit(db_cursor):
    cur = db_cursor
    cur.execute("SELECT * FROM actor LIMIT 10")
    rows = cur.fetchall()
    assert len(rows) == 10, f"The query must return 10 records, it returned {len(rows)} instead"

@pytest.mark.db
@pytest.mark.smoke
def test_db_offset(db_cursor):
    cur = db_cursor
    cur.execute("SELECT * FROM actor ORDER BY actor_id ASC")
    full_sample = cur.fetchmany(37)
    cur.execute("SELECT * FROM actor ORDER BY actor_id ASC LIMIT 17")
    first_half = cur.fetchall()
    cur.execute("SELECT * FROM actor ORDER BY actor_id ASC LIMIT 20 OFFSET 17")
    second_half = cur.fetchall()
    assert first_half + second_half == full_sample, "Recovered records are different from what is expected"

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("query" , [
    "SELECT film.title, actor.first_name, actor.last_name FROM film INNER JOIN film_actor on film_actor.film_id = film.film_id INNER JOIN actor on film_actor.actor_id = actor.actor_id LIMIT 3",
    "SELECT * FROM actor LEFT JOIN film_actor ON film_actor.actor_id = actor.actor_id LIMIT 3",
    "SELECT * FROM actor RIGHT JOIN film_actor ON film_actor.actor_id = actor.actor_id LIMIT 3",

])
def test_db_join(db_cursor, query):
    cur = db_cursor
    cur.execute(query)
    rows = cur.fetchall()
    assert rows is not None, "No records were returned"

@pytest.mark.db
@pytest.mark.smoke
def test_db_count(db_cursor):
    cur = db_cursor
    cur.execute("SELECT * FROM actor")
    rows = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM actor")
    count = cur.fetchone()
    assert len(rows) == count[0] , f"Expected the count to be{len(rows)} got {count[0]} instead"

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("option",[
    "MIN",
    "MAX",
    "SUM"
]
)
def test_db_min_max(db_cursor, option):
    cur = db_cursor
    ids = []
    cur.execute("SELECT actor_id FROM actor")
    rows = cur.fetchall()
    cur.execute(f"SELECT {option}(actor_id) FROM actor")
    actor_id = cur.fetchone()
    for row in rows:
        ids.append(row[0])
    match option.lower():
        case "min":
            assert min(ids) == actor_id[0], f"Expected min value to be {min(ids)} got {actor_id[0]} instead"
        case "max":
            assert max(ids) == actor_id[0], f"Expected max value to be {max(ids)} got {actor_id[0]} instead"
        case "sum":
            assert sum(ids) == actor_id[0], f"Expected sum value to be {sum(ids)} got {actor_id[0]} instead"
        case "avg":
            assert sum(ids) / len(ids) == actor_id[0], f"Expected avg value to be {sum(ids) / len(ids)} got {actor_id[0]} instead"
