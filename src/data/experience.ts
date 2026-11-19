// src/data/experience.ts
// Career history, certifications, and achievements verified against official LinkedIn profile and professional records.
// Accurately delineates employer, client assignment, and role while protecting confidential internal details.

export interface ExperienceEntry {
  employer: string;
  client?: string;
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
    client: 'Cisco Splunk',
    role: 'Senior Software Engineer — Integration & Observability',
    periodLabel: 'December 2025 – Present',
    startDate: '2025-12',
    endDate: null,
    summary:
      'Engineering enterprise observability pipelines, log analytics, and telemetry integrations on Splunk Enterprise across distributed platforms.',
    highlights: [
      'Architecting high-throughput data onboarding pipelines and Splunk Technology Add-ons (TAs) for log ingestion, indexing, and field normalization.',
      'Designing optimized SPL (Search Processing Language) queries, dashboards, and automated alert rules to maintain platform visibility and operational SLAs.',
      'Building automated Python scripts to validate forwarder and indexer health, data integrity, and telemetry performance.',
      'Collaborating with cross-functional platform teams to ensure secure, resilient telemetry pipelines and enterprise compliance.',
    ],
    technologies: [
      'Splunk Enterprise',
      'SPL',
      'Python',
      'Observability',
      'Linux',
      'REST APIs',
      'Data Pipelines',
    ],
    visibility: 'public',
    verified: true,
  },
  {
    employer: 'Cognizant',
    client: 'Verizon',
    role: 'Pega Lead & Senior System Architect',
    periodLabel: 'June 2024 – November 2025',
    startDate: '2024-06',
    endDate: '2025-11',
    summary:
      'Led enterprise Pega workflows, case management architectures, and platform guardrails on Pega Platform 8.8.3 for telecom customer onboarding.',
    highlights: [
      'Delivered 5G Fixed Wireless Access (FWA) customer onboarding, order fulfillment, and telecom billing integration workflows on Pega Platform 8.8.3.',
      'Enforced Pega design guardrails and conducted structured code reviews, ensuring compliance and maintainability.',
      'Streamlined defect triaging and backlog grooming to decrease incident resolution turnaround time by 15% and increased SLA compliance from 92% to 98%.',
      'Cross-skilled engineering teams on Agile delivery practices and Pega Dev Studio standards.',
    ],
    technologies: [
      'Pega Platform 8.8.3',
      'Case Management',
      'Queue Processors',
      'REST APIs',
      'BIX',
      'Agile',
    ],
    visibility: 'public',
    verified: true,
  },
  {
    employer: 'Cognizant',
    client: 'Google India Account',
    role: 'Pega Senior System Architect & Tools Engineer',
    periodLabel: 'March 2022 – June 2024',
    startDate: '2022-03',
    endDate: '2024-06',
    summary:
      'Delivered critical enterprise workflows on Pega Platform 8.8.3 and secure cloud integrations for internal operations.',
    highlights: [
      'Designed and maintained core case management workflows on Pega Platform 8.8.3 for high-volume operational teams.',
      'Architected secure Google Drive API integration for document attachment storage, reducing transactional database bloat.',
      'Engineered custom automation scripts and RESTful API microservices, reducing manual operational overhead across teams.',
      'Managed sprint deployment pipelines to higher environments and coordinated production cutovers.',
    ],
    technologies: [
      'Pega Platform 8.8.3',
      'Google Drive API',
      'REST APIs',
      'Python',
      'Microservices',
      'CI/CD',
    ],
    visibility: 'public',
    verified: true,
  },
  {
    employer: 'Astreya',
    client: 'Google India Account',
    role: 'Software Developer & Tools Engineer',
    periodLabel: 'November 2015 – March 2022',
    startDate: '2015-11',
    endDate: '2022-03',
    summary:
      'Over six years delivering core enterprise workflows on Pega Platform and engineering a suite of internal browser extensions and web tools for operations teams.',
    highlights: [
      'Engineered complex Pega workflows, Data Models, Activities, SLA rules, BIX extracts, and application security roles with 99.5% deployment success rate.',
      'Built Automated CSAT Application with a custom Chrome extension, email response capture, and BigQuery analytics dashboard.',
      'Designed Netco circuit integration Chrome extension using AngularJS and GCP Cloud Storage to sync network provisioning workflows.',
      'Developed operational chatbot automations using Google Apps Script and Dialogflow to streamline recurring operational queries.',
      'Authored reusable engineering components that reduced new-feature development time across teams by ~25%.',
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
      'SQL',
    ],
    visibility: 'public',
    verified: true,
  },
  {
    employer: 'Wipro Technologies',
    role: 'Software Engineer',
    periodLabel: 'December 2012 – October 2015',
    startDate: '2012-12',
    endDate: '2015-10',
    summary:
      'Early-career software engineering developing web applications, automated monitoring utilities, and proof-of-concept solutions.',
    highlights: [
      'Developed responsive UI for single-page applications using JavaScript, AngularJS, and Bootstrap, and backend tools with Python (Django, MySQL).',
      'Automated Linux system health checks, performance tracking scripts, and database maintenance routines.',
      'Reduced defect leakage by 35% through early testing automation and cut MySQL query response times by 40% via schema and index optimization.',
      'Awarded Certificate of Recognition for rapid POC prototyping; secured Rank 1 in technical training batch among 40+ engineers.',
    ],
    technologies: [
      'JavaScript',
      'HTML5',
      'CSS3',
      'Python',
      'Django',
      'MySQL',
      'Linux/Shell',
      'AngularJS',
    ],
    visibility: 'public',
    verified: true,
  },
];

export const publicExperience: ExperienceEntry[] = experience.filter((e) => e.visibility === 'public');

export const certifications: Certification[] = [
  {
    name: 'Certified Senior System Architect (CSSA 23)',
    issuer: 'Pegasystems',
    date: 'April 2024',
    status: 'active',
  },
  {
    name: 'Certified System Architect (CSA 7.2)',
    issuer: 'Pegasystems',
    date: 'February 2018',
    status: 'active',
  },
  {
    name: 'React.js & Modern Web Architecture',
    issuer: 'LinkedIn Learning',
    date: 'March 2024',
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
