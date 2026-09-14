---
title: "AI.M.E."
summary: "A multi-agent research system that scores organisational AI maturity from public evidence alone, with published FTSE AIM 100 and FTSE 350 studies."
context: "Professional"
role: "Programme lead: evaluation framework, research methodology and architecture decisions"
collaborators:
  - "Small Braidr engineering team"
status: "In production"
order: 1
featured: true
tags:
  - "multi_agent_systems"
  - "evaluation_methodology"
  - "ai_maturity"
  - "google_adk"
links:
  - label: "FTSE 350 study"
    url: "https://aime.braidr.ai/ftse350"
  - label: "Published methodology"
    url: "https://braidr.ai/blog/braidrs-ai-maturity-evaluation-index-showing-our-workings/"
highlights:
  - value: "350"
    label: "Companies scored, FTSE 350 study (July 2026)"
  - value: "5,878"
    label: "Distinct public sources cited, FTSE 350"
  - value: "180+"
    label: "Criteria across five pillars"
  - value: "~15 min"
    label: "Median research time per company, FTSE 350"
---

AI.M.E. (Agentic AI Maturity Evaluation) is a multi-agent research system that scores how organisations adopt and govern AI, using publicly available evidence only. I lead the programme at Braidr, from the evaluation framework and research design through to architecture decisions, and co-built the system with a small engineering team. Two cohort studies are published, the FTSE AIM 100 (September 2025) and the FTSE 350 (July 2026), and the system now runs on demand as a production research service.

## The research problem

A company's public record holds real signals about its AI capability, but no direct view of internal practice. I made that constraint the design principle rather than a caveat: every finding cites an identifiable source, uncertainty stays visible, and a score must be explainable from the evidence behind it. The model is never the source of a fact, and the result measures publicly evidenced maturity, not everything a company does.

My contribution sits in the framework. I defined what the assessment measures: five pillars (AI Strategy, Data & Insight, Content, Product & Service, People), a maturity curve from Analogue to Augmentation, and the 180+ criteria the assessors reason against. I also chose to publish the methodology in full, so the scores can be challenged on their workings rather than taken on trust.

## How the agents work

The system is built on Google's Agent Development Kit (ADK). A research coordinator delegates to pillar specialists, each working in an isolated context so evidence for one pillar cannot bleed into another's reasoning before findings are pooled. An assessor council is organised by maturity stage rather than topic: each assessor specialises in the signals separating genuine adoption from a well-funded pilot, and the council debates the evidence over structured rounds.

Two decisions keep the output auditable. Language models gather and weigh evidence, but final scores are calculated deterministically in code, so the same inputs give the same figures on every run. Reporting is constrained to cited findings, each with a source and a reliability rating, so a reader can see where the evidence is thin.

## Published work and continuing questions

The FTSE AIM 100 run assessed 100 companies in about two weeks, at roughly $1–$2 per company for that run. The FTSE 350 study assessed 350 companies in just under 99 hours of runtime, drawing on 5,878 distinct public sources; 65% of its evidence findings were rated four or five out of five for reliability (figures from the published methodology).

One open question concerns subsidiaries. Several FTSE 350 constituents are listed parents above dozens or hundreds of consumer brands. I have designed an empirical test of whether a parent score represents its brands, comparing the brands' own evidence rather than assuming the score carries down. Assessor judgement also rests on model behaviour that shifts with model updates, so regression against earlier runs is a standing concern rather than a solved problem.
