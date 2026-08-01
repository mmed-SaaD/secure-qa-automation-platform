# Secure QA Automation Platform - Security Test Cases

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Cases

---

## Purpose

This document maps implemented test coverage to requirement IDs, scenario IDs, pytest markers, and repository sources.

Security coverage represents the documented automated and manual-validation workflow against OWASP Juice Shop. Scanner findings must be manually confirmed before being recorded as defects.

---

## Test Cases

| Test Case ID | Scenario ID | Requirement ID | Test Case | Priority | Markers / Tags | Execution Model | Automation Source | Status |
|---|---|---|---|---|---|---|---|---|
| `TC-SEC-001` | `TS-SEC-001` | `NFR-SEC-001` | Validate authentication bypass through injection | Critical | `security, injection` | Automated attack validation | `tests/security` | Automated |
| `TC-SEC-002` | `TS-SEC-002` | `NFR-SEC-002` | Validate broken access control and IDOR behaviour | Critical | `security, idor, access-control` | Automated attack validation | `tests/security` | Automated |
| `TC-SEC-003` | `TS-SEC-003` | `NFR-SEC-003` | Validate reflected XSS behaviour | High | `security, xss` | Automated browser/API validation | `tests/security` | Automated |
| `TC-SEC-004` | `TS-SEC-004` | `NFR-SEC-004` | Validate security headers and configuration | High | `security, misconfiguration` | Automated configuration validation | `tests/security` | Automated |
| `TC-SEC-005` | `TS-SEC-005` | `NFR-SEC-005` | Run OWASP ZAP automated scan | High | `security, zap` | Automated scan | `tests/security` | Automated |
| `TC-SEC-006` | `TS-SEC-006` | `NFR-SEC-005` | Validate ZAP findings manually before defect classification | High | `security, manual-validation` | Human validation step | `SECURITY_TESTING_WORKFLOW.MD` | Documented |

---

## Traceability Rule

- Requirement IDs originate from `requirements-analysis.md`.
- Scenario IDs originate from `test-scenarios.md`.
- Concrete pytest node IDs use the format `path::test_function`.
- Parametrized tests identify their execution count where confirmed.
- Expected failures marked with `xfail` document known target limitations and are not treated as ordinary passed tests.
