---
title: "Redspace mapping"
screenshot:
  src: "../../assets/projects/redspace-mapping.png"
  alt: "Redspace Atlas showing a discourse-pressure scatter plot, narrative chapters and a selected term's evidence panel."
summary: "A discourse-pressure map of Israel–Palestine conflict language: 300+ client-approved terms scored for how reliably they provoke hostile reaction, each with a confidence rating, feeding a peace campaign's messaging."
context: "Professional"
role: "Methodology lead and Atlas builder: scoring framework, triangulation, QA and the client-facing web app"
collaborators:
  - "Small Braidr team (collection pipeline, source governance, domain steer)"
  - "Culture3, white-label partner for the Principles for Peace campaign"
status: "Delivered August 2026"
order: 3
featured: false
tags:
  - "discourse_analysis"
  - "peacebuilding"
  - "computational_linguistics"
  - "llm"
links:
  - label: "Redspace Atlas (stakeholder preview, sign-in required)"
    url: "https://redspace-mapping.web.app/"
highlights:
  - value: "300+"
    label: "Client-approved terms scored"
  - value: "3"
    label: "Evidence streams triangulated"
  - value: "~7 days"
    label: "Brief to authenticated client prototype"
---

Redspace mapping is a discourse-pressure map of the language around the Israel–Palestine conflict, built for a creative agency's work on a peace campaign convened by the Principles for Peace foundation. The question was practical: which terms reliably set people off, which hold across communities, and how confident can anyone be in each call. I led the methodology and built the Redspace Atlas, the authenticated web app in which the client explores the results. The work ran white-label and was delivered in August 2026, about six weeks from kickoff.

## Why the language matters

Public polling shows that the label and the substance of the same proposition can poll twenty points apart, so a campaign built on the wrong words dies before its argument is heard. The brief was to map the redspace, where messaging dies, and the holding language that draws agreement, as one input to the campaign's propositional work alongside polling and a qualitative panel.

The constraints shaped the method. Nobody on the team was a subject-matter expert, the material was distressing, and the output had to survive hostile methodological attack rather than peer review. So coverage is driven by a taxonomy of the conflict's contested facets, crossed with community and era, rather than by whichever platforms are easiest to scrape. Collection used publicly accessible data only, anonymised at ingest, with closed spaces excluded and every source signed off by the client before collection began. Limits travel with every artefact: data asymmetries between communities, the post-October 2023 window, and a corpus that tilts toward public, performative talk.

## My contribution

I designed the scoring framework and the triangulation protocol. A term is scored in the reaction layer only, through replies, quote posts and comments, because reactions show whether a word lands quietly or ignites. The composite combines hostility intensity, cross-community divergence (asymmetry is the dangerous signal) and volatility, reported on a 0–100 scale and banded red, amber or green. Confidence is reported separately, driven by sample size, cross-source consistency and validation agreement, so a low-confidence red stays red and says so. Language models handle structured classification only; heat, confidence, gates and band movement are deterministic rules, which means every score can be explained. Scores are cross-checked against the polling and an academic and historic layer, and disagreement raises a flag for human review rather than being averaged away.

I wrote the pipeline requirements with a pre-mortem, reviewed the collection and classification pipeline a colleague built, QA'd the final dataset (catching canonical terms split across unrelated facets before integration), designed the bias check, and built and deployed the Atlas on Firebase with a Cloud Run backend and OAuth sign-in. It plots each term by score, sizes it by reaction volume, and rings the terms that scoring gates escalated. The client described the approved seed list as unusually comprehensive, and the August walkthrough with the agency landed well. The standing limitation is 
    label: "Client-approved terms scored"
  - value: "3"
    label: "Evidence streams triangulated"
  - value: "~7 days"
    label: "Brief to authenticated client prototype"
---

Redspace mapping is a discourse-pressure map of the language around the Israel–Palestine conflict, built for a creative agency's work on a peace campaign convened by the Principles for Peace foundation. The question was practical: which terms reliably set people off, which hold across communities, and how confident can anyone be in each call. I led the methodology and built the Redspace Atlas, the authenticated web app in which the client explores the results. The work ran white-label and was delivered in August 2026, about six weeks from kickoff.

## Why the language matters

Public polling shows that the label and the substance of the same proposition can poll twenty points apart, so a campaign built on the wrong words dies before its argument is heard. The brief was to map the redspace, where messaging dies, and the holding language that draws agreement, as one input to the campaign's propositional work alongside polling and a qualitative panel.

The constraints shaped the method. Nobody on the team was a subject-matter expert, the material was distressing, and the output had to survive hostile methodological attack rather than peer review. So coverage is driven by a taxonomy of the conflict's contested facets, crossed with community and era, rather than by whichever platforms are easiest to scrape. Collection used publicly accessible data only, anonymised at ingest, with closed spaces excluded and every source signed off by the client before collection began. Limits travel with every artefact: data asymmetries between communities, the post-October 2023 window, and a corpus that tilts toward public, performative talk.

## My contribution

I designed the scoring framework and the triangulation protocol. A term is scored in the reaction layer only, through replies, quote posts and comments, because reactions show whether a word lands quietly or ignites. The composite combines hostility intensity, cross-community divergence (asymmetry is the dangerous signal) and volatility, reported on a 0–100 scale and banded red, amber or green. Confidence is reported separately, driven by sample size, cross-source consistency and validation agreement, so a low-confidence red stays red and says so. Language models handle structured classification only; heat, confidence, gates and band movement are deterministic rules, which means every score can be explained. Scores are cross-checked against the polling and an academic and historic layer, and disagreement raises a flag for human review rather than being averaged away.

I wrote the pipeline requirements with a pre-mortem, reviewed the collection and classification pipeline a colleague built, QA'd the final dataset (catching canonical terms split across unrelated facets before integration), designed the bias check, and built and deployed the Atlas on Firebase with a Cloud Run backend and OAuth sign-in. It plots each term by score, sizes it by reaction volume, and rings the terms that scoring gates escalated. The client described the approved seed list as unusually comprehensive, and the August walkthrough with the agency landed well. The standing limitation is that native-speaker validation for Hebrew and Arabic was thinner than designed, so confidence caps hold on community-weighted claims.
