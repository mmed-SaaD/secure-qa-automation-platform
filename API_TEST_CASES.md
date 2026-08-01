# Secure QA Automation Platform - API Test Cases

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Cases

---

## Purpose

This document maps implemented test coverage to requirement IDs, scenario IDs, pytest markers, and repository sources.

Rows with a concrete `module::test_function` source represent inspected pytest functions. Rows that reference only a module are intentionally kept at module level because the repository contains additional workflow and parametrized definitions; they are not expanded into invented cases.

---

## Test Cases

| Test Case ID | Scenario ID | Requirement ID | Test Case | Priority | Markers / Tags | Execution Model | Automation Source | Status |
|---|---|---|---|---|---|---|---|---|
| `TC-API-001` | `TS-API-001` | `FR-API-001` | API test endpoint is reachable within the response-time limit | High | `api, smoke` | Single pytest test | `tests/api/connectivity/test_api_reachable.py::test_api_is_reachable` | Automated |
| `TC-API-002` | `TS-API-001` | `FR-API-001` | Core API endpoints return successful responses | High | `api, smoke` | Parametrized: 8 endpoints | `tests/api/connectivity/test_api_reachable.py::test_api_core_endpoints` | Automated |
| `TC-API-003` | `TS-API-001` | `FR-API-010` | Core endpoint bodies contain the expected collection key | High | `api, smoke` | Parametrized: 7 endpoints | `tests/api/connectivity/test_api_reachable.py::test_api_endpoint_body_form` | Automated |
| `TC-API-004` | `TS-API-002` | `FR-API-002` | Valid credentials return an access token | Critical | `api, auth, smoke` | Single pytest test | `tests/api/auth/test_user_login.py::test_login_valid_credentials` | Automated |
| `TC-API-005` | `TS-API-004` | `FR-API-003` | Valid authentication grants access to protected products | Critical | `api, auth, smoke` | Single pytest test | `tests/api/auth/test_user_login.py::test_valide_auth_protected_endpoint_access` | Automated |
| `TC-API-006` | `TS-API-005` | `FR-API-003` | Invalid authentication cannot access protected products | Critical | `api, unauthorized` | Single pytest test | `tests/api/auth/test_user_login.py::test_protected_endpoint_access_invalid_auth` | Automated |
| `TC-API-007` | `TS-API-003` | `FR-API-002` | Invalid credentials are rejected | High | `api, auth` | Single pytest test | `tests/api/auth/test_user_login.py::test_login_invalid_credentials` | Automated |
| `TC-API-008` | `TS-API-005` | `FR-API-003` | Products listing is rejected without authorization | Critical | `api, unauthorized` | Single pytest test | `tests/api/auth/test_user_login.py::test_unauthorized_products_listing` | Automated |
| `TC-API-009` | `TS-API-006` | `FR-API-004` | Product collection contains valid records, metadata, unique IDs, and field types | High | `api, smoke` | Single pytest test | `tests/api/products/test_api_products.py::test_api_products_collection` | Automated |
| `TC-API-010` | `TS-API-007` | `FR-API-005` | All users contain required fields, valid emails, and unique IDs | High | `api, smoke` | Single pytest test | `tests/api/users/test_api_users.py::test_get_all_users` | Automated |
| `TC-API-011` | `TS-API-007` | `FR-API-005` | A user can be retrieved by ID | High | `api, smoke` | Single pytest test | `tests/api/users/test_api_users.py::test_get_user_by_id` | Automated |
| `TC-API-012` | `TS-API-008` | `FR-API-006` | All carts contain valid product structures | High | `api, smoke` | Single pytest test | `tests/api/carts/test_api_cart.py::test_api_get_all_carts` | Automated |
| `TC-API-013` | `TS-API-008` | `FR-API-006` | A cart can be retrieved by ID | High | `api, smoke` | Single pytest test | `tests/api/carts/test_api_cart.py::test_api_get_cart_by_id` | Automated |
| `TC-API-014` | `TS-API-008` | `FR-API-006` | Carts can be retrieved by user ID | High | `api, smoke` | Single pytest test | `tests/api/carts/test_api_cart.py::test_api_get_cart_by_user` | Automated |
| `TC-API-015` | `TS-API-008` | `FR-API-006` | Cart totals, discounts, quantities, and counts are coherent | Critical | `api, smoke` | Single pytest test | `tests/api/carts/test_api_cart.py::test_api_cart_total_coherance` | Automated |
| `TC-API-016` | `TS-API-009` | `FR-API-007` | All recipes can be retrieved and validated | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_fetch_recipes.py::test_api_get_all_recipes` | Automated |
| `TC-API-017` | `TS-API-009` | `FR-API-007` | A recipe can be retrieved by ID | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_fetch_recipes.py::test_api_get_recipe_by_id` | Automated |
| `TC-API-018` | `TS-API-010` | `FR-API-008` | A valid recipe can be added | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_write_recipes.py::test_api_add_recipe` | Automated |
| `TC-API-019` | `TS-API-013` | `FR-API-008` | Recipe creation rejects an empty payload | Medium | `api, xfail` | Expected failure: target limitation | `tests/api/recipes/test_api_write_recipes.py::test_api_add_recipe_with_empty_payload` | Automated |
| `TC-API-020` | `TS-API-013` | `FR-API-008` | Recipe creation rejects missing required fields | Medium | `api, xfail` | Expected failure: target limitation | `tests/api/recipes/test_api_write_recipes.py::test_api_add_recipe_missing_fields` | Automated |
| `TC-API-021` | `TS-API-010` | `FR-API-008` | A recipe can be updated | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_write_recipes.py::test_api_update_recipe` | Automated |
| `TC-API-022` | `TS-API-010` | `FR-API-008` | A recipe can be partially updated | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_write_recipes.py::test_api_partial_update_recipe` | Automated |
| `TC-API-023` | `TS-API-010` | `FR-API-008` | A recipe can be completely updated | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_write_recipes.py::test_api_complete_update_recipe` | Automated |
| `TC-API-024` | `TS-API-010` | `FR-API-008` | Selected recipe attributes can be patched without changing unrelated fields | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_write_recipes.py::test_api_patch_recipe_attributes` | Automated |
| `TC-API-025` | `TS-API-013` | `FR-API-010` | Unknown recipe fields are rejected | Medium | `api, xfail` | Expected failure: target limitation | `tests/api/recipes/test_api_write_recipes.py::test_api_update_non_existing_recipe_fields` | Automated |
| `TC-API-026` | `TS-API-011` | `FR-API-009` | An existing recipe can be deleted | High | `api, smoke` | Single pytest test | `tests/api/recipes/test_api_delete_recipes.py::test_api_delete_existing_recipe` | Automated |
| `TC-API-027` | `TS-API-011` | `FR-API-009` | A deleted recipe cannot be retrieved | Medium | `api, xfail` | Expected failure: target limitation | `tests/api/recipes/test_api_delete_recipes.py::test_api_retreive_deleted_recipe` | Automated |
| `TC-API-028` | `TS-API-013` | `FR-API-009` | Deleting a non-existing recipe returns a controlled error | Medium | `api` | Single pytest test | `tests/api/recipes/test_api_delete_recipes.py::test_api_delete_non_exisiting_recipe` | Automated |
| `TC-API-029` | `TS-API-013` | `FR-API-009` | Repeated deletion of a recipe is rejected | Medium | `api, xfail` | Expected failure: target limitation | `tests/api/recipes/test_api_delete_recipes.py::test_api_repeatedly_deleting_recipe` | Automated |
| `TC-API-030` | `TS-API-012` | `FR-API-010` | Product collection response schema is stable | High | `api, smoke` | Single pytest test | `tests/api/response/test_api_response_schema.py::test_api_response_products_collection_schema` | Automated |
| `TC-API-031` | `TS-API-012` | `FR-API-010` | Single-recipe response schema is valid | High | `api, smoke` | Single pytest test | `tests/api/response/test_api_response_schema.py::test_api_response_single_recipe_schema` | Automated |
| `TC-API-032` | `TS-API-012` | `FR-API-010` | Cart response schema is valid | High | `api, smoke` | Single pytest test | `tests/api/response/test_api_response_schema.py::test_api_response_cart_schema` | Automated |
| `TC-API-033` | `TS-API-012` | `FR-API-010` | Error response schema contains a message | High | `api, smoke` | Single pytest test | `tests/api/response/test_api_response_schema.py::test_api_response_error_schema` | Automated |
| `TC-API-034` | `TS-API-012` | `FR-API-010` | Authenticated user response schema is valid | High | `api, smoke` | Single pytest test | `tests/api/response/test_api_response_schema.py::test_api_response_auth_response_schema` | Automated |
| `TC-API-035` | `TS-API-012` | `FR-API-010` | Additional response validation workflows execute | High | `api` | Test definitions maintained in module | `tests/api/response/test_api_response_validation.py` | Automated |
| `TC-API-036` | `TS-API-006` | `FR-API-004` | Single-product workflow executes | High | `api` | Test definitions maintained in module | `tests/api/products/test_api_single_product_workflow.py` | Automated |
| `TC-API-037` | `TS-API-006` | `FR-API-004` | Product search workflow executes | High | `api` | Test definitions maintained in module | `tests/api/products/test_api_product_search_workflow.py` | Automated |
| `TC-API-038` | `TS-API-006` | `FR-API-004` | Product pagination parameters are validated | Medium | `api` | Test definitions maintained in module | `tests/api/products/test_api_product_pagination_params.py` | Automated |
| `TC-API-039` | `TS-API-013` | `FR-API-010` | Query-parameter workflow is validated | Medium | `api` | Test definitions maintained in module | `tests/api/query/test_api_query_parameters_workflow.py` | Automated |
| `TC-API-040` | `TS-API-013` | `FR-API-002` | Negative authentication workflow executes | High | `api, negative, auth` | Test definitions maintained in module | `tests/api/negative/auth/test_api_auth_negative_workflow.py` | Automated |
| `TC-API-041` | `TS-API-013` | `FR-API-004` | Negative products workflow executes | High | `api, negative` | Test definitions maintained in module | `tests/api/negative/products/test_api_products_negative_workflow.py` | Automated |
| `TC-API-042` | `TS-API-013` | `FR-API-007` | Negative recipes workflow executes | High | `api, negative` | Test definitions maintained in module | `tests/api/negative/recipes/test_api_recipes_negative_workflow.py` | Automated |
| `TC-API-043` | `TS-API-013` | `FR-API-008` | Login and recipe-booking end-to-end workflow executes | High | `api, e2e` | Test definitions maintained in module | `tests/api/e2e/test_api_e2e_login_booking_recipes.py` | Automated |

---

## Traceability Rule

- Requirement IDs originate from `requirements-analysis.md`.
- Scenario IDs originate from `test-scenarios.md`.
- Concrete pytest node IDs use the format `path::test_function`.
- Parametrized tests identify their execution count where confirmed.
- Expected failures marked with `xfail` document known target limitations and are not treated as ordinary passed tests.
