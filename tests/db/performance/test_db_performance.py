import pytest, psycopg2, time
from core.utils.db.get_explain_plan import get_explain_plan
from core.utils.db.extract_node_types import extract_node_types
from core.utils.db.invalid_n1_case import get_actor_film_n1_issue
from core.utils.db.resolved_n1_case import get_actor_film_n1_resolved_issue
from src.db.counting_cursor import CountingCursor

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("query, threshold" , [
    ("SELECT * FROM actor", 1.0),
    ("SELECT film.title, actor.first_name, actor.last_name FROM film INNER JOIN film_actor on film_actor.film_id = film.film_id INNER JOIN actor on film_actor.actor_id = actor.actor_id LIMIT 3", 1.5),
    ("SELECT * FROM actor RIGHT JOIN film_actor ON film_actor.actor_id = actor.actor_id LIMIT 3", 1.5),
    ("SELECT * FROM film", 1.0)
])
def test_db_performance(db_cursor, query, threshold):
    cur = db_cursor
    
    plan = get_explain_plan(db_cursor, query)
    
    assert plan["Execution Time"] < threshold, f"Query : {query} exceeded expected execution time {threshold} to {plan["Execution Time"]:3f}"


@pytest.mark.db
@pytest.mark.smoke
def test_db_idx_execution_time_improvement(db_cursor, db_connection, get_perf_test_table):
    conn = db_connection
    cur = db_cursor
    table_name = get_perf_test_table
    email = "user2@gmail.com",
    query =  f"SELECT * FROM {table_name} WHERE email = %s"
    before_idx = get_explain_plan(db_cursor, query, (email,))
    before_node_types = extract_node_types(before_idx["Plan"])
    before_execution_time = before_idx["Execution Time"]

    cur.execute(
            f"CREATE INDEX idx_{table_name}_email ON {table_name}(email);"
        )
    cur.execute(f"ANALYZE {table_name};")

    after_idx = get_explain_plan(db_cursor, query, (email,))
    after_node_types = extract_node_types(after_idx["Plan"])
    after_execution_time = after_idx["Execution Time"]

    assert any(
        node_type in ("Index Scan", "Index Only Scan", "Bitmap Heap Scan", "Bitmap Index Scan")
        for node_type in after_node_types
    ), f"Expected indexed access, got: {after_node_types}"
    assert after_execution_time < before_execution_time, "Execution time before creating an index is supposed to be longer than after creating an index"

@pytest.mark.db
@pytest.mark.smoke
def test_test(db_cursor):
    cursor1 = CountingCursor(db_cursor)
    cursor2 = CountingCursor(db_cursor)
    get_actor_film_n1_issue(cursor1)
    get_actor_film_n1_resolved_issue(cursor2)
    assert cursor1.query_count > cursor2.query_count , f"cursor1 queries : {cursor1.query_count} - cursor2 queires {cursor2.query_count}"
    assert cursor2.query_count == 1, f"Expecting cursor2 queries to be 1 got {cursor2.query_count}"