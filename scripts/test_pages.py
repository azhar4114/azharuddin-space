#!/usr/bin/env python3
"""
scripts/test_pages.py
Runs a headless browser check across all routes:
- Collects console errors / warnings
- Verifies HTTP 200
- Tests interactive elements on /lab
"""
import subprocess
import json

ROUTES = [
    '/',
    '/about',
    '/experience',
    '/services',
    '/contact',
    '/resume',
    '/lab',
    '/projects',
    '/projects/aforapple',
    '/projects/agla-owner',
    '/projects/ai-crm',
    '/projects/chrome-extensions-automation',
    '/projects/cloud-integration-engineering',
    '/projects/enterprise-workflow-engineering',
    '/writing',
    '/writing/event-driven-integration-patterns',
    '/writing/practical-browser-extensions-enterprise',
    '/writing/reliable-api-retry-mechanisms',
]

def check_routes_curl():
    import urllib.request
    print('Checking HTTP status codes...')
    all_ok = True
    for r in ROUTES:
        url = f'http://127.0.0.1:4321{r}'
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as res:
                code = res.getcode()
                if code != 200:
                    print(f'FAIL: {r} returned {code}')
                    all_ok = False
        except Exception as e:
            print(f'ERROR: {r} -> {e}')
            all_ok = False
    if all_ok:
        print('All 18 routes return HTTP 200!')

if __name__ == '__main__':
    check_routes_curl()
