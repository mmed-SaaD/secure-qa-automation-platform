import pytest, psycopg2

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("table_name", [
    "actor",
    "address",
    "category",
    "city",
    "country",
    "film"
])
def test_db_schema_table_exists(db_cursor, table_name):
    cur = db_cursor
    cur.execute("""
        SELECT EXISTS (
        SELECT 1 FROM information_schema.tables 
        WHERE table_name = %s
    );
    """, (table_name,))
    exists = cur.fetchone()[0]
    assert exists, f"Table {table_name} does not exist"

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("table_name , column_name", [
    ("actor" , ["actor_id", "first_name" , "last_name"]),
    ("address" , ["address", "address", "address2", "district"]),
    ("category" , ["category_id", "name", "last_update"]),
    ("city" , ["city_id", "city", "country_id", "last_update"]),
    ("country", ["country_id", "country", "last_update"]),
    ("film" , ["film_id" , "title", "description"])
]
)
def test_db_column_exists(db_cursor, table_name, column_name):
    cur = db_cursor
    cur.execute("""
            SELECT column_name FROM information_schema.columns
            WHERE table_name = %s AND column_name = ANY(%s)
    """, (table_name, column_name))
    found = [row[0] for row in cur.fetchall()]
    for column in column_name:
        assert column in found, f"Column '{column_name}' does not exist in table '{table_name}'"

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("table_name, column_expected_type", [
    ("actor" , {"actor_id" : "integer", "first_name" : "text", "last_name" : "text"}),
    ("address" , {"address_id" : "integer", "address" : "text", "address2" : "text", "district" : "text"}),
    ("category" , {"category_id" : "integer", "name" : "text"}),
    ("city" , {"city_id" : "integer", "country_id" : "integer", "city" : "text",}),
    ("country" , {"country_id" : "integer", "country" : "text"}),
    ("film" , {"film_id" : "integer", "release_year" : "integer", "title" : "text", "description" : "text"})
])
def test(db_cursor, table_name, column_expected_type):
    cur = db_cursor
    cur.execute("""
            SELECT column_name, data_type FROM information_schema.columns
            WHERE table_name = %s AND column_name = ANY(%s)
    """, (table_name, list(column_expected_type.keys())))
    rows = cur.fetchall()
    found = {row[0]: row[1] for row in rows}
    for column_name, expected_type in column_expected_type.items():
        assert column_name in found, f"Column {column_name} was not found"
        assert found[column_name] == expected_type, f"Expected {column_name} to be {expected_type}, got {found[column_name]} instead"

@pytest.mark.db
@pytest.mark.smoke
@pytest.mark.parametrize("table_name , index_name" , [
    ("actor" , "actor_pkey"),
    ("address", "address_pkey"),
    ("category", "category_pkey"),
    ("city", "city_pkey"),
    ("category", "category_pkey"),
    ("film", "film_pkey")
])
def test_db_indexes_exist(db_cursor, table_name, index_name):
    cur = db_cursor
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM pg_indexes WHERE tablename = %s AND indexname = %s
        )
    """, (table_name, index_name))
    exists = cur.fetchone()[0]
    assert exists, f"Missing index {index_name} for the table {table_name}"