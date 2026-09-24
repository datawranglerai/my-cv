---
title: "AI.M.E."
screenshot:
  src: "../../assets/projects/aime.png"
  alt: "AI.M.E. leaderboard showing ranked companies and their scores across five AI maturity pillars."
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

AI.M.E. (Agentic AI Maturity Evaluation)

Every company that cares about AI says it's doing AI. The honest way to check is to look at what they actually publish, and that's what AI.M.E. does. It's a multi-agent research system that scores how organisations adopt and govern AI, working from publicly available evidence only. I lead the programme at Braidr, from the evaluation framework and research design through to architecture decisions, and co-built the system with a small engineering team. Two cohort studies are published, the FTSE AIM 100 (September 2025) and the FTSE 350 (July 2026), and the system now runs on demand as a production research service.

## The constraint became the design

A company's public record holds real signals about its AI capability. It holds no direct view of internal practice, and I decided early to treat that as a design principle rather than a caveat. Every finding cites an identifiable source. Uncertainty stays visible in the output instead of being polished away. A score has to be explainable from the evidence behind it, and where the evidence is thin, the report says so. The model can misread what it's given. It just can't invent what it wasn't given. So what AI.M.E. measures is publicly evidenced maturity, not everything a company quietly does behind closed doors.

My part sits in the framework. I defined what the assessment measures: five pillars (AI Strategy, Data & Insight, Content, Product & Service, People), a maturity curve running from Analogue to Augmentation, and the 180+ criteria the assessors reason against. I also chose to publish the methodology in full, so anyone can argue with the scores on their workings rather than taking them on trust.

## How it works

The system runs on Google's Agent Development Kit (ADK). A research coordinator delegates to pillar specialists, and the specialists share an intelligence bus, so a finding that surfaces under Data & Insight can do useful work under AI Strategy too. Then comes the assessor council, organised by maturity stage rather than topic. Each assessor specialises in the signals that separate genuine adoption from a well-funded pilot, and the council debates the evidence over structured rounds until it reaches consensus. Fact-checking agents run through multiple layers before anything gets reported.

Two choices keep the output auditable. The models gather and weigh evidence, but final scores are calculated deterministically in code, so the same inputs give the same figures on every run. The models argue; the spreadsheet keeps the score. Reporting is constrained to cited findings, each with a source and a reliability rating, so a reader can see which findings rest on solid ground and which don't.

## What's published, and what still nags

The FTSE AIM 100 run assessed 100 companies in about two weeks, at roughly $1 to $2 per company. The FTSE 350 study took 350 companies through just under 99 hours of runtime, drawing on 5,878 distinct public sources. Sixty-five percent of its evidence findings came out rated four or five out of five for reliability, per the published methodology. That's a number I'm pleased with but not smug about, since reliability ratings are only as good as the fact-checkers giving them.

One open question concerns subsidiaries. Several FTSE 350 constituents are listed parents sitting above dozens or hundreds of consumer brands, and it's not obvious that a parent's score carries down to them. I've designed an empirical test that compares the brands' own evidence rather than assuming the score transfers. There's a second question I can't quite close: the assessors are models, and models change when their makers update them. Regression against earlier runs is a standing concern, not a solved problem, which is how most real systems live.
