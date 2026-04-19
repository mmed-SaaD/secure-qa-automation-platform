import pytest, psycopg2
from core.utils.db.get_user_sql_unprotected import get_user_sql_unprotected
from core.utils.db.get_user_sql_protected import get_user_sql_protected

@pytest.mark.db
@pytest.mark.smoke
def test_db_sql_injection(db_cursor, create_users_table):
    table_name = create_users_table
    params = {
        "username" : "' OR 1=1--'",
        "password" : "password_7"
    }
    results = get_user_sql_unprotected(db_cursor, table_name, params)
    assert results is not None , "Returned results from the function get_user_sql_unprotected are not supposed to be empty"
    results = get_user_sql_protected(db_cursor, table_name, params)
    assert results == [], "Returned results from the function get_user_sql_protected are supposed to be empty"