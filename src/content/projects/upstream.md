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

Upstream is a joint research initiative from Fieldcraft Studios and Braidr, built as the founding project of Braidr's AI for Good programme. It maps the gap between what UK recreational water users care about and the invisible threat of antimicrobial resistance (AMR) in rivers, and publishes the results free for anyone designing awareness work. I led the project at Braidr and owned the analytical pipeline end to end, from social data collection through LLM analysis to the public web deliverable. Fieldcraft brought the brief, the AMR expertise and the campaign strategy.

## The communication problem

Antibiotic-resistant bacteria have been found at every UK river site sampled, and University of Exeter research found surfers carrying resistant E. coli at three times the rate of non-surfers. Most of the public knows about sewage in rivers. Almost nobody connects it to drug-resistant infection. The people most exposed, wild swimmers, paddlers, anglers and surfers, are also emotionally invested in the activity that exposes them, and many frame it as essential to their mental health. Any message that reads as "stop swimming" will be rejected.

So the research question was not "how do we explain AMR" but "what does each community already care about, whom do they trust, and where is the bridge from that to a fact they need". The answer had to be specific to community and platform, because the same people tolerate paragraph-length explanations on Reddit and two sentences of text overlay on TikTok.

## The work

I designed the pipeline as a research instrument rather than a summariser. Every analysis call carries a system prompt grounded in published AMR science, risk-communication research and UK regulatory context, with every factual claim citing its source inline. The model is instructed to propagate those citations into its outputs, so the finished analysis is traceable to the Exeter study, Environment Agency surveillance, Wellcome Trust research and the UK AMR National Action Plan rather than to the model's general knowledge. Outputs follow a strict schema, and every behavioural signal carries a strength rating from strong to isolated, so a single striking post cannot masquerade as a trend.

Data was collected per community and per platform, filtered for UK relevance, then analysed in two passes: a platform-level analysis, then a cross-platform synthesis into stable community-level insights. I structured the data in three layers, platform, community and comparative matrix, because some findings are platform-specific, some hold across a community, and the strategically interesting ones sit in between. The static site renders the matrix of ten communities against seven dimensions, from opportunity sizing and awareness gap through trust calibration to near-copy message hooks, with a deep-dive page per community.

The wild-swimming pilot on TikTok set the method. Across 482 UK posts from 169 creators there was not a single mention of AMR, the creator ecosystem was almost entirely grassroots, and the dominant safety heuristic was visual clarity, the most dangerous and most correctable misconception in the data. One organic comment warning about resistant bacteria showed peer-delivered health information is accepted. Those findings became five messaging pathways with bridge logic, credible messengers and risk notes.

The work is published as living research, with collection still under way on some platforms, and it formed part of Braidr's work recognised at the 2026 DataComms Awards. Colleagues built the collection pipeline and the visual design; Fieldcraft turns the matrix into campaign creative.
