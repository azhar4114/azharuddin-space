// src/data/experience.ts
// Career history, certifications, and achievements verified against official LinkedIn profile (Profile.pdf).
// Formatted to be professional, accurate, and completely safe with respect to enterprise confidentiality.

export interface ExperienceEntry {
  employer: string;
  role: string;
  periodLabel: string;
  startDate: string; // ISO YYYY-MM
  endDate: string | null; // null = current
  summary: string;
  highlights: string[];
  technologies: string[];
  visibility: 'public' | 'private';
  verified: boolean;
}

export interface Certification {
  name: string;
  issuer: string;
  date: string;
  status: 'active' | 'in-progress';
}

export interface EducationEntry {
  degree: string;
  institution: string;
  university: string;
  year: string;
  score?: string;
}

export interface AwardEntry {
  title: string;
  organization: string;
  description: string;
}

export const experience: ExperienceEntry[] = [
  {
    employer: 'Cognizant',
    role: 'Lead Integration Architect & Pega Senior System Architect',
    periodLabel: 'March 2022 – Present',
    startDate: '2022-03',
    endDate: null,
    summary:
      'Directing enterprise integration architecture, observability systems (Splunk), and Pega Platform (8.8.3) workflow engineering across tier-1 enterprise accounts.',
    highlights: [
      'Architected robust RESTful microservices and Python-based automated data pipelines supporting high-throughput enterprise data onboarding.',
      'Lead BPM and case-management architecture on Pega Platform 8.8.3, establishing enterprise guardrails and standardizing Dev Studio patterns.',
      'Optimized observability and log analytics using Splunk (Technology Add-ons, SPL query tuning, indexer/search head monitoring).',
      'Early adopter of Agentic AI tools (Claude Code, OpenAI Codex) into engineering workflows, accelerating architecture reviews and unit testing.',
      'Mentored and coached junior and mid-level developers, conducting structured code reviews and driving CI/CD automation best practices.',
      'Key Measurable Outcomes: Reduced defect resolution turnaround by 15%, improved SLA compliance from 92% to 98%, increased straight-through processing by 22%, and raised team velocity by 18% over two quarters.'
    ],
    technologies: [
      'Pega 8.8.3 / PRPC',
      'Python',
      'Splunk (SPL)',
      'RESTful Microservices',
      'AWS (EC2, S3, IAM)',
      'Docker',
      'Agentic AI Workflows',
      'CI/CD'
    ],
    visibility: 'public',
    verified: true,
  },
  {
    employer: 'Astreya',
    role: 'Software Developer & Tools Engineer (Google Account)',
    periodLabel: 'November 2015 – March 2022',
    startDate: '2015-11',
    endDate: '2022-03',
    summary:
      'Over six years delivering core enterprise workflows on Pega Platform and engineering a suite of internal browser extensions and web tools for operations teams.',
    highlights: [
      'Delivered features, complex case lifecycles, and bug fixes on Pega Platform; coordinated multi-environment releases with 99.5% deployment success rate.',
      'Architected Google Drive integration for secure attachment storage, cutting transactional database bloat and streamlining document lifecycles.',
      'Designed and deployed an internal productivity tools suite: Automated CSAT application with email response capture, Netco circuit syncing extension, and Advanced Search tool with BigQuery backend.',
      'Developed an interactive operational chatbot using Google Apps Script and Dialogflow to automate recurring support queries.',
      'Engineered Python automation scripts and test utilities that eliminated 20+ hours/week of manual processing and shortened average case lifecycle by 2.5 days.',
      'Authored 15+ reusable engineering components that reduced new-feature development time across teams by ~25%.'
    ],
    technologies: [
      'Pega PRPC',
      'JavaScript (ES6+)',
      'Chrome Extensions API',
      'Google Apps Script',
      'BigQuery',
      'GCP',
      'Python',
      'AngularJS',
      'SQL'
    ],
    visibility: 'public',
    verified: true,
  },
  {
    employer: 'Wipro Technologies',
    role: 'Software Developer & Engineer',
    periodLabel: 'December 2012 – October 2015',
    startDate: '2012-12',
    endDate: '2015-10',
    summary:
      'Early-career software engineering developing web applications, automated monitoring utilities, and proof-of-concept solutions.',
    highlights: [
      'Developed responsive UI for single-page applications using JavaScript, AngularJS, and Bootstrap, and backend tools with Python (Django, MySQL).',
      'Automated Linux system health checks, performance tracking scripts, and database maintenance routines.',
      'Reduced defect leakage by 35% through early testing automation and cut MySQL query response times by 40% via schema and index optimization.',
      'Secured First Place in training batch among 40+ engineering peers; awarded Certificate of Recognition for rapid technology adoption and POC development.'
    ],
    technologies: ['JavaScript', 'HTML5', 'CSS3', 'Python', 'Django', 'MySQL', 'Linux/Shell', 'AngularJS'],
    visibility: 'public',
    verified: true,
  },
];

export const certifications: Certification[] = [
  {
    name: 'Certified Senior System Architect (CSSA)',
    issuer: 'Pegasystems',
    date: 'Certified',
    status: 'active',
  },
  {
    name: 'Certified System Architect (CSA)',
    issuer: 'Pegasystems',
    date: 'Certified',
    status: 'active',
  },
  {
    name: 'React.js & Modern Web Architecture',
    issuer: 'LinkedIn Learning',
    date: 'Certified',
    status: 'active',
  },
  {
    name: 'Pega Lead System Architect (LSA)',
    issuer: 'Pegasystems',
    date: 'In Progress',
    status: 'in-progress',
  },
];

export const education: EducationEntry[] = [
  {
    degree: 'Bachelor of Engineering (B.E.), Electrical, Electronics & Communications Engineering',
    institution: 'MJ College of Engineering & Technology',
    university: 'Osmania University, Hyderabad',
    year: '2008 – 2012',
    score: 'First Class with Distinction',
  },
];

export const awards: AwardEntry[] = [
  {
    title: 'Top Performer in Training',
    organization: 'Wipro Technologies',
    description: 'Secured first rank in training batch among 40+ engineering peers.',
  },
  {
    title: 'Certificate of Recognition',
    organization: 'Wipro Technologies',
    description: 'Recognized for innovation, rapid learning of emerging technologies, and high-impact POC development.',
  },
];

export const publicExperience = experience.filter(
  (e) => e.visibility === 'public'
);
