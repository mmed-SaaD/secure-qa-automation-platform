# Test Scenarios

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Scenarios

---

## 1. API Test Scenarios

| Scenario ID | Requirement ID | Scenario | Priority | Automation Source |
|---|---|---|---|---|
| TS-API-001 | FR-API-001 | Verify core API availability | High | `tests/api/connectivity/test_api_reachable.py` |
| TS-API-002 | FR-API-002 | Verify login with valid credentials | Critical | `tests/api/auth/test_user_login.py` |
| TS-API-003 | FR-API-002 | Verify invalid authentication is rejected | High | `tests/api/auth/test_user_login.py` |
| TS-API-004 | FR-API-003 | Verify protected endpoint access with a valid token | Critical | `tests/api/auth/test_user_login.py` |
| TS-API-005 | FR-API-003 | Verify protected endpoint rejection without valid authorization | Critical | `tests/api/auth/test_user_login.py` |
| TS-API-006 | FR-API-004 | Verify product collection structure and metadata | High | `tests/api/products/test_api_products.py` |
| TS-API-007 | FR-API-005 | Verify user collection and individual-user retrieval | High | `tests/api/users/test_api_users.py` |
| TS-API-008 | FR-API-006 | Verify carts, products, totals, quantities, and discounts | High | `tests/api/carts/test_api_cart.py` |
| TS-API-009 | FR-API-007 | Verify recipe collection and individual-recipe retrieval | Medium | `tests/api/recipes/test_api_fetch_recipes.py` |
| TS-API-010 | FR-API-008 | Verify recipe creation and update behaviour | Medium | `tests/api/recipes/test_api_write_recipes.py` |
| TS-API-011 | FR-API-009 | Verify recipe deletion behaviour | Medium | `tests/api/recipes/test_api_delete_recipes.py` |
| TS-API-012 | FR-API-010 | Verify API response schema and required fields | High | `tests/api/response/test_api_response_schema.py` |

---

## 2. UI Test Scenarios

| Scenario ID | Requirement ID | Scenario | Priority | Automation Source |
|---|---|---|---|---|
| TS-UI-001 | FR-UI-001 | Verify valid SauceDemo login and logout | Critical | `tests/ui/test_loginpage.py` |
| TS-UI-002 | FR-UI-002 | Verify empty login validation | High | `tests/ui/test_loginpage.py` |
| TS-UI-003 | FR-UI-002 | Verify invalid username validation | High | `tests/ui/test_loginpage.py` |
| TS-UI-004 | FR-UI-002 | Verify invalid password validation | High | `tests/ui/test_loginpage.py` |
| TS-UI-005 | FR-UI-002 | Verify locked-user rejection | High | `tests/ui/test_loginpage.py` |
| TS-UI-006 | FR-UI-003 | Verify inventory and product details | High | `tests/ui/test_inventorypage.py` |
| TS-UI-007 | FR-UI-004 | Verify product sorting | Medium | `tests/ui/test_inventorypage.py` |
| TS-UI-008 | FR-UI-005 | Verify adding and removing products | High | `tests/ui/test_inventorypage.py` |
| TS-UI-009 | FR-UI-005 | Verify cart count and cart persistence | High | `tests/ui/test_cartpage.py`, `tests/ui/test_inventorypage.py` |
| TS-UI-010 | FR-UI-006 | Verify direct inventory access is blocked after logout | High | `tests/ui/test_inventorypage.py` |
| TS-UI-011 | FR-UI-006 | Verify new-tab and new-context session isolation | High | `tests/ui/test_inventorypage.py` |
| TS-UI-012 | FR-UI-007 | Verify checkout rejection with missing mandatory data | High | `tests/ui/test_checkoutpage.py` |
| TS-UI-013 | FR-UI-008 | Verify complete checkout happy path | Critical | `tests/ui/test_checkoutpage.py` |
| TS-UI-014 | FR-UI-009 | Verify Twitter, Facebook, LinkedIn, and About navigation | Medium | `tests/ui/test_navigation.py` |
| TS-UI-015 | FR-UI-010 | Verify application state reset | Medium | `tests/ui/test_navigation.py` |

---

## 3. Database Test Scenarios

| Scenario ID | Requirement ID | Scenario | Priority | Automation Source |
|---|---|---|---|---|
| TS-DB-001 | FR-DB-001 | Verify PostgreSQL database connectivity | Critical | `tests/db/connection/test_db_connection.py` |
| TS-DB-002 | FR-DB-002 | Verify required schema elements | High | `tests/db/schema/test_db_schema_validation.py` |
| TS-DB-003 | FR-DB-003 | Verify expected query results | High | `tests/db/crud/test_db_query_validation.py` |
| TS-DB-004 | FR-DB-004 | Verify record fetch and write operations | High | `tests/db/crud/test_db_fetch_write_entries.py` |
| TS-DB-005 | FR-DB-005 | Verify database data integrity | Critical | `tests/db/crud/test_db_data_integrity.py` |
| TS-DB-006 | FR-DB-006 | Verify transaction commit and rollback | High | `tests/db/transactions/test_db_transactions.py` |
| TS-DB-007 | FR-DB-007 | Verify database permissions | Critical | `tests/db/security/test_db_permissions.py` |
| TS-DB-008 | FR-DB-008 | Verify sensitive data is not exposed | Critical | `tests/db/security/test_db_security.py` |
| TS-DB-009 | NFR-PERF-001 | Verify database query performance | Medium | `tests/db/performance/test_db_performance.py` |

---

## 4. Performance Test Scenarios

| Scenario ID | Requirement ID | Scenario | Priority |
|---|---|---|---|
| TS-PERF-001 | NFR-PERF-001 | Measure all-products endpoint performance | High |
| TS-PERF-002 | NFR-PERF-001 | Measure single-product endpoint performance | High |
| TS-PERF-003 | NFR-PERF-001 | Measure filtered-product requests | Medium |
| TS-PERF-004 | NFR-PERF-002 | Measure product-creation error rate and latency | High |
| TS-PERF-005 | NFR-PERF-004 | Measure authenticated login and protected-resource workflow | High |
| TS-PERF-006 | NFR-PERF-003 | Identify degradation and failure point under stress | High |
| TS-PERF-007 | NFR-PERF-005 | Measure SauceDemo happy-path journey duration | Medium |

---

## 5. Security Test Scenarios

| Scenario ID | Requirement ID | Scenario | Priority |
|---|---|---|---|
| TS-SEC-001 | NFR-SEC-001 | Verify authentication bypass through injection | Critical |
| TS-SEC-002 | NFR-SEC-002 | Verify unauthorized access through ID manipulation | Critical |
| TS-SEC-003 | NFR-SEC-003 | Verify reflected XSS behaviour | High |
| TS-SEC-004 | NFR-SEC-004 | Verify security headers and configuration | High |
| TS-SEC-005 | NFR-SEC-005 | Execute OWASP ZAP scanning | High |
| TS-SEC-006 | NFR-SEC-005 | Manually validate scanner findings | High |
