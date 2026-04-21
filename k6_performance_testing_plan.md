# ⚡ Performance Testing Workflow — QA Automation Project (k6)

---

## 🎯 Objective

This phase focuses on evaluating the performance and responsiveness of the application under different usage scenarios using **k6**.

The goal was to:

* Simulate realistic user behavior
* Measure system performance under load
* Identify latency patterns and potential bottlenecks
* Analyze both API-level and UI-level performance

---

## 🧩 System Under Test (SUT)

* Target: DummyJSON API & associated UI workflows
* Type: REST API with frontend interaction
* Purpose: Simulate real-world user behavior and measure performance impact

---

## 🧰 Tools & Technologies

* k6 (performance testing tool)
* JavaScript (test scripting)
* Custom metrics (Trend, Rate)
* Grafana (visualization) *(optional)*
* InfluxDB (metrics storage) *(optional)*

---

## 🏗️ Workflow Overview

The performance phase was structured into:

1. Scenario-based API Load Testing
2. End-to-End Workflow Simulation
3. UI Performance Measurement

---

# 🟢 Phase 1 — Scenario-Based API Testing

## 🎯 Objective

Test individual API endpoints under controlled load to measure response time and reliability.

---

## 🧪 Scenarios Implemented

### 1. Read All Products

* Endpoint: `/products`
* Goal: Evaluate performance of bulk data retrieval

---

### 2. Read Single Product

* Endpoint: `/products/{id}`
* Goal: Measure latency for individual resource access

---

### 3. Filter Products

* Endpoint: `/products/search`
* Goal: Test performance of query-based filtering

---

### 4. Add Product

* Endpoint: `/products/add`
* Goal: Evaluate write operation performance and system stability

---

## 📊 Metrics Collected

* Response time (avg, p90, p95)
* Error rate
* Throughput

---

## 🧠 Key Insight

Testing isolated endpoints helps establish a **baseline performance profile** before moving to more complex workflows.

---

# 🔵 Phase 2 — End-to-End API Workflow

## 🎯 Objective

Simulate a realistic user journey interacting with multiple endpoints sequentially.

---

## 🧪 Scenario

Authenticated user workflow:

1. Login
2. Retrieve authenticated user information
3. Access product listing as authenticated user

---

## 🧠 Purpose

* Validate system behavior under **stateful interactions**
* Measure cumulative latency across multiple steps
* Ensure consistency across authenticated requests

---

## 📊 Observations

* Slight increase in latency compared to isolated endpoints
* Performance remained stable under moderate load
* No critical failures observed

---

# 🟣 Phase 3 — UI End-to-End Performance (Happy Path)

## 🎯 Objective

Measure full user experience performance from start to completion.

---

## 🧪 Scenario

UI "happy path" workflow:

1. Navigate through application
2. Perform standard user actions
3. Complete full interaction flow

---

## 🔁 Execution

* Total iterations: **6**
* Each iteration measured from:

  ```text
  Start of interaction → Final step completion
  ```

---

## 📊 Metrics Collected

* Total duration per iteration
* Step-level timing (where applicable)
* Consistency across iterations

---

## 🧠 Observations

* Execution times remained relatively consistent
* Minor variations observed between iterations
* No significant performance degradation detected

---

## 🔍 Example Insight

Tracking full iteration time provides a **user-centric performance perspective**, complementing API-level metrics.

---

# 🧠 Key Learnings

* API performance does not always reflect real user experience
* End-to-end workflows introduce cumulative latency
* Monitoring iteration-based performance reveals consistency issues
* Scenario-based testing provides better insights than isolated requests

---

# 🚀 Final Outcome

The performance testing phase successfully evaluated:

* Individual endpoint performance
* Multi-step user workflows
* UI-level interaction timing

---

## 📌 Conclusion

This workflow demonstrates a structured approach to performance testing by combining:

* Endpoint-level analysis
* Workflow simulation
* User experience measurement

The result is a balanced and realistic evaluation of application performance aligned with professional QA practices.

---
