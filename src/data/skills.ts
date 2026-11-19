// src/data/skills.ts
// Technical skills verified against official LinkedIn profile (Profile.pdf).

export interface Skill {
  name: string;
  level: 'professional' | 'working' | 'learning';
}

export interface SkillGroup {
  heading: string;
  skills: Skill[];
}

export const skillGroups: SkillGroup[] = [
  {
    heading: 'Integration & Observability',
    skills: [
      { name: 'REST & SOAP Microservices', level: 'professional' },
      { name: 'Splunk Observability & Log Analysis', level: 'professional' },
      { name: 'SPL Query Optimization & Field Extraction', level: 'professional' },
      { name: 'Splunk Technology Add-ons (AWS TA)', level: 'professional' },
      { name: 'System Refactoring & Performance Tuning', level: 'professional' },
    ],
  },
  {
    heading: 'Pega Architecture (CSSA)',
    skills: [
      { name: 'Pega Platform (8.8.3 / PRPC)', level: 'professional' },
      { name: 'Case Lifecycle & Microjourneys', level: 'professional' },
      { name: 'Queue Processors & Job Schedulers', level: 'professional' },
      { name: 'Data Pages & REST/SQL Connectors', level: 'professional' },
      { name: 'Enterprise Guardrails & PDC Health', level: 'professional' },
      { name: 'BIX (Business Information Exchange)', level: 'professional' },
    ],
  },
  {
    heading: 'Backend & Cloud Systems',
    skills: [
      { name: 'Python (Django, FastAPI, Scripting)', level: 'professional' },
      { name: 'AWS (EC2, S3, IAM, VPC)', level: 'working' },
      { name: 'Docker & Containerization', level: 'working' },
      { name: 'CI/CD Pipelines (Jenkins, Git)', level: 'professional' },
      { name: 'SQL (PostgreSQL, MySQL, BigQuery)', level: 'professional' },
    ],
  },
  {
    heading: 'Frontend, Extensions & Apps',
    skills: [
      { name: 'JavaScript (ES6+, DOM, OOP)', level: 'professional' },
      { name: 'Chrome Extension Development (v2/v3)', level: 'professional' },
      { name: 'HTML5 Canvas & Responsive CSS3', level: 'professional' },
      { name: 'Android Application Development', level: 'working' },
      { name: 'Google Apps Script', level: 'professional' },
    ],
  },
  {
    heading: 'AI-Assisted Engineering & Leadership',
    skills: [
      { name: 'Agentic AI Workflows (Claude Code, Codex)', level: 'professional' },
      { name: 'AI-Driven Code Reviews & Refactoring', level: 'professional' },
      { name: 'Engineering Mentorship & Best Practices', level: 'professional' },
      { name: 'Defect Triaging & SLA Governance', level: 'professional' },
      { name: 'Agile / Scrum Sprint Delivery', level: 'professional' },
    ],
  },
];
