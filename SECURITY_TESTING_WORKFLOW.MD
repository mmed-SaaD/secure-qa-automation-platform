# 🔐 Security Testing Workflow — QA Automation Project

---

## 🎯 Objective

This phase integrates security testing into a QA automation workflow by combining:

* Automated Dynamic Application Security Testing (DAST)
* Python-based orchestration
* Targeted manual vulnerability validation

The objective was not to perform a full penetration test, but to demonstrate the ability to:

* Identify vulnerabilities using automated tools
* Validate findings manually
* Analyze real impact
* Report results in a structured, professional manner

---

## 🧩 System Under Test (SUT)

* Target: OWASP Juice Shop
* Type: Deliberately vulnerable web application
* Purpose: Safe and controlled environment for security testing practice

---

## 🧰 Tools & Technologies

* OWASP ZAP (automated scanning)
* Python (scan orchestration & result extraction)
* Docker (environment setup)
* Browser DevTools (manual testing)
* Burp Suite Community Edition (request interception & manipulation)

---

## 🏗️ Workflow Overview

The security phase was executed in three main layers:

1. Automated Scanning (ZAP)
2. Analysis & Filtering (Python + manual review)
3. Manual Exploitation (targeted validation)

---

# 🟢 Phase 1 — Environment Setup

### Tasks

* Configured Docker environment
* Deployed OWASP Juice Shop locally
* Ran OWASP ZAP in daemon (headless) mode via Docker
* Verified ZAP API connectivity
* Connected Python client to ZAP API

### Deliverables

* Fully working local security testing environment
* Verified connection using `zap.core.version`

---

# 🔵 Phase 2 — Automated Security Scanning

### Tasks

* Initiated target access via ZAP
* Performed spider scan to discover endpoints
* Waited for spider completion
* Executed active scan for vulnerability detection
* Monitored scan progress
* Retrieved alerts via ZAP API

### Observations

* Large volume of alerts generated (mostly low-value)
* Many findings related to static assets and non-relevant endpoints

### Deliverables

* `zap_scan.py` script
* Raw alert dataset from ZAP
* Initial vulnerability list

---

# 🟣 Phase 3 — Analysis & Filtering

### Tasks

* Parsed alerts returned by ZAP
* Filtered out noise (static files, duplicate findings)
* Grouped vulnerabilities into meaningful categories
* Prioritized findings based on impact

### Key Insight

Automated tools produced noisy output, requiring manual analysis to extract actionable vulnerabilities.

### Final Categories Identified

* Security Misconfiguration
* Cross-Site Scripting (potential)
* Injection indicators

### Deliverables

* Cleaned vulnerability set
* Structured report (`final_report.md`)

---

# 🔴 Phase 4 — Manual Vulnerability Validation

## 🎯 Objective

Validate high-impact vulnerabilities through manual testing and confirm exploitability.

---

## 🔥 1. Cross-Site Scripting (XSS)

### Approach

* Focused on real user input points (search functionality)
* Ignored static asset endpoints flagged by scanner
* Tested multiple payload variations

### Result

* Basic payload (`<script>`) was blocked
* Alternative payload successfully executed:

  ```html
  <iframe src="javascript:alert(`xss`)">
  ```

### Outcome

* Reflected XSS confirmed
* Demonstrated weak input sanitization

---

## 💥 2. Authentication Bypass via Injection

### Approach

* Targeted login functionality
* Injected payload into username field

### Payload Used

```sql
' OR '1'='1'--
```

### Result

* Successfully bypassed authentication
* Logged in as administrative user

### Impact

* Full account takeover
* Access to sensitive user data (PII & financial information)

---

## 🔴 3. Broken Access Control (IDOR)

### Approach

* Observed API requests using Burp Suite
* Identified basket endpoint using numeric identifiers
* Modified resource identifiers manually

### Example

```http
GET /rest/basket/6   → original request  
GET /rest/basket/4   → modified request
```

### Result

* Accessed another user’s basket data
* No ownership validation enforced

### Outcome

* Confirmed Horizontal Access Control vulnerability (IDOR)

---

# 🧠 Key Learnings

* Automated scanners generate noisy results and require manual validation
* Real vulnerabilities are often found through targeted testing, not broad scanning
* Input-based attacks (Injection, XSS) require creativity and payload variation
* Access control issues require understanding application logic rather than relying on tools

---

# 🚀 Final Outcome

The workflow successfully identified and validated vulnerabilities across multiple categories:

* 🔴 Critical: Authentication Bypass via Injection
* 🔴 High: Broken Access Control (IDOR)
* 🟠 Medium: Reflected XSS
* 🟡 Low–Medium: Security Misconfiguration

---

## 📌 Conclusion

This workflow demonstrates a practical, real-world approach to integrating security testing into QA processes by combining:

* Automated scanning
* Manual validation
* Impact-driven analysis

The result is a structured and realistic security assessment aligned with professional practices.

---
