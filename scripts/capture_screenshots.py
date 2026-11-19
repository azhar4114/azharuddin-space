#!/usr/bin/env python3
"""
scripts/capture_screenshots.py
Captures desktop and mobile screenshots for all routes using Chromium.
"""
import os
import subprocess
import time

ROUTES = [
    ('/', '01_home'),
    ('/about', '02_about'),
    ('/experience', '03_experience'),
    ('/services', '04_services'),
    ('/contact', '05_contact'),
    ('/resume', '06_resume'),
    ('/lab', '07_lab'),
    ('/projects', '08_projects'),
    ('/projects/aforapple', '09_proj_aforapple'),
    ('/projects/agla-owner', '10_proj_agla_owner'),
    ('/projects/ai-crm', '11_proj_ai_crm'),
    ('/projects/chrome-extensions-automation', '12_proj_chrome_ext'),
    ('/projects/cloud-integration-engineering', '13_proj_cloud_integ'),
    ('/projects/enterprise-workflow-engineering', '14_proj_enterprise_wf'),
    ('/writing', '15_writing'),
    ('/writing/event-driven-integration-patterns', '16_writing_event_driven'),
    ('/writing/practical-browser-extensions-enterprise', '17_writing_browser_ext'),
    ('/writing/reliable-api-retry-mechanisms', '18_writing_api_retry'),
]

OUT_DIR = '/home/azhar41141/azharuddin-space/screenshots'
os.makedirs(OUT_DIR, exist_ok=True)

def capture(url, out_path, width=1280, height=1400):
    cmd = [
        'chromium',
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        f'--window-size={width},{height}',
        f'--screenshot={out_path}',
        '--hide-scrollbars',
        url
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)

def main():
    base_url = 'http://127.0.0.1:4321'
    print(f'Starting screenshot capture of {len(ROUTES)} routes...')
    for path, name in ROUTES:
        desktop_img = os.path.join(OUT_DIR, f'{name}_desktop.png')
        url = f'{base_url}{path}'
        print(f'Capturing {path} -> {name}_desktop.png')
        capture(url, desktop_img, width=1280, height=1400)
    
    # Also capture mobile for key pages (Home, About, Lab, Contact)
    mobile_pages = [('/', '01_home_mobile'), ('/about', '02_about_mobile'), ('/lab', '07_lab_mobile'), ('/contact', '05_contact_mobile')]
    for path, name in mobile_pages:
        mobile_img = os.path.join(OUT_DIR, f'{name}.png')
        url = f'{base_url}{path}'
        print(f'Capturing mobile {path} -> {name}.png')
        capture(url, mobile_img, width=390, height=844)

    print('All screenshots captured!')

if __name__ == '__main__':
    main()
