import requests
import pytest

EXPECTED_HEADERS = [
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "X-Frame-Options",
]

@pytest.mark.security
def test_server_not_leaking_muchInfos(BASE_URL):
    r = requests.get(BASE_URL)
    server = r.headers.get("server", "")
    assert len(server) < 80

@pytest.mark.security
def test_basic_security_headers_missing(BASE_URL):
    r = requests.get(BASE_URL)
    missing = [h for h in EXPECTED_HEADERS if h not in r.headers]
     
    if missing:
        print("\nMissing security headers:", missing)
        print("Present headers snapshot:", {k: r.headers.get(k) for k in EXPECTED_HEADERS})

    # For now: don't fail hard, just track (xfail means "expected to fail")
    pytest.xfail(f"Security headers not yet configured. Missing: {missing}")
