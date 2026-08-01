# Secure QA Automation Platform - Database Test Cases

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Cases

---

## Purpose

This document maps implemented test coverage to requirement IDs, scenario IDs, pytest markers, and repository sources.

Database cases are mapped to the repository's concrete validation modules. The exact executable count may be higher because each module can contain several pytest functions and parametrized executions.

---

## Test Cases

| Test Case ID | Scenario ID | Requirement ID | Test Case | Priority | Markers / Tags | Execution Model | Automation Source | Status |
|---|---|---|---|---|---|---|---|---|
| `TC-DB-001` | `TS-DB-001` | `FR-DB-001` | PostgreSQL Pagila connection is established | Critical | `db` | Test definitions maintained in module | `tests/db/connection/test_db_connection.py` | Automated |
| `TC-DB-002` | `TS-DB-002` | `FR-DB-002` | Database schema, tables, columns, and relationships are validated | High | `db` | Test definitions maintained in module | `tests/db/schema/test_db_schema_validation.py` | Automated |
| `TC-DB-003` | `TS-DB-003` | `FR-DB-003` | Database query results are validated | High | `db` | Test definitions maintained in module | `tests/db/crud/test_db_query_validation.py` | Automated |
| `TC-DB-004` | `TS-DB-004` | `FR-DB-004` | Database records can be fetched and written | High | `db` | Test definitions maintained in module | `tests/db/crud/test_db_fetch_write_entries.py` | Automated |
| `TC-DB-005` | `TS-DB-005` | `FR-DB-005` | Database data integrity is preserved | Critical | `db` | Test definitions maintained in module | `tests/db/crud/test_db_data_integrity.py` | Automated |
| `TC-DB-006` | `TS-DB-006` | `FR-DB-006` | Transactions commit and roll back correctly | High | `db` | Test definitions maintained in module | `tests/db/transactions/test_db_transactions.py` | Automated |
| `TC-DB-007` | `TS-DB-007` | `FR-DB-007` | Database permissions prevent unauthorized operations | Critical | `db, security` | Test definitions maintained in module | `tests/db/security/test_db_permissions.py` | Automated |
| `TC-DB-008` | `TS-DB-008` | `FR-DB-008` | Sensitive database data is not exposed | Critical | `db, security` | Test definitions maintained in module | `tests/db/security/test_db_security.py` | Automated |
| `TC-DB-009` | `TS-DB-009` | `NFR-PERF-001` | Database query performance meets configured expectations | Medium | `db, performance` | Test definitions maintained in module | `tests/db/performance/test_db_performance.py` | Automated |
| `TC-DB-010` | `TS-DB-003` | `FR-DB-003` | Invalid CRUD operations return controlled database errors | High | `db, negative` | Test definitions maintained in module | `tests/db/negative_crud/test_db_negative_crud.py` | Automated |

---

## Traceability Rule

- Requirement IDs originate from `requirements-analysis.md`.
- Scenario IDs originate from `test-scenarios.md`.
- Concrete pytest node IDs use the format `path::test_function`.
- Parametrized tests identify their execution count where confirmed.
- Expected failures marked with `xfail` document known target limitations and are not treated as ordinary passed tests.
