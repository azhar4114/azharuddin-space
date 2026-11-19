#!/usr/bin/env python3
"""
scripts/generate_resume.py
Generates the executive one-page / two-page PDF resume for Mohammad Azharuddin.
Clean, professional, compliant with corporate workplace safety:
- NO 'Founder' or commercial entity claims
- Accurate start date: 'Enterprise engineering experience since December 2012'
- Verified contact details and career history
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

    # 0.5 inch margins (36 pt)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
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
        fontSize=18,
        leading=22,
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
        fontSize=10,
        leading=13,
        textColor=primary_color,
        spaceAfter=3,
        spaceBefore=6
    )

    role_style = ParagraphStyle(
        'RoleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=primary_color
    )

    role_meta = ParagraphStyle(
        'RoleMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=accent_color,
        alignment=TA_RIGHT
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=text_color
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=text_color,
        leftIndent=10,
        firstLineIndent=-6,
        spaceAfter=1.5
    )

    story = []

    # Header
    story.append(Paragraph('MOHAMMAD AZHARUDDIN', name_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph('Lead Integration Architect &amp; Pega Senior System Architect (CSSA) | Python &amp; Observability', title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph('Hyderabad, India &nbsp;|&nbsp; azhar4114@gmail.com &nbsp;|&nbsp; linkedin.com/in/azhar4114 &nbsp;|&nbsp; azharuddin.space', contact_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width='100%', thickness=1, color=light_border, spaceBefore=2, spaceAfter=4))

    # Professional Summary
    story.append(Paragraph('PROFESSIONAL SUMMARY', section_heading))
    story.append(Paragraph(
        'Certified Pega Senior System Architect (CSSA) and Lead Integration Architect with enterprise software engineering experience since December 2012. Specializes in Pega Platform (8.8.3), enterprise integration architectures, observability systems (Splunk), and Python backend microservices across tier-1 enterprises. Proven track record in case management, RESTful microservices, Google Cloud integrations, developer automation tooling, and asynchronous queue processing.',
        body_style
    ))
    story.append(Spacer(1, 4))

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
    cert_edu_table = Table(cert_edu_data, colWidths=[270, 270])
    cert_edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(cert_edu_table)
    story.append(Spacer(1, 4))

    # Technical Skills
    story.append(Paragraph('TECHNICAL SKILLS', section_heading))
    skills_text = (
        '<b>Pega Platform:</b> Pega 8.8.3, Case Management, Data Pages, Process Flows, Queue Processors, Job Schedulers, BIX, PDC, Guardrails Governance<br/>'
        '<b>Languages &amp; Web:</b> Python (FastAPI, Flask, Pandas, openpyxl), JavaScript (ES6+), TypeScript, React, HTML5, CSS3, Google Apps Script, SQL<br/>'
        '<b>Observability &amp; Cloud:</b> Splunk Enterprise (SPL, TAs, Dashboards), Google Cloud Platform (GCP), BigQuery, Google Drive APIs, REST APIs<br/>'
        '<b>Tooling &amp; Systems:</b> Chrome Extensions (Manifest v2/v3), Android Apps, Smart TV UI, Git, Jenkins, JIRA, Linux'
    )
    story.append(Paragraph(skills_text, body_style))
    story.append(Spacer(1, 4))

    # Professional Experience
    story.append(Paragraph('PROFESSIONAL EXPERIENCE', section_heading))

    def add_role(role, company, period, bullets):
        header_table = Table([
            [Paragraph(f'<b>{role}</b> — <i>{company}</i>', role_style), Paragraph(period, role_meta)]
        ], colWidths=[400, 140])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 1.5))
        for b in bullets:
            story.append(Paragraph(f'• {b}', bullet_style))
        story.append(Spacer(1, 3))

    add_role(
        'Lead Integration Architect &amp; Pega Lead', 'Cognizant', 'Jun 2024 – Present',
        [
            'Lead engineering teams in architecting enterprise Pega workflows, enforcing design guardrails, and conducting rigorous code reviews.',
            'Streamlined defect triaging and backlog grooming to decrease incident resolution turnaround time by 15% and increased SLA compliance from 92% to 98%.',
            'Architected 5G Fixed Wireless Access (FWA) features for customer onboarding, order orchestration, and telecom billing integration.',
            'Championed cross-skilling across Agile engineering and Pega best practices, ensuring 100% on-schedule sprint delivery.'
        ]
    )

    add_role(
        'Pega Senior System Architect (SSA)', 'Cognizant', 'Mar 2022 – Jun 2024',
        [
            'Designed, delivered, and maintained critical enterprise workflows on Pega Platform 8.8.3 for high-volume enterprise operations.',
            'Architected secure Google Drive API integration for document attachment storage, streamlining file lifecycle compliance.',
            'Engineered custom automation scripts and RESTful API microservices, reducing manual operational overhead across teams.',
            'Managed sprint deployment pipelines to higher environments and coordinated production releases with cross-functional teams.'
        ]
    )

    add_role(
        'Software Developer — Pega &amp; Tooling', 'Astreya', 'Nov 2015 – Feb 2022',
        [
            'Engineered complex Pega workflows, Data Models, Activities, SLA rules, BIX extracts, and application security roles.',
            'Developed operational chatbot automations using Google Apps Script and Dialogflow to streamline recurring support workflows.',
            'Built Automated CSAT Application with a custom Chrome extension and BigQuery dashboard for feedback capture and analytics.',
            'Designed Netco integration Chrome extension using AngularJS and GCP Cloud Storage to sync network provisioning circuits.'
        ]
    )

    add_role(
        'Software Engineer', 'Wipro Technologies', 'Dec 2012 – Oct 2015',
        [
            'Developed web applications and internal tools with JavaScript, HTML, CSS, and XML; engineered with Python, Django, and Unix shell scripting.',
            'Awarded Certificate of Recognition for rapid POC prototyping; secured Rank 1 in technical training batch among 40+ engineers.'
        ]
    )

    # Key Engineering Projects
    story.append(Paragraph('KEY ENGINEERING &amp; TOOLING PROJECTS', section_heading))
    story.append(Paragraph(
        '• <b>aforapple.fun:</b> Interactive educational web application and companion Android tool featuring canvas letter tracing, phonics, and quizzes optimized for Smart TVs (D-pad remote mapping) and touch devices. Built with JavaScript, HTML5 Canvas, and Google Apps Script serverless backend.<br/>'
        '• <b>Enterprise Browser Extension &amp; Automation Suite:</b> Custom extensions and internal tools (CSAT response capture, Netco circuit syncing, multi-field search engine) deployed across operational engineering teams.<br/>'
        '• <b>AI-Assisted CRM Platform:</b> Full-stack platform featuring decoupled FastAPI backend, React/TypeScript frontend, multi-provider LLM integrations (Gemini, OpenAI), and spreadsheet bulk ingestion.',
        body_style
    ))

    doc.build(story)
    print(f'Successfully generated: {pdf_path}')

if __name__ == '__main__':
    generate_pdf()
