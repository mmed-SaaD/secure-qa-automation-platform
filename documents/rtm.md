# Requirements Traceability Matrix (RTM)

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Requirements Traceability Matrix

---

## 1. Purpose

This RTM maps each derived requirement to its test scenarios and primary automation source.

---

## 2. Traceability Matrix

| Requirement ID | Requirement | Scenario IDs | Test Layer | Primary Automation Source | Coverage |
|---|---|---|---|---|---|
| FR-API-001 | API Availability | TS-API-001 | API | `tests/api/connectivity/test_api_reachable.py` | Covered |
| FR-API-002 | Authentication | TS-API-002, TS-API-003 | API | `tests/api/auth/test_user_login.py` | Covered |
| FR-API-003 | Protected Resource Access | TS-API-004, TS-API-005 | API | `tests/api/auth/test_user_login.py` | Covered |
| FR-API-004 | Product Catalogue | TS-API-006 | API | `tests/api/products/test_api_products.py` | Covered |
| FR-API-005 | User Retrieval | TS-API-007 | API | `tests/api/users/test_api_users.py` | Covered |
| FR-API-006 | Cart Retrieval and Calculation | TS-API-008 | API | `tests/api/carts/test_api_cart.py` | Covered |
| FR-API-007 | Recipe Retrieval | TS-API-009 | API | `tests/api/recipes/test_api_fetch_recipes.py` | Covered |
| FR-API-008 | Recipe Creation and Update | TS-API-010 | API | `tests/api/recipes/test_api_write_recipes.py` | Covered |
| FR-API-009 | Recipe Deletion | TS-API-011 | API | `tests/api/recipes/test_api_delete_recipes.py` | Covered |
| FR-API-010 | API Contract Validation | TS-API-012 | API | `tests/api/response/test_api_response_schema.py` | Covered |
| FR-UI-001 | User Login and Logout | TS-UI-001 | UI | `tests/ui/test_loginpage.py` | Covered |
| FR-UI-002 | Login Validation | TS-UI-002, TS-UI-003, TS-UI-004, TS-UI-005 | UI | `tests/ui/test_loginpage.py` | Covered |
| FR-UI-003 | Inventory Validation | TS-UI-006 | UI | `tests/ui/test_inventorypage.py` | Covered |
| FR-UI-004 | Product Sorting | TS-UI-007 | UI | `tests/ui/test_inventorypage.py` | Covered |
| FR-UI-005 | Cart Management | TS-UI-008, TS-UI-009 | UI | `tests/ui/test_inventorypage.py`, `tests/ui/test_cartpage.py` | Covered |
| FR-UI-006 | Access Control and Session Isolation | TS-UI-010, TS-UI-011 | UI | `tests/ui/test_inventorypage.py` | Covered |
| FR-UI-007 | Checkout Validation | TS-UI-012 | UI | `tests/ui/test_checkoutpage.py` | Covered |
| FR-UI-008 | Successful Checkout | TS-UI-013 | UI | `tests/ui/test_checkoutpage.py` | Covered |
| FR-UI-009 | Navigation | TS-UI-014 | UI | `tests/ui/test_navigation.py` | Covered |
| FR-UI-010 | Application State Reset | TS-UI-015 | UI | `tests/ui/test_navigation.py` | Covered |
| FR-DB-001 | Database Connectivity | TS-DB-001 | Database | `tests/db/connection/test_db_connection.py` | Covered |
| FR-DB-002 | Schema Validation | TS-DB-002 | Database | `tests/db/schema/test_db_schema_validation.py` | Covered |
| FR-DB-003 | Query Validation | TS-DB-003 | Database | `tests/db/crud/test_db_query_validation.py` | Covered |
| FR-DB-004 | CRUD Operations | TS-DB-004 | Database | `tests/db/crud/test_db_fetch_write_entries.py` | Covered |
| FR-DB-005 | Data Integrity | TS-DB-005 | Database | `tests/db/crud/test_db_data_integrity.py` | Covered |
| FR-DB-006 | Transaction Behaviour | TS-DB-006 | Database | `tests/db/transactions/test_db_transactions.py` | Covered |
| FR-DB-007 | Database Permissions | TS-DB-007 | Database | `tests/db/security/test_db_permissions.py` | Covered |
| FR-DB-008 | Sensitive Data Protection | TS-DB-008 | Database | `tests/db/security/test_db_security.py` | Covered |
| NFR-PERF-001 | Response and Query Time | TS-DB-009, TS-PERF-001, TS-PERF-002, TS-PERF-003 | Database / Performance | DB performance tests and k6 scripts | Covered |
| NFR-PERF-002 | Error Rate | TS-PERF-004 | Performance | k6 scripts | Covered |
| NFR-PERF-003 | Stress Behaviour | TS-PERF-006 | Performance | k6 stress scenarios | Covered |
| NFR-PERF-004 | Authenticated Workflow Performance | TS-PERF-005 | Performance | k6 authenticated workflow | Covered |
| NFR-PERF-005 | UI Journey Timing | TS-PERF-007 | UI Performance | UI performance tests | Covered |
| NFR-SEC-001 | Injection Resistance | TS-SEC-001 | Security | OWASP Juice Shop security tests | Covered |
| NFR-SEC-002 | Broken Access Control | TS-SEC-002 | Security | OWASP Juice Shop security tests | Covered |
| NFR-SEC-003 | Cross-Site Scripting | TS-SEC-003 | Security | OWASP Juice Shop security tests | Covered |
| NFR-SEC-004 | Security Configuration | TS-SEC-004 | Security | Security configuration tests | Covered |
| NFR-SEC-005 | Automated Vulnerability Scanning | TS-SEC-005, TS-SEC-006 | Security | OWASP ZAP and manual validation | Covered |
| NFR-REP-001 | Reporting | N/A | Reporting | Allure and GitHub Pages | Covered |
| NFR-CI-001 | Continuous Integration | N/A | CI/CD | GitHub Actions | Covered |
| NFR-CI-002 | Secure Configuration | N/A | CI/CD | GitHub Secrets and environment variables | Covered |

---

## 3. Coverage Summary

| Category | Requirements | Covered | Coverage |
|---|---:|---:|---:|
| API Functional | 10 | 10 | 100% |
| UI Functional | 10 | 10 | 100% |
| Database Functional | 8 | 8 | 100% |
| Performance | 5 | 5 | 100% |
| Security | 5 | 5 | 100% |
| Reporting and CI/CD | 3 | 3 | 100% |
| **Overall** | **41** | **41** | **100%** |

---

## 4. Limitations

This RTM proves traceability to repository modules and scenarios. It does not claim that the requirements came from an original business specification.

The exact number of executable tests should be taken from the current pytest collection or Allure report because the README describes the suite as `180+` tests rather than providing a fixed inventory.
