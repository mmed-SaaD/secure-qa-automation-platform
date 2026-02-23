# Test Strategy — Secure QA Automation Platform

## 1. Purpose
Define how we will test the System Under Test (SUT) in a production-style way: functional + non-functional + security.

## 2. System Under Test (SUT)
Online Boutique (Google Microservices Demo) running locally via Docker.

## 3. Goals
- Validate core user journeys (browse → cart → checkout)
- Validate API/service behavior and contracts
- Detect security issues early (DAST + misconfig checks)
- Validate performance baselines and regressions
- Provide CI-ready, repeatable execution and reporting

## 4. In Scope
- UI: storefront critical flows
- API: core endpoints behind frontend (as observable via HTTP)
- Security: baseline DAST, headers, auth/session behavior, common web vulns scanning
- Performance: smoke + baseline load tests for key flows


## 5. Test Levels & Types
### 5.1 Smoke
- Homepage reachable
- Product listing loads
- Add to cart works

### 5.2 Functional / Regression
- Cart operations
- Checkout happy path
- Negative cases (invalid quantity, empty cart checkout)

### 5.3 API Contract Checks
- Schema validation (basic)
- Status codes and error handling
- Idempotency where relevant

### 5.4 Security (DAST)
- OWASP ZAP baseline scan against the routed frontend
- Security headers checks
- Cookie flags review (Secure/HttpOnly/SameSite)
- Basic injection probes (safe, non-destructive)

### 5.5 Performance
- k6 smoke: low VU short run
- Baseline: fixed VU for fixed time + thresholds

## 6. Environments
- Local Docker Compose environment (primary)
- CI environment (GitHub Actions) later

## 7. Tooling (planned)
- Pytest for test execution
- Playwright for UI automation (later phase)
- OWASP ZAP for DAST
- k6 for performance
- GitHub Actions for CI

## 8. Reporting
- Test results in CI logs + artifacts
- Later: Allure or similar reporting (phase planned)

## 9. Definition of Done
A phase is “done” when:
- Tests run locally consistently
- Readme updated
- CI step (if applicable) added
- Results are reproducible