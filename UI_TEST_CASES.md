# Secure QA Automation Platform - UI Test Cases

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Cases

---

## Purpose

This document maps implemented test coverage to requirement IDs, scenario IDs, pytest markers, and repository sources.

Each row represents an inspected pytest test function from the SauceDemo UI suite. Browser evidence is retained only on failure according to the pytest configuration.

---

## Test Cases

| Test Case ID | Scenario ID | Requirement ID | Test Case | Priority | Markers / Tags | Execution Model | Automation Source | Status |
|---|---|---|---|---|---|---|---|---|
| `TC-UI-001` | `TS-UI-001` | `FR-UI-001` | Valid login and logout | Critical | `ui, smoke` | Single pytest test | `tests/ui/test_loginpage.py::test_ui_login_and_logout` | Automated |
| `TC-UI-002` | `TS-UI-002` | `FR-UI-002` | Empty login displays an error | High | `ui` | Single pytest test | `tests/ui/test_loginpage.py::test_ui_empty_login_shows_err` | Automated |
| `TC-UI-003` | `TS-UI-003` | `FR-UI-002` | Invalid username displays an error | High | `ui` | Single pytest test | `tests/ui/test_loginpage.py::test_ui_invalid_username_shows_err` | Automated |
| `TC-UI-004` | `TS-UI-004` | `FR-UI-002` | Invalid password displays an error | High | `ui` | Single pytest test | `tests/ui/test_loginpage.py::test_ui_invalid_password_shows_err` | Automated |
| `TC-UI-005` | `TS-UI-005` | `FR-UI-002` | Locked-out user displays an error | High | `ui` | Single pytest test | `tests/ui/test_loginpage.py::test_ui_locked_out_user_shows_err` | Automated |
| `TC-UI-006` | `TS-UI-006` | `FR-UI-003` | Inventory item details are displayed correctly | High | `ui, smoke` | Single pytest test | `tests/ui/test_inventorypage.py::test_ui_login_items_checked` | Automated |
| `TC-UI-007` | `TS-UI-007` | `FR-UI-004` | Inventory products can be sorted | Medium | `ui, smoke` | Single pytest test | `tests/ui/test_inventorypage.py::test_ui_login_sort_items` | Automated |
| `TC-UI-008` | `TS-UI-008` | `FR-UI-005` | Products can be added and removed from inventory, details, and cart | High | `ui, smoke` | Single pytest test | `tests/ui/test_inventorypage.py::test_ui_login_add_items_to_cart` | Automated |
| `TC-UI-009` | `TS-UI-009` | `FR-UI-005` | Cart count matches cart contents | High | `ui, smoke` | Single pytest test | `tests/ui/test_cartpage.py::test_ui_login_check_cart_count_matches` | Automated |
| `TC-UI-010` | `TS-UI-009` | `FR-UI-005` | Cart count persists after refresh | High | `ui, smoke` | Single pytest test | `tests/ui/test_inventorypage.py::test_ui_login_refresh_page_check_cart_count_persists` | Automated |
| `TC-UI-011` | `TS-UI-010` | `FR-UI-006` | Inventory cannot be accessed directly after logout | High | `ui, smoke` | Single pytest test | `tests/ui/test_inventorypage.py::test_ui_bypass_loginpage_to_inventorypage` | Automated |
| `TC-UI-012` | `TS-UI-011` | `FR-UI-006` | A new tab opens in the expected session state | Medium | `ui, smoke` | Single pytest test | `tests/ui/test_inventorypage.py::test_ui_new_tab` | Automated |
| `TC-UI-013` | `TS-UI-011` | `FR-UI-006` | A new browser context does not inherit the authenticated session | High | `ui, smoke` | Single pytest test | `tests/ui/test_inventorypage.py::test_ui_new_session` | Automated |
| `TC-UI-014` | `TS-UI-012` | `FR-UI-007` | Checkout rejects an empty customer-information form | High | `ui` | Single pytest test | `tests/ui/test_checkoutpage.py::test_ui_login_checkout_empty_form` | Automated |
| `TC-UI-015` | `TS-UI-012` | `FR-UI-007` | Checkout rejects a missing first name | High | `ui` | Single pytest test | `tests/ui/test_checkoutpage.py::test_ui_login_checkout_empty_firstname` | Automated |
| `TC-UI-016` | `TS-UI-012` | `FR-UI-007` | Checkout rejects a missing last name | High | `ui` | Single pytest test | `tests/ui/test_checkoutpage.py::test_ui_login_checkout_empty_lastname` | Automated |
| `TC-UI-017` | `TS-UI-012` | `FR-UI-007` | Checkout rejects a missing postal code | High | `ui` | Single pytest test | `tests/ui/test_checkoutpage.py::test_ui_login_checkout_empty_zip` | Automated |
| `TC-UI-018` | `TS-UI-013` | `FR-UI-008` | Authenticated user completes the checkout happy path | Critical | `ui, smoke` | Single pytest test | `tests/ui/test_checkoutpage.py::test_ui_login_add_items_to_cart_checkout` | Automated |
| `TC-UI-019` | `TS-UI-014` | `FR-UI-009` | Twitter navigation opens correctly | Medium | `ui, smoke` | Single pytest test | `tests/ui/test_navigation.py::test_ui_visit_twitter` | Automated |
| `TC-UI-020` | `TS-UI-014` | `FR-UI-009` | Facebook navigation opens correctly | Medium | `ui, smoke` | Single pytest test | `tests/ui/test_navigation.py::test_ui_visit_facebook` | Automated |
| `TC-UI-021` | `TS-UI-014` | `FR-UI-009` | LinkedIn navigation opens correctly | Medium | `ui, smoke` | Single pytest test | `tests/ui/test_navigation.py::test_ui_visit_linkedin` | Automated |
| `TC-UI-022` | `TS-UI-014` | `FR-UI-009` | About navigation opens correctly | Medium | `ui, smoke` | Single pytest test | `tests/ui/test_navigation.py::test_ui_visit_about` | Automated |
| `TC-UI-023` | `TS-UI-015` | `FR-UI-010` | Application state can be reset | Medium | `ui, smoke` | Single pytest test | `tests/ui/test_navigation.py::test_ui_resetting_app_state` | Automated |

---

## Traceability Rule

- Requirement IDs originate from `requirements-analysis.md`.
- Scenario IDs originate from `test-scenarios.md`.
- Concrete pytest node IDs use the format `path::test_function`.
- Parametrized tests identify their execution count where confirmed.
- Expected failures marked with `xfail` document known target limitations and are not treated as ordinary passed tests.
