🟢 AUTOMATED (ZAP — Coverage Layer)

👉 These come from OWASP ZAP

You are NOT exploiting them manually
You are analyzing + classifying them

✅ 1. Security Misconfiguration (MUST)
Missing security headers
X-Frame-Options
Content-Security-Policy
X-Content-Type-Options

👉 Why:

always detected
easy to explain
shows understanding of web security basics
✅ 2. Information Disclosure
Server info
technology leaks
verbose responses

👉 Why:

very common in real apps
easy to connect to risk
✅ 3. Cross-Site Scripting (XSS Indicators)
reflected or stored alerts from ZAP

👉 Your role:

verify if exploitable or false positive

👉 Why:

shows you can think beyond scanner output
✅ 4. Cookie / Session Issues
missing HttpOnly
missing Secure flag

👉 Why:

very relevant in real-world apps
✅ 5. General Low/Medium Alerts
directory browsing
cache issues
minor misconfigs

👉 Why:

shows you can filter noise

👉 That’s your automated layer = breadth

🔴 MANUAL (YOUR SIGNATURE — Depth Layer)

👉 These are your 3 core vulnerabilities

🔥 1. Broken Access Control (MANDATORY)
What you test:
access other users' data
change IDs in requests (IDOR)
bypass restrictions
Why this is #1:
most critical real-world vulnerability
highly valued by clients
shows deep understanding
🔥 2. Injection (SQL / NoSQL)
What you test:
login inputs
search fields
API payloads
Why:
classic but still powerful
easy to demonstrate clearly
🔥 3. API Abuse / Authentication Weakness
What you test:
direct API calls
bypass frontend validation
token/session misuse
Why:
modern apps = API-driven
shows advanced thinking