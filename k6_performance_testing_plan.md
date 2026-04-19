# k6 Performance Testing — Mastery Plan
> Complete this checklist before confidently saying: *"I do performance testing."*

---

## 🧭 Overview

| Stage | Focus | Goal |
|-------|-------|------|
| 1 | Setup & Fundamentals | Write and run your first k6 test |
| 2 | Core Test Types | Cover the 4 main performance test scenarios |
| 3 | Assertions & Thresholds | Make tests pass/fail with real criteria |
| 4 | CI/CD Integration | Run k6 in GitHub Actions automatically |
| 5 | Reporting & Observability | Visualize results with Grafana |
| 6 | Advanced Scenarios | Real-world patterns that impress clients |
| 7 | Portfolio Polish | What you ship to GitHub and show in interviews |

---

## Stage 1 — Setup & Fundamentals

- [ ] Install k6 locally (`brew install k6` / `choco install k6` / Linux apt)
- [ ] Understand the k6 execution model: **VUs (Virtual Users)** vs iterations vs duration
- [ ] Write a minimal smoke test against a public API (e.g. `https://jsonplaceholder.typicode.com`)
- [ ] Learn the test lifecycle: `init` → `setup()` → `default fn` → `teardown()`
- [ ] Run your first test: `k6 run script.js`
- [ ] Read and understand the default CLI output:
  - `http_req_duration` (p50, p90, p95, p99)
  - `http_req_failed`
  - `iterations` and `vus`
- [ ] Use `--vus` and `--duration` flags to override options at runtime
- [ ] Organize your repo: `tests/performance/` folder structure

---

## Stage 2 — Core Test Types

Each test type has a distinct shape. Implement all four.

### 2.1 Smoke Test
- [ ] Run with 1–2 VUs for a short duration (30s)
- [ ] Goal: verify the script works and the system isn't broken at baseline
- [ ] Used as a pre-gate before heavier tests

### 2.2 Load Test
- [ ] Simulate expected production traffic (e.g. 50 VUs over 5 minutes)
- [ ] Use `stages` to ramp up → hold → ramp down
```js
stages: [
  { duration: '1m', target: 50 },
  { duration: '3m', target: 50 },
  { duration: '1m', target: 0 },
]
```
- [ ] Identify p95 response time at normal load

### 2.3 Stress Test
- [ ] Push beyond expected limits (e.g. ramp up to 200+ VUs)
- [ ] Goal: find the **breaking point** of your system
- [ ] Document at what VU count errors appear or latency spikes

### 2.4 Soak Test (Endurance Test)
- [ ] Run at moderate load for a long duration (30–60 min)
- [ ] Goal: detect **memory leaks**, connection pool exhaustion, degradation over time
- [ ] Note: you don't need to wait 60 min in dev — 10–15 min is enough to demonstrate understanding

---

## Stage 3 — Assertions & Thresholds

- [ ] Use `check()` to assert individual responses:
```js
check(res, {
  'status is 200': (r) => r.status === 200,
  'response time < 500ms': (r) => r.timings.duration < 500,
});
```
- [ ] Use `thresholds` in options to define pass/fail criteria:
```js
thresholds: {
  http_req_duration: ['p(95)<500'],
  http_req_failed: ['rate<0.01'],
}
```
- [ ] Understand that **failed thresholds = non-zero exit code** (critical for CI)
- [ ] Test a failing threshold intentionally to see the behavior
- [ ] Use `abortOnFail: true` to stop a test early when a threshold is breached

---

## Stage 4 — CI/CD Integration (GitHub Actions)

- [ ] Create `.github/workflows/performance.yml`
- [ ] Trigger the workflow:
  - On push to `main`
  - On pull requests
  - On a manual `workflow_dispatch`
- [ ] Run a smoke test on every PR (fast, cheap)
- [ ] Run a full load test on merge to `main` or on a schedule
- [ ] Capture k6 output and surface threshold failures as pipeline failures
- [ ] Store the JSON results as a GitHub Actions artifact:
```yaml
- name: Upload k6 results
  uses: actions/upload-artifact@v3
  with:
    name: k6-results
    path: results.json
```
- [ ] (Optional) Post a summary comment to the PR using the results

---

## Stage 5 — Reporting & Observability

- [ ] Output results to JSON: `k6 run --out json=results.json script.js`
- [ ] Generate the built-in HTML report (k6 v0.44+):
```js
import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";
export function handleSummary(data) {
  return { "summary.html": htmlReport(data) };
}
```
- [ ] Understand what each metric means in the report
- [ ] (Bonus — portfolio standout) Set up **Grafana + InfluxDB** locally with Docker Compose:
  - Run k6 and stream metrics: `k6 run --out influxdb=http://localhost:8086/k6 script.js`
  - Import the official k6 Grafana dashboard (ID: 2587)
  - Take a screenshot for your README

---

## Stage 6 — Advanced Scenarios

These separate junior from mid/senior in interviews and freelance proposals.

- [ ] **Parameterize data** — load user data from a CSV file using `SharedArray`:
```js
import { SharedArray } from 'k6/data';
const users = new SharedArray('users', () => {
  return JSON.parse(open('./data/users.json'));
});
```
- [ ] **Authenticated requests** — handle login flow, store token, use in subsequent requests
- [ ] **Groups** — wrap related requests in `group()` for better reporting
- [ ] **Custom metrics** — define a `Trend`, `Counter`, or `Rate` metric for business logic:
```js
import { Trend } from 'k6/metrics';
const checkoutDuration = new Trend('checkout_duration');
checkoutDuration.add(res.timings.duration);
```
- [ ] **Environment variables** — use `__ENV.BASE_URL` so the same script targets dev/staging/prod
- [ ] **Scenarios** — define multiple independent workloads in one script (different executor types):
  - `constant-vus`
  - `ramping-vus`
  - `constant-arrival-rate`
- [ ] **Browser testing** (k6 browser module) — run a basic Chromium-based test to measure frontend performance

---

## Stage 7 — Portfolio Polish

What your GitHub repo should show before you claim performance testing on your profile.

### Repository Structure
```
tests/
  performance/
    smoke.test.js
    load.test.js
    stress.test.js
    soak.test.js
    scenarios/
      authenticated_flow.js
      checkout_flow.js
    data/
      users.csv
    utils/
      auth.js
      thresholds.js
.github/
  workflows/
    performance.yml
```

### README Section for Performance Testing
- [ ] Write a dedicated `## Performance Testing` section in your project README
- [ ] Explain what each test type does and when to run it
- [ ] Include a screenshot of Grafana dashboard OR the HTML report output
- [ ] Show the GitHub Actions badge (passing)
- [ ] Document what thresholds you set and why

### Talking Points (for interviews and freelance pitches)
- [ ] You can explain the difference between load, stress, and soak testing
- [ ] You can explain what p95 latency means and why it matters more than average
- [ ] You can explain how thresholds create a CI quality gate
- [ ] You can explain VU-based (closed model) vs arrival-rate (open model) testing

---

## ✅ Done When...

You can say *"I do performance testing"* when:

1. Your GitHub repo has all 4 test types with working scripts
2. GitHub Actions runs them automatically and fails the pipeline on threshold breach
3. Results are exported and stored as artifacts
4. Your README shows visual evidence (Grafana screenshot or HTML report)
5. You can comfortably explain every metric and decision to a client or interviewer

---

*Tool: [k6 by Grafana Labs](https://k6.io) | Docs: https://grafana.com/docs/k6/latest/*
