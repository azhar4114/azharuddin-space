// src/data/navigation.ts

export interface NavLink {
  label: string;
  href: string;
}

export const navLinks: NavLink[] = [
  { label: 'About', href: '/about' },
  { label: 'Experience', href: '/experience' },
  { label: 'Projects', href: '/projects' },
  { label: 'Writing', href: '/writing' },
  { label: 'Lab', href: '/lab' },
  { label: 'Capabilities', href: '/services' },
  { label: 'Contact', href: '/contact' },
];

export const footerLinks = [
  {
    heading: 'Engineering',
    links: [
      { label: 'Projects', href: '/projects' },
      { label: 'Experience', href: '/experience' },
      { label: 'Capabilities', href: '/services' },
      { label: 'Resume', href: '/resume' },
    ],
  },
  {
    heading: 'Knowledge & Tools',
    links: [
      { label: 'Writing', href: '/writing' },
      { label: 'Developer Lab', href: '/lab' },
    ],
  },
  {
    heading: 'Connect',
    links: [
      { label: 'About', href: '/about' },
      { label: 'Contact', href: '/contact' },
    ],
  },
];
