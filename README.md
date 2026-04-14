# 🚀 Secure QA Automation Platform

A professional QA automation framework designed to simulate real-world testing practices across UI, API, DB, Security and Performance layers.

---

## 📌 Project Overview

This project demonstrates a **production-style QA automation setup** using modern tools and best practices.

It covers:
- UI automation (end-to-end workflows)
- API testing (functional & negative scenarios)
- Structured test design (workflow-based)
- Reusable architecture (Page Object Model, fixtures, utilities)
- Test reporting (Allure)
- Failure artifacts (screenshots, videos, traces)
---

## 🧰 Tech Stack

- **Language:** Python 3.12
- **Test Framework:** pytest
- **UI Automation:** Playwright
- **API Testing:** requests
- **Reporting:** Allure
- **Configuration:** python-dotenv
- **Parallel Execution:** pytest-xdist
- **Retry Logic:** pytest-rerunfailures

---

## 🏗️ Project Structure


secure-qa-automation-platform/
│
├── core/ # Config, utilities, drivers, logging
├── src/
│ └── ui/pages/ # Page Object Model (UI layer)
│
├── tests/
│ ├── ui/ # UI test scenarios
│ ├── api/ # API test scenarios
│ ├── db/ # (planned)
│ └── security/ # (planned)
│
├── reports/ # Test results & Allure outputs
├── pytest.ini # Test configuration & markers
├── requirements.txt
└── README.md


---

## 🧪 Testing Scope

### ✅ UI Testing (Playwright)

Covers real user workflows on SauceDemo:

- Authentication
  - Valid login
  - Invalid login
  - Locked user
  - Logout

- Product Interaction
  - View product list
  - Open product details
  - Verify consistency

- Sorting
  - Name (A-Z / Z-A)
  - Price (low-high / high-low)

- Cart Management
  - Add/remove items
  - Cart badge validation

- Checkout Flow
  - Complete purchase
  - Validate totals
  - Order confirmation

- Negative Scenarios
  - Missing required fields
  - Error message validation

---

### 🌐 API Testing

Covers functional and negative API scenarios:

- Connectivity checks
- Response validation (status, timing)
- Data integrity checks
- Negative cases (invalid inputs, edge cases)

---

## ⚙️ Test Configuration

### Markers (pytest.ini)

- `ui` → UI tests
- `api` → API tests
- `smoke` → critical tests
- `regression` → full coverage
- `security` → security-related tests (planned)

---

## ▶️ How to Run Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Set environment variables

Create .env file:

BASE_URL=https://www.saucedemo.com/
HEADLESS=true
3. Run tests
Run all tests
pytest
Run UI tests
pytest -m ui
Run API tests
pytest -m api
Run smoke tests
pytest -m smoke
📊 Reporting (Allure)

Generate Allure report:

allure serve reports/allure-results

The report includes:

Test execution summary
Pass/fail breakdown
Detailed logs
Failure screenshots & traces
📸 Failure Artifacts

On test failure, the framework automatically captures:

Screenshots
Videos
Playwright traces

Stored in:

artifacts/
🧠 Design Approach

This project follows real-world QA engineering practices:

Page Object Model (UI abstraction)
Fixtures for reusable setup
Workflow-based test design
Separation of concerns (UI vs API vs utilities)
Config-driven execution
Scalable structure for future extensions
🚧 Roadmap

Planned improvements:

 CI/CD integration (GitHub Actions)
 Performance testing (k6 / locust)
 Database validation layer
 Security testing (DAST tools)
 Dockerized execution
 Hosted Allure reports
🎯 Portfolio Value

This project demonstrates:

End-to-end QA automation skills     
Strong test organization and architecture
Ability to simulate real QA workflows
Understanding of both UI and API testing
Readiness for junior QA automation roles