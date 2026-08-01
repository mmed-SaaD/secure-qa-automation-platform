# Test Strategy

**Project:** Secure QA Automation Platform  
**Applications Under Test:** DummyJSON, SauceDemo, PostgreSQL Pagila, OWASP Juice Shop  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Strategy

---

## 1. Purpose

This document defines the overall testing approach for the Secure QA Automation Platform.

The project combines API, UI, database, performance, and security testing within one structured automation solution. The strategy focuses on repeatability, layered validation, maintainability, risk reduction, and continuous feedback through automated reporting and CI/CD.

---

## 2. Objectives

The testing strategy aims to:

- Validate core functional behaviour across API, UI, and database layers.
- Detect regressions in business-critical workflows.
- Verify API contracts, authentication, authorization, and data consistency.
- Validate SauceDemo user journeys through browser automation.
- Confirm PostgreSQL Pagila database connectivity, integrity, transactions, permissions, and query behaviour.
- Measure backend and end-to-end workflow performance using k6.
- Identify and reproduce common OWASP-related security weaknesses.
- Generate structured Allure reports.
- Execute tests automatically through GitHub Actions.

---

## 3. Systems Under Test

| System | Purpose | Main Test Layers |
|---|---|---|
| DummyJSON | Public test API for products, users, carts, recipes, and authentication | API, Performance |
| SauceDemo | Web application used for browser-based functional and end-to-end validation | UI, UI Performance |
| PostgreSQL Pagila | Relational sample database used for database validation | Database |
| OWASP Juice Shop | Intentionally vulnerable application used for security testing | Security |

---

## 4. Scope

### In Scope

#### API Testing

- Endpoint availability
- Authentication
- Protected-resource access
- Products
- Users
- Carts
- Recipes
- Response schema and metadata
- Positive and negative requests
- Authorization failures
- End-to-end API workflows

#### UI Testing

- Login and logout
- Invalid and locked-user authentication
- Inventory and product details
- Product sorting
- Cart operations
- Cart persistence
- Checkout validation
- Successful checkout
- Navigation and external links
- Session isolation
- Application state reset

#### Database Testing

- Connectivity
- Schema validation
- Query validation
- CRUD operations
- Data integrity
- Transactions
- Permissions
- Sensitive-data exposure
- Query performance

#### Performance Testing

- Product collection requests
- Single-product requests
- Product filtering
- Product creation
- Authenticated API workflow
- SauceDemo end-to-end journey timing
- Response time, p95, error rate, and iteration behaviour
- Stress and degradation analysis

#### Security Testing

- Authentication bypass through injection
- Broken access control and IDOR
- Reflected XSS
- Security misconfiguration
- Automated OWASP ZAP scanning
- Manual validation of automated findings

### Out of Scope

- Native mobile applications
- Full accessibility certification
- Localization testing
- Production penetration testing
- Source-code security review
- Payment-gateway integration
- Destructive testing against non-laboratory environments

---

## 5. Test Levels and Types

| Test Level | Test Types |
|---|---|
| API | Functional, contract, negative, authorization, smoke, end-to-end |
| UI | Functional, smoke, negative, navigation, session, end-to-end |
| Database | Connectivity, schema, CRUD, integrity, transaction, permission, performance |
| Performance | Smoke, load, stress, workflow timing |
| Security | Vulnerability scanning, exploitation validation, access control, injection, XSS |

---

## 6. Test Design Techniques

The project applies:

- Positive testing
- Negative testing
- Equivalence partitioning
- Boundary and invalid-input validation
- Error guessing
- State-transition testing
- End-to-end workflow testing
- API contract validation
- Risk-based testing
- Data-integrity verification
- Security attack simulation
- Performance threshold validation

---

## 7. Automation Architecture

The platform uses a layered architecture:

- `src/` contains reusable page objects, API models, helpers, and abstractions.
- `tests/` contains test suites organized by API, UI, database, performance, and security domains.
- Shared fixtures and configuration are managed through pytest.
- Test categories are controlled using pytest markers.
- Playwright supports browser automation.
- Requests supports API interactions.
- PostgreSQL is used for database validation.
- k6 executes performance scenarios.
- OWASP ZAP supports automated security analysis.
- Allure provides reporting.

This separation improves reuse, scalability, maintainability, and failure analysis.

---

## 8. Test Data Strategy

Test data may be:

- Loaded through environment variables and secrets.
- Defined in fixtures.
- Retrieved from public test systems.
- Created dynamically for write operations.
- Isolated where possible to avoid cross-test dependency.
- Cleaned up after destructive or write-based tests when supported.

Sensitive values must not be hardcoded in the repository.

---

## 9. Environment Strategy

The platform supports local and CI execution.

Required environments include:

- Python 3.12
- pytest
- Playwright browsers
- Access to DummyJSON
- SauceDemo credentials
- PostgreSQL Pagila database
- OWASP Juice Shop
- k6
- OWASP ZAP
- Allure tooling
- Docker where required

---

## 10. Entry Criteria

Testing may begin when:

- Dependencies are installed.
- Required applications and services are reachable.
- Environment variables and secrets are configured.
- Browser dependencies are available.
- Database connectivity is confirmed.
- Required test data is available.
- The selected pytest marker or suite is known.

---

## 11. Exit Criteria

Testing is considered complete when:

- Planned suites have executed.
- Critical workflows have been validated.
- Execution evidence is available.
- Failures have been classified as product, environment, data, or automation issues.
- Critical defects are documented.
- Allure reports are generated.
- Remaining risks and limitations are recorded.

---

## 12. Defect Management

Failed tests must be analysed before a defect is raised.

A confirmed defect should include:

- Defect ID
- Related requirement
- Related scenario and automated test
- Environment
- Preconditions
- Reproduction steps
- Expected result
- Actual result
- Severity and priority
- Evidence
- Logs, screenshots, traces, API responses, or reports

---

## 13. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Public test services change unexpectedly | Use clear assertions, isolate contracts, and document external dependencies |
| Environment or network instability | Apply retries only where justified and distinguish infrastructure failures from product failures |
| Shared test data causes collisions | Generate unique data and clean up created records |
| Browser timing causes flaky tests | Use Playwright auto-waiting and page-object abstractions |
| Security tools produce false positives | Manually validate findings before defect classification |
| Performance results vary by environment | Record thresholds, load model, host resources, and execution context |
| Database tests modify shared data | Use transactions, rollback, and isolated records |
| Secrets are exposed | Use environment variables and GitHub Secrets |

---

## 14. Reporting and CI/CD

Allure reports provide:

- Execution overview
- Suite organization
- Duration distribution
- Timeline analysis
- Failure details
- Evidence for UI failures

GitHub Actions executes tests on:

- Pushes to `main`
- Pull requests targeting `main`
- Scheduled daily runs
- Manual execution with selectable suites

The pipeline installs dependencies, configures Python and Playwright, executes the selected tests, builds Allure reports, and publishes the latest report through GitHub Pages.

---

## 15. Deliverables

- Automated API tests
- Automated UI tests
- Database validation tests
- k6 performance scripts
- Security tests and ZAP scans
- Allure reports
- CI/CD workflow
- Test Strategy
- Test Plan
- Requirements Analysis
- Test Scenarios
- Requirements Traceability Matrix

---

## 16. Conclusion

The Secure QA Automation Platform uses a multi-layer strategy to validate functionality, data, performance, and security across several controlled systems.

The combination of pytest, Playwright, API validation, PostgreSQL testing, k6, OWASP ZAP, Allure, Docker, and GitHub Actions provides a production-oriented foundation for scalable QA automation.
