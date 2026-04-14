import pytest, psycopg2, os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.db
@pytest.mark.smoke
def test_db_connection_success(db_connection):
    assert db_connection.closed == 0, "DB Connection must be opened"

@pytest.mark.db
def test_db_connection_wrong_user_pass():
    with pytest.raises(psycopg2.OperationalError):
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            dbname = os.getenv("DB_NAME"),
            user = "random_username",
            password = "random_password"
        )
        assert conn.closed == 1, "With wrong credentials, DB Connection must not be successfull"

@pytest.mark.db
def test_db_connection_wrong_host_port():
    with pytest.raises(psycopg2.OperationalError):
        conn = psycopg2.connect(
            host = "Random host",
            port = 1700007,
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD")
        )
        assert conn.closed == 1, "With wrong credentials, DB Connection must not be successfull"



