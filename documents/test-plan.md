# Test Plan

**Project:** Secure QA Automation Platform  
**Applications Under Test:** DummyJSON, SauceDemo, PostgreSQL Pagila, OWASP Juice Shop  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Plan

---

## 1. Purpose

This Test Plan defines the execution approach for the Secure QA Automation Platform.

It describes the planned scope, systems, test items, resources, environments, sequence, entry and exit criteria, risks, reporting, and deliverables for API, UI, database, performance, and security testing.

---

## 2. Objectives

The project will:

- Validate DummyJSON API availability, contracts, data, authentication, and workflows.
- Validate SauceDemo login, inventory, cart, checkout, navigation, and session behaviour.
- Validate PostgreSQL Pagila connectivity, schema, CRUD, integrity, transactions, permissions, and performance.
- Measure API and UI workflow performance using k6.
- Validate selected OWASP Juice Shop vulnerabilities through scanning and controlled attack simulation.
- Produce Allure reports.
- Run automated suites through GitHub Actions.

---

## 3. Test Items

| Test Item | Application | Test Layer |
|---|---|---|
| Authentication and protected endpoints | DummyJSON | API |
| Products, users, carts, and recipes | DummyJSON | API |
| Login, inventory, cart, checkout, navigation | SauceDemo | UI |
| Database connection, schema, CRUD, transactions, permissions | PostgreSQL Pagila | Database |
| API and browser workflow performance | DummyJSON / SauceDemo | Performance |
| Injection, IDOR, XSS, misconfiguration, ZAP scanning | OWASP Juice Shop | Security |

---

## 4. Scope

### Included

- Functional API validation
- API response schema and metadata
- Positive and negative API behaviour
- Browser-based functional testing
- End-to-end checkout
- Session and state validation
- Database CRUD and integrity
- Database permissions and security checks
- Database and API performance
- UI journey timing
- Security scanning and exploit validation
- Allure reporting
- CI/CD execution

### Excluded

- Mobile testing
- Accessibility certification
- Localization
- Source-code review
- Production penetration testing
- Real payment processing
- Unsupported browsers not configured in the framework

---

## 5. Test Approach

Testing is automated and layered.

Execution may be selected using pytest markers such as:

- `smoke`
- `api`
- `ui`
- `security`
- `auth`
- `unauthorized`
- `negative`
- `e2e`
- `db`
- `performance_ui`

The recommended execution order is:

1. Environment validation
2. Smoke tests
3. API tests
4. UI tests
5. Database tests
6. Performance tests
7. Security tests
8. Allure report generation
9. Result review and defect classification

---

## 6. Test Environment

| Component | Technology / System |
|---|---|
| Test runner | pytest |
| Programming language | Python 3.12 |
| UI automation | Playwright |
| API client | Requests |
| Database | PostgreSQL Pagila |
| Performance | k6 |
| Security | OWASP ZAP and controlled manual validation |
| Reporting | Allure |
| Containers | Docker |
| CI/CD | GitHub Actions |
| API SUT | DummyJSON |
| UI SUT | SauceDemo |
| Security SUT | OWASP Juice Shop |

---

## 7. Test Data

Required data includes:

- Valid and invalid DummyJSON credentials
- Protected-endpoint tokens
- Product, user, cart, and recipe IDs
- Valid, locked, and invalid SauceDemo users
- Checkout customer data
- PostgreSQL connection details
- Isolated database records
- Security payloads
- k6 workload configuration

Credentials and secrets must be injected through environment variables or GitHub Secrets.

---

## 8. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| QA Automation Engineer | Design, implement, maintain, execute, and analyse tests |
| pytest framework | Discover and execute automated tests |
| GitHub Actions | Execute CI suites and publish reports |
| Allure | Present test results and evidence |
| k6 | Execute performance workloads |
| OWASP ZAP | Perform automated security scanning |

---

## 9. Entry Criteria

Testing starts when:

- The repository is available.
- Dependencies are installed.
- Required secrets are configured.
- External systems are reachable.
- Playwright browsers are installed.
- Database access is available.
- Security targets are authorized and running.
- The selected suite is identified.

---

## 10. Exit Criteria

Testing is complete when:

- Selected tests have executed.
- Core workflows have been validated.
- Failures have been reviewed.
- Critical defects have been reported.
- Allure reports are available.
- Performance results are recorded.
- Security findings are validated.
- Outstanding risks are documented.

---

## 11. Suspension Criteria

Testing may be suspended when:

- A required system is unavailable.
- Environment configuration is invalid.
- Database connectivity is lost.
- Blocking automation failures prevent execution.
- Test data is corrupted.
- Security testing authorization is unavailable.
- CI infrastructure is unavailable.

---

## 12. Resumption Criteria

Testing resumes when:

- Systems are reachable.
- Blocking configuration issues are resolved.
- Test data is restored.
- Database connectivity is verified.
- Automation blockers are fixed.
- Authorization and tooling are available.

---

## 13. Execution Schedule

The project follows a suite-based execution model rather than fixed calendar dates.

| Trigger | Planned Execution |
|---|---|
| Pull request | CI suite excluding environment-dependent DB tests |
| Push to `main` | Main validation suite and report publication |
| Daily schedule | Smoke tests |
| Manual run | Smoke, API, UI, or full suite |
| Local development | Targeted marker, module, or individual test |

---

## 14. Risks

- Third-party API behaviour may change.
- Public demo applications may be unavailable.
- Shared user accounts may create state conflicts.
- Browser tests may fail due to timing or environment issues.
- Database tests may affect shared records.
- Performance results depend on execution infrastructure.
- Security scanners may report false positives.
- External systems are not controlled by the project owner.

---

## 15. Mitigation

- Keep tests modular and isolated.
- Use page objects and reusable API abstractions.
- Generate unique data for write scenarios.
- Use transaction rollback where appropriate.
- Store secrets securely.
- Separate smoke, API, UI, DB, performance, and security execution.
- Validate security findings manually.
- Record environment details for performance runs.
- Preserve traces, screenshots, and videos only on failure.

---

## 16. Deliverables

- Test Strategy
- Test Plan
- Requirements Analysis
- Test Scenarios
- RTM
- Automated pytest suites
- k6 performance tests
- Security tests and ZAP results
- Allure reports
- GitHub Actions pipeline

---

## 17. Approval Criteria

The test cycle is acceptable when:

- Core API and UI smoke tests pass.
- Critical workflows execute successfully.
- No unreviewed critical security finding remains.
- Database integrity tests complete without unexplained failures.
- Performance results are captured and compared with configured thresholds.
- Reports are generated and accessible.

---

## 18. Conclusion

This Test Plan provides the execution framework for validating the Secure QA Automation Platform across API, UI, database, performance, and security layers.

It supports targeted local execution, automated CI feedback, scheduled smoke validation, and continuously published reporting.
