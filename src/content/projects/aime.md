---
title: "AI.M.E."
summary: "A public-evidence research system for assessing organisational AI maturity, with published FTSE AIM 100 and FTSE 350 studies."
context: "Professional"
role: "Programme lead; evaluation methodology and research design"
collaborators:
  - "Braidr engineering team"
status: "In production"
order: 1
featured: true
tags:
  - "AI maturity"
  - "Multi-agent research"
  - "Evaluation methodology"
links:
  - label: "FTSE 350 study"
    url: "https://aime.braidr.ai/ftse350"
  - label: "Published methodology"
    url: "https://braidr.ai/blog/braidrs-ai-maturity-evaluation-index-showing-our-workings/"
highlights:
  - value: "350"
    label: "Companies in the published FTSE 350 study"
  - value: "180+"
    label: "Assessment criteria"
---

AI.M.E. (Agentic AI Maturity Evaluation) assesses how organisations use and govern AI using publicly available evidence. I lead the programme at Braidr, from the evaluation methodology and research design through to its continuing operation. I designed and co-built the system with a small engineering team. The FTSE AIM 100 and FTSE 350 assessments are complete and published; the research agents remain in production and run on demand for other use cases.

## The research problem

An organisation's public record offers clues about its AI capability, but it does not give us direct access to its internal practice. That constraint shaped the assessment: findings need identifiable sources, uncertainty needs to remain visible, and a score needs to be explainable in terms of the evidence available. A public-evidence assessment should not be mistaken for a complete account of what happens inside a company.

My work includes deciding what the assessment should measure, how the research should gather evidence, and how assessors should reason across more than 180 criteria. These choices matter as much as the agent architecture: they determine what the system can responsibly conclude from its sources.

## How the agents work

The system uses a hierarchical architecture built on Google's Agent Development Kit (ADK). A coordinator delegates research to agents specialising in different assessment pillars. Each specialist has an isolated context, so its research can be developed within a defined part of the evaluation before the findings are brought together.

A council of agents representing maturity levels then debates and scores the evidence over structured discussion rounds. Every finding is traced to its source and receives a confidence rating. This lets a reader inspect the basis for an assessment and see where the available evidence is weaker.

## Published work and continuing questions

We assessed the FTSE AIM 100: 100 companies in two weeks, at roughly $1–$2 per company for that run. We also completed and published the FTSE 350 assessment. These runs show the system operating across large company lists while keeping its findings tied to public sources. I continue to lead the production research programme as the agents are used on demand for further questions.

One such question concerns subsidiaries. I have designed an empirical test of whether a parent company's maturity score represents its subsidiary brands. That question needs a comparison of the brands' own evidence, rather than an assumption that the parent's score applies to each of them.
