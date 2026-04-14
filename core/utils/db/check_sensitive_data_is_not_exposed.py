def check_sensitive_data_is_not_exposed(db_cursor):
    cur = db_cursor
    cur.execute("SELECT password FROM security_test_users")
    passwords = cur.fetchall()
    for password in passwords:
        assert password[0].startswith("$argon2id$"), "Warning : Passwords are stored in plaintext !!"
