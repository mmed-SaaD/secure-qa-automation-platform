# 1 — Connection & Setup  => Checked

Connect to the database successfully
Verify connection closes properly
Verify connection fails with wrong credentials
Verify connection fails with wrong host/port

# 2 — CRUD Operations => Checked

Insert a record and verify it was saved
Read a record by ID
Update a record and verify changes persisted
Delete a record and verify it's gone
Verify deleted record is not retrievable

# 3 — Data Integrity => Checked

Verify primary key uniqueness
Verify foreign key constraints are enforced
Verify NOT NULL constraints are enforced
Verify UNIQUE constraints are enforced
Verify default values are applied correctly

# 4 — Query Validation => Checked

Verify SELECT returns correct data
Verify WHERE clause filters correctly
Verify ORDER BY sorts correctly
Verify LIMIT and OFFSET work correctly
Verify JOIN returns correct combined data
Verify aggregate functions (COUNT, SUM, AVG, MAX, MIN)

# 5 — Schema Validation => Checked

Verify table exists
Verify column names are correct
Verify column types are correct
Verify indexes exist where expected

# 6 — Transactions => Checked

Verify COMMIT persists data
Verify ROLLBACK undoes changes
Verify transaction isolation works correctly

# 7 — Performance => Checked

Verify query executes within acceptable time
Verify indexes improve query speed
Verify no N+1 query issues

# 8 — Security

Verify SQL injection is handled
Verify user permissions are enforced
Verify sensitive data is not exposed

# 9 — Boundary & Negative => Checked

Insert record with missing required fields
Insert record with wrong data types
Query non-existing record returns correct response
Insert duplicate primary key returns correct error