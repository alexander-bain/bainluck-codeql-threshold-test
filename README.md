# Isolated CodeQL threshold acceptance fixture

Authorized controlled acceptance test for alexander-bain/bainluck#11092. No product source, credentials, real session data, deployment, server execution or production access. Code is analyzed statically only.

Official CodeQL v3 actions, security-and-quality query suite, Python and JavaScript/TypeScript matrix, Ubuntu runner and language categories mirror the product scanner. Product-specific compose/master qualification and deployment are intentionally absent: this tests GitHub native check-failure thresholds only.

Saved repository thresholds: Security Medium or higher; Standard Only errors. A branch changes only the synthetic session cookie Secure flag; Python rule py/insecure-cookie has security severity5.0 and ordinary severitywarning. Verify red, then restore Secure=True and verify green. Never merge an insecure fixture.
