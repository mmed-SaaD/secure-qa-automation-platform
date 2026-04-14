import pytest
from core.utils.db.check_sensitive_data_is_not_exposed import check_sensitive_data_is_not_exposed

@pytest.mark.db
@pytest.mark.smoke
def test_sensitive_data_exposure(db_cursor, create_users_table):
    cur = db_cursor
    check_sensitive_data_is_not_exposed(cur)
