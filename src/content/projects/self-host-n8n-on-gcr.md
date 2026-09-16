---
title: "Self-hosting n8n on Google Cloud Run"
screenshot:
  src: "../../assets/projects/self-host-n8n-on-gcr.png"
  alt: "GitHub repository for self-hosting n8n on Google Cloud Run, showing deployment files and the setup guide."
summary: "An open-source deployment guide for running the n8n automation platform serverlessly on Google Cloud for a few pounds a month, with more than 600 GitHub stars and contributions from Google's Cloud Run product team."
context: "Open source"
role: "Author and maintainer"
collaborators:
  - "Community contributors, including Google Cloud Run product team members"
status: "Maintained since March 2025"
order: 7
featured: false
tags:
  - "n8n"
  - "google_cloud_run"
  - "serverless"
  - "open_source"
links:
  - label: "Read the guide on GitHub"
    url: "https://github.com/datawranglerai/self-host-n8n-on-gcr"
highlights:
  - value: "600+"
    label: "GitHub stars"
  - value: "130+"
    label: "Forks"
  - value: "£2–£12"
    label: "Typical monthly running cost"
---

I wrote and maintain an open-source guide to self-hosting n8n, the workflow automation platform, on Google Cloud Run. It is for people who want their automation infrastructure under their own control and on their own cloud bill, without a subscription and without a server to patch. The deployment scales to zero when idle and persists workflows in Cloud SQL, so a typical instance costs between two and twelve pounds a month, most of it the database.

## A guide that people use

The repository has passed 600 stars and 130 forks since March 2025 and is licensed under MIT. Contributors include members of Google's Cloud Run product team, who reached out and made improvements directly, alongside community members who added a full Terraform configuration and a step-by-step video walkthrough. Google has since published its own Cloud Run guidance for n8n; this guide remains the more complete route for anyone going beyond a quick start, covering queue mode, Google Workspace OAuth, updates and cost tuning.

I also run Braidr's own n8n instance from this setup, which is where the team builds low-code agentic workflows that pull from Slack, Asana, Google Drive and email.

## The contribution

The value of the guide is in the parts that only surface when you actually run n8n on Cloud Run. The database connection races the container start, so the guide adds a short delay. Cloud Run intercepts every path ending in "z" at its load balancer, which silently breaks n8n's default health endpoint, so the guide moves it. CPU throttling has to be disabled or background executions stall. Redis for queue mode needs Direct VPC egress to stay private. Each of these is explained rather than just asserted, so readers can judge whether the workaround still applies as the platforms change.

The guide is structured as nine manual steps with a Terraform alternative, a choice between the official image and a custom container, and a separate section on scaling to queue mode with dedicated workers. I keep it current as n8n and Cloud Run move, and review contributions so that what people copy into production is correct.
