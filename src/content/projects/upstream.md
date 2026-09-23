---
title: "Upstream"
screenshot:
  src: "../../assets/projects/upstream.png"
  alt: "Upstream research landing page with a river photograph and an introduction to UK water-user communities and antimicrobial resistance."
summary: "An open audience-intelligence matrix profiling ten UK water-user communities across seven strategic dimensions, so an antimicrobial resistance campaign can reach people who have never heard of the threat."
context: "Professional"
role: "Project lead: pipeline architecture, research-grounded analysis design, data architecture and the web deliverable"
collaborators:
  - "Fieldcraft Studios (brief, AMR subject expertise, campaign strategy)"
  - "Braidr colleagues (data collection, visual design)"
status: "Live, living research"
order: 3
featured: false
tags:
  - "audience_intelligence"
  - "ai_for_good"
  - "antimicrobial_resistance"
  - "discourse_analysis"
links:
  - label: "Explore Upstream"
    url: "https://good.braidr.ai/upstream"
highlights:
  - value: "10 × 7"
    label: "Communities profiled across strategic dimensions"
  - value: "3"
    label: "Platforms analysed: TikTok, Instagram, Reddit"
  - value: "482"
    label: "UK posts in the wild-swimming pilot, with zero AMR mentions"
---

Upstream is a joint research initiative from Fieldcraft Studios and Braidr, and the founding project of Braidr's AI for Good programme. It maps the gap between what UK wild swimmers, paddlers, anglers and surfers care about and the antimicrobial resistance (AMR) sharing the water with them, and publishes the findings free for anyone designing awareness work. I led the Braidr side and owned the analytical pipeline end to end.

## Why "stop swimming" doesn't work

Antibiotic-resistant bacteria have turned up at every UK river site sampled, and University of Exeter research found surfers carrying resistant E. coli at three times the rate of non-surfers. Most people know about sewage in rivers. Almost nobody connects it to drug-resistant infection. And the people most exposed are the most attached to the water, so anything that reads as "stop swimming" gets binned.

The useful question turned out to be what each community already cares about, whom it trusts, and where the bridge is from there to a fact it needs. Per platform, too: the same people will read a paragraph on Reddit and two sentences on TikTok.

## How it works

I built the pipeline as a research instrument. Every analysis call runs on a system prompt grounded in published AMR science, risk-communication research and UK regulatory context, with each claim cited inline. The model propagates those citations into its outputs, so the analysis traces to the Exeter study and Environment Agency surveillance rather than to whatever the model half-remembers. Every behavioural signal also gets a strength rating from strong to isolated, so one striking post can't masquerade as a trend.

The public site renders ten communities against seven dimensions, from opportunity sizing to near-copy message hooks, with a deep dive per community.

The wild-swimming pilot on TikTok set the method. Across 482 UK posts from 169 creators, AMR came up zero times, and the dominant safety heuristic was whether the water looked clear, the most dangerous and most correctable misconception in the data. Those findings became five messaging pathways with bridge logic, credible messengers and risk notes.

It's living research, still collecting on some platforms, and part of the Braidr work recognised at the 2026 DataComms Awards. Colleagues built the collection pipeline and visual design; Fieldcraft brought the brief and AMR expertise, and turns the matrix into campaign creative.
