#!/usr/bin/env python3
"""
scripts/generate_resume.py
Generates the executive PDF resume for Mohammad Azharuddin.
Clean, professional, compliant with corporate workplace safety:
- NO 'Founder' or commercial entity claims
- Accurate start date: 'Enterprise engineering experience since December 2012'
- Verified contact details, client assignments, and career history
- Consistent positioning: Senior Software Engineer | Integration & Observability | Pega CSSA
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def generate_pdf():
    pdf_path = os.path.abspath('public/resume/Mohammad_Azharuddin_Resume.pdf')
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    # 0.45 inch margins (32 pt)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=32,
        rightMargin=32,
        topMargin=28,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()

    primary_color = colors.HexColor('#10141D')
    accent_color = colors.HexColor('#1E40AF')
    text_color = colors.HexColor('#1F2937')
    muted_color = colors.HexColor('#4B5563')
    light_border = colors.HexColor('#E5E7EB')

    name_style = ParagraphStyle(
        'DocName',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=primary_color,
        alignment=TA_CENTER
    )

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=accent_color,
        alignment=TA_CENTER
    )

    contact_style = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=muted_color,
        alignment=TA_CENTER
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=primary_color,
        spaceAfter=2,
        spaceBefore=5
    )

    role_style = ParagraphStyle(
        'RoleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=primary_color
    )

    role_meta = ParagraphStyle(
        'RoleMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11.5,
        textColor=accent_color,
        alignment=TA_RIGHT
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=text_color
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=text_color,
        leftIndent=9,
        firstLineIndent=-5,
        spaceAfter=1.2
    )

    story = []

    # Header
    story.append(Paragraph('MOHAMMAD AZHARUDDIN', name_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph('Senior Software Engineer | Integration &amp; Observability | Pega CSSA', title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph('Hyderabad, India &nbsp;|&nbsp; azhar4114@gmail.com &nbsp;|&nbsp; linkedin.com/in/azhar4114 &nbsp;|&nbsp; azharuddin.space', contact_style))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width='100%', thickness=1, color=light_border, spaceBefore=2, spaceAfter=3))

    # Professional Summary
    story.append(Paragraph('PROFESSIONAL SUMMARY', section_heading))
    story.append(Paragraph(
        'Certified Pega Senior System Architect (CSSA) and Senior Software Engineer with over 12 years of enterprise engineering experience (since December 2012). Specializes in enterprise observability systems (Splunk), resilient integration architectures, Pega Platform workflow automation (8.8.3), and Python backend microservices across tier-1 telecom and technology environments. Proven track record in data onboarding pipelines, RESTful microservices, asynchronous queue processing, and developer productivity tooling.',
        body_style
    ))
    story.append(Spacer(1, 3))

    # Certifications & Education (2 columns)
    cert_edu_data = [
        [
            Paragraph('<b>CERTIFICATIONS</b>', section_heading),
            Paragraph('<b>EDUCATION</b>', section_heading)
        ],
        [
            Paragraph('• <b>Certified Pega Senior System Architect (CSSA 23)</b> — Apr 2024<br/>• <b>Pega Certified System Architect (CSA 7.2)</b> — Feb 2018<br/>• <i>Lead System Architect (LSA)</i> — In Progress', body_style),
            Paragraph('• <b>B.E. in Electronics &amp; Communication Engineering</b> (78.5%)<br/>&nbsp;&nbsp;MJ College of Engineering &amp; Tech, Osmania University, 2012<br/>• <b>Top Performer Award</b> — Wipro Training Batch (Rank 1 / 40+)', body_style)
        ]
    ]
    cert_edu_table = Table(cert_edu_data, colWidths=[274, 274])
    cert_edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(cert_edu_table)
    story.append(Spacer(1, 3))

    # Technical Skills
    story.append(Paragraph('TECHNICAL SKILLS', section_heading))
    skills_text = (
        '<b>Pega Platform:</b> Pega 8.8.3, Case Lifecycle Management, Data Pages, Process Flows, Queue Processors, Job Schedulers, BIX, PDC, Guardrails (90+)<br/>'
        '<b>Observability &amp; Data:</b> Splunk Enterprise / Cloud (SPL Tuning, Technology Add-ons, Dashboards), Google Cloud Platform (GCP), BigQuery, SQL<br/>'
        '<b>Languages &amp; Backend:</b> Python (FastAPI, Flask, Pandas, openpyxl), JavaScript (ES6+), TypeScript, React, HTML5, CSS3, Google Apps Script<br/>'
        '<b>APIs &amp; Tooling:</b> REST / SOAP Services, OAuth 2.0, Chrome Extensions (Manifest v2/v3), Android Apps, Git, Jenkins, JIRA, Linux'
    )
    story.append(Paragraph(skills_text, body_style))
    story.append(Spacer(1, 3))

    # Professional Experience
    story.append(Paragraph('PROFESSIONAL EXPERIENCE', section_heading))

    def add_role(role, company, period, bullets):
        header_table = Table([
            [Paragraph(f'<b>{role}</b> — <i>{company}</i>', role_style), Paragraph(period, role_meta)]
        ], colWidths=[408, 140])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 1))
        for b in bullets:
            story.append(Paragraph(f'• {b}', bullet_style))
        story.append(Spacer(1, 2.5))

    add_role(
        'Senior Software Engineer (Client: Cisco Splunk)', 'Cognizant', 'Dec 2025 – Present',
        [
            'Engineer and optimize enterprise observability pipelines, log analytics, and telemetry monitoring workflows.',
            'Configure and validate Splunk Technology Add-on (TA) data onboarding pipelines for high-throughput log ingestion.',
            'Tune complex SPL queries and operational dashboards to ensure rapid incident triage and SLA adherence.'
        ]
    )

    add_role(
        'Lead Integration Architect &amp; Pega Lead (Client: Verizon)', 'Cognizant', 'Jun 2024 – Nov 2025',
        [
            'Led engineering delivery for enterprise workflow automation on Pega Platform 8.8.3, enforcing strict design guardrails and code reviews.',
            'Streamlined defect triaging and backlog grooming to decrease turnaround time by 15% and increase SLA compliance from 92% to 98%.',
            'Architected 5G Fixed Wireless Access (FWA) customer onboarding, order orchestration, and telecom billing integration workflows.',
            'Conducted technical cross-skilling across Agile engineering best practices, ensuring consistent on-schedule sprint delivery.'
        ]
    )

    add_role(
        'Pega Senior System Architect (Client: Google India Account)', 'Cognizant', 'Mar 2022 – Jun 2024',
        [
            'Engineered and maintained high-volume case lifecycles on Pega Platform 8.8.3 with asynchronous Queue Processors.',
            'Architected secure Google Drive API integration for document attachment offloading, streamlining compliance and storage.',
            'Built automated Python utilities and RESTful connectors, reducing manual operational overhead across teams.'
        ]
    )

    add_role(
        'Software Developer — Pega &amp; Tooling (Client: Google India Account)', 'Astreya', 'Nov 2015 – Mar 2022',
        [
            'Developed Pega workflows, Data Pages, Activities, SLA rules, BIX extracts, and role-based access control (RBAC).',
            'Built an automated CSAT application with a custom Manifest v2 Chrome extension and BigQuery dashboard for feedback capture.',
            'Engineered the Netco integration Chrome extension with AngularJS and GCP Cloud Storage to sync network provisioning circuits.'
        ]
    )

    add_role(
        'Software Engineer', 'Wipro Technologies', 'Dec 2012 – Oct 2015',
        [
            'Developed web applications and internal tools with JavaScript, HTML, CSS, and XML; automated pipelines using Python and Unix shell scripting.',
            'Awarded Certificate of Recognition for rapid POC prototyping; secured Rank 1 in technical training batch among 40+ engineers.'
        ]
    )

    # Key Engineering Projects
    story.append(Paragraph('KEY ENGINEERING &amp; INDEPENDENT PROJECTS', section_heading))
    story.append(Paragraph(
        '• <b>aforapple.fun:</b> Independent educational web application and companion Android tool featuring canvas letter tracing, phonics, and quizzes optimized for Smart TVs (D-pad remote navigation) and touch devices. Built with JavaScript, HTML5 Canvas, and Google Apps Script.<br/>'
        '• <b>AI CRM Prototype:</b> Full-stack architecture exploration featuring decoupled FastAPI backend, React/TypeScript frontend, multi-provider LLM integrations (Gemini, OpenAI), and spreadsheet bulk ingestion.<br/>'
        '• <b>Enterprise Browser Automation Suite:</b> Custom extensions and internal tools (CSAT response capture, circuit sync, multi-field search engine) deployed across operational engineering teams.',
        body_style
    ))

    doc.build(story)
    print(f'Successfully generated: {pdf_path}')

if __name__ == '__main__':
    generate_pdf()
