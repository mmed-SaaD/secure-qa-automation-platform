🔐 Security Testing Workflow — QA Automation Project
🎯 Objective

This phase aims to integrate security testing into a QA automation workflow by combining:

Automated Dynamic Application Security Testing (DAST)
Python-based orchestration
Targeted manual vulnerability validation

The goal is not full penetration testing, but to demonstrate the ability to:

identify vulnerabilities using professional tools
validate critical findings
report them in a structured, business-oriented manner
🧩 System Under Test (SUT)
Target: OWASP Juice Shop
Type: Deliberately vulnerable web application
Purpose: Safe and controlled environment for practicing security testing
🧰 Tools & Technologies
OWASP ZAP (DAST scanner)
Python (automation and reporting)
Docker (environment setup)
Browser (manual validation)

Optional:

Burp Suite Community Edition (manual request manipulation)
🏗️ Workflow Overview

The security phase is divided into three main layers:

Automated Scanning
Python-Orchestrated Analysis
Manual Vulnerability Validation
🟢 Phase 1 — Environment Setup
Tasks

Install and configure Docker

Run OWASP Juice Shop container

Run OWASP ZAP in daemon (headless) mode

Verify ZAP API accessibility

Connect Python client to ZAP API

Deliverables
Working local environment
Verified API connectivity (zap.core.version)
🔵 Phase 2 — Automated Security Scanning
Tasks

Trigger target access via ZAP

Perform spider scan (endpoint discovery)

Wait for spider completion

Perform active scan (vulnerability detection)

Monitor scan progress

Retrieve alerts from ZAP

Deliverables
Script: zap_scan.py
Console output of scan progress
Raw vulnerability data
🟣 Phase 3 — Data Processing & Reporting
Tasks

Extract alerts from ZAP API

Structure results (JSON format)

Classify findings by risk level:

High
Medium
Low

Filter out noise / irrelevant alerts

Generate structured report

Deliverables
zap_report.json
final_report.md
🔴 Phase 4 — Manual Vulnerability Validation
Objective

Validate high-value vulnerabilities identified during automated scanning.

Scope (limited and focused)

Select 2–3 vulnerabilities maximum, such as:

Broken Access Control
Injection (SQL/NoSQL)
Authentication / Session weaknesses
Tasks

For each vulnerability:

Identify endpoint from scan results

Reproduce the issue manually

Capture request and response

Analyze exploitability

Evaluate impact

Suggest remediation