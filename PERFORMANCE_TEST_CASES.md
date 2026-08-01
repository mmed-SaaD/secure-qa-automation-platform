# Secure QA Automation Platform - Performance Test Cases

**Project:** Secure QA Automation Platform  
**Document Version:** 1.0  
**Author:** BAZOURHI Mohamed Saad  
**Document Type:** Test Cases

---

## Purpose

This document maps implemented test coverage to requirement IDs, scenario IDs, pytest markers, and repository sources.

Performance coverage is based on the repository README and performance architecture. Each row represents one implemented workload or workflow category rather than an invented per-endpoint expansion.

---

## Test Cases

| Test Case ID | Scenario ID | Requirement ID | Test Case | Priority | Markers / Tags | Execution Model | Automation Source | Status |
|---|---|---|---|---|---|---|---|---|
| `TC-PERF-001` | `TS-PERF-001` | `NFR-PERF-001` | Measure all-products endpoint response time and error rate | High | `performance, k6` | k6 scenario | `tests/performance` | Automated |
| `TC-PERF-002` | `TS-PERF-002` | `NFR-PERF-001` | Measure single-product endpoint response time | High | `performance, k6` | k6 scenario | `tests/performance` | Automated |
| `TC-PERF-003` | `TS-PERF-003` | `NFR-PERF-001` | Measure filtered-products request performance | Medium | `performance, k6` | k6 scenario | `tests/performance` | Automated |
| `TC-PERF-004` | `TS-PERF-004` | `NFR-PERF-002` | Measure product-creation latency and error rate | High | `performance, k6` | k6 scenario | `tests/performance` | Automated |
| `TC-PERF-005` | `TS-PERF-005` | `NFR-PERF-004` | Measure authenticated login, user-information, and product-access workflow | High | `performance, k6, auth` | k6 workflow | `tests/performance` | Automated |
| `TC-PERF-006` | `TS-PERF-006` | `NFR-PERF-003` | Measure progressive-load degradation and system failure point | High | `performance, k6, stress` | k6 stress scenario | `tests/performance` | Automated |
| `TC-PERF-007` | `TS-PERF-007` | `NFR-PERF-005` | Measure SauceDemo end-to-end happy-path duration | Medium | `performance_ui, ui` | pytest UI performance workflow | `tests/performance` | Automated |

---

## Traceability Rule

- Requirement IDs originate from `requirements-analysis.md`.
- Scenario IDs originate from `test-scenarios.md`.
- Concrete pytest node IDs use the format `path::test_function`.
- Parametrized tests identify their execution count where confirmed.
- Expected failures marked with `xfail` document known target limitations and are not treated as ordinary passed tests.
