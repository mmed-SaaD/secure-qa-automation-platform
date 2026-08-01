# Requirements Analysis

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Requirements Analysis

---

## 1. Purpose

This document defines requirements derived from the repository's implemented tests, README, configuration, and automation structure.

The original stakeholder specification is not available. Therefore, these are **derived requirements** and should not be presented as original client requirements.

---

## 2. Systems

- DummyJSON API
- SauceDemo web application
- PostgreSQL Pagila database
- OWASP Juice Shop
- GitHub Actions and Allure reporting pipeline

---

## 3. Functional Requirements

### FR-API-001 API Availability

DummyJSON API endpoints used by the project shall be reachable and return controlled HTTP responses.

**Acceptance Criteria**

- Core endpoints respond.
- Successful requests return expected status codes.
- Invalid routes return controlled errors.
- Responses remain parseable.

**Priority:** High

---

### FR-API-002 Authentication

Users shall be able to authenticate with valid DummyJSON credentials and receive an access token.

**Acceptance Criteria**

- Valid credentials return `200`.
- An access token is present and non-empty.
- Invalid credentials are rejected.
- Missing or invalid authorization is rejected.

**Priority:** Critical

---

### FR-API-003 Protected Resource Access

Protected API resources shall require a valid access token.

**Acceptance Criteria**

- Valid tokens permit access.
- Missing tokens return unauthorized responses.
- Invalid authentication does not permit protected access.

**Priority:** Critical

---

### FR-API-004 Product Catalogue

The API shall expose product collections and product records with consistent fields and metadata.

**Acceptance Criteria**

- Product collections are non-empty.
- Product IDs are unique.
- Required fields are present.
- Numeric and string fields use expected data types.
- Pagination metadata is coherent.

**Priority:** High

---

### FR-API-005 User Retrieval

The API shall provide user collections and individual users.

**Acceptance Criteria**

- User lists are returned successfully.
- User IDs are unique.
- Required fields are present.
- Email values follow a valid format.
- Individual-user responses match the requested ID.

**Priority:** High

---

### FR-API-006 Cart Retrieval and Calculation

The API shall expose carts and calculate totals consistently.

**Acceptance Criteria**

- Cart collections and individual carts are retrievable.
- Carts contain expected product structures.
- Product totals equal price multiplied by quantity.
- Discounted totals are calculated correctly.
- Cart-level totals, quantities, and product counts are coherent.

**Priority:** High

---

### FR-API-007 Recipe Retrieval

The API shall allow recipe collections and individual recipes to be retrieved.

**Priority:** Medium

---

### FR-API-008 Recipe Creation and Update

The API shall accept supported recipe creation and update operations.

**Priority:** Medium

---

### FR-API-009 Recipe Deletion

The API shall support recipe deletion behaviour.

**Priority:** Medium

---

### FR-API-010 API Contract Validation

API responses shall follow expected JSON structures.

**Priority:** High

---

### FR-UI-001 User Login and Logout

SauceDemo users shall be able to log in with valid credentials and log out.

**Priority:** Critical

---

### FR-UI-002 Login Validation

Invalid, empty, or locked-user credentials shall be rejected with visible error feedback.

**Priority:** High

---

### FR-UI-003 Inventory Validation

Authenticated users shall be able to view inventory and product details.

**Priority:** High

---

### FR-UI-004 Product Sorting

Users shall be able to sort inventory products.

**Priority:** Medium

---

### FR-UI-005 Cart Management

Users shall be able to add, remove, and review cart items.

**Priority:** High

---

### FR-UI-006 Access Control and Session Isolation

Unauthenticated or newly isolated sessions shall not inherit authenticated access.

**Priority:** High

---

### FR-UI-007 Checkout Validation

Checkout shall reject missing mandatory customer information.

**Priority:** High

---

### FR-UI-008 Successful Checkout

An authenticated user with products in the cart shall be able to complete checkout.

**Priority:** Critical

---

### FR-UI-009 Navigation

Application and external navigation links shall function correctly.

**Priority:** Medium

---

### FR-UI-010 Application State Reset

Authenticated users shall be able to reset the application state.

**Priority:** Medium

---

### FR-DB-001 Database Connectivity

The platform shall establish a valid connection to the PostgreSQL Pagila database.

**Priority:** Critical

---

### FR-DB-002 Schema Validation

Required tables, columns, keys, and relationships shall exist.

**Priority:** High

---

### FR-DB-003 Query Validation

Queries shall return expected structures and controlled results.

**Priority:** High

---

### FR-DB-004 CRUD Operations

Supported records shall be inserted, read, updated, and deleted correctly.

**Priority:** High

---

### FR-DB-005 Data Integrity

Database constraints and relationships shall preserve data consistency.

**Priority:** Critical

---

### FR-DB-006 Transaction Behaviour

Transactions shall commit and roll back correctly.

**Priority:** High

---

### FR-DB-007 Database Permissions

Database users shall only perform authorized operations.

**Priority:** Critical

---

### FR-DB-008 Sensitive Data Protection

Database queries and outputs shall not expose sensitive information unnecessarily.

**Priority:** Critical

---

## 4. Non-Functional Requirements

### NFR-PERF-001 API Response Time

Selected API endpoints shall meet configured average and percentile response-time thresholds.

### NFR-PERF-002 Error Rate

The error rate shall remain within configured limits during supported workloads.

### NFR-PERF-003 Stress Behaviour

The system's degradation and failure point shall be measurable under progressive load.

### NFR-PERF-004 Authenticated Workflow Performance

Login and protected API operations shall remain measurable and stable under the configured workload.

### NFR-PERF-005 UI Journey Timing

The SauceDemo end-to-end happy path shall be measured at workflow level.

### NFR-SEC-001 Injection Resistance

Authentication inputs shall resist injection-based bypass attempts.

### NFR-SEC-002 Broken Access Control

Users shall not access resources belonging to other users by manipulating identifiers.

### NFR-SEC-003 Cross-Site Scripting

User-controlled input shall not execute unauthorized scripts in the browser.

### NFR-SEC-004 Security Configuration

Security headers and application configuration shall not expose avoidable weaknesses.

### NFR-SEC-005 Automated Vulnerability Scanning

OWASP ZAP scans shall identify and report common vulnerabilities.

### NFR-REP-001 Reporting

Automated executions shall produce Allure-compatible results with suite, duration, status, and evidence information.

### NFR-CI-001 Continuous Integration

The platform shall execute automated tests on configured push, pull-request, schedule, and manual triggers.

### NFR-CI-002 Secure Configuration

Credentials and environment-specific values shall be injected through environment variables or GitHub Secrets.

---

## 5. Assumptions and Limitations

- DummyJSON, SauceDemo, and OWASP Juice Shop are external or laboratory systems.
- Requirements reflect implemented behaviour, not original stakeholder specifications.
- Some public APIs simulate writes rather than permanently persisting data.
- Performance results depend on the execution environment.
- Security findings require manual validation before defect classification.
