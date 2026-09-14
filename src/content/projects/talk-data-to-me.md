---
title: "Talk Data to Me"
summary: "A real-time audio commentator for multi-agent AI workflows, built for the Google Gemma 3n Impact Challenge: sensitive agent decisions run locally on Gemma 3n while a cloud commentator explains them to a human audience as they happen."
context: "Hackathon"
role: "Creator: architecture, agents, audio pipeline and write-up"
status: "Hackathon entry, July 2025"
order: 6
featured: false
tags:
  - "agentic_workflows"
  - "ai_transparency"
  - "gemma_3n"
  - "google_adk"
highlights:
  - value: "<500 ms"
    label: "Event to spoken explanation"
  - value: "5"
    label: "Agents in the crisis-response demo"
  - value: "8 GB"
    label: "Consumer laptop it runs on"
links:
  - label: "Read the hackathon write-up"
    url: "https://www.kaggle.com/competitions/google-gemma-3n-hackathon/writeups/talk-data-to-me"
  - label: "Source code on GitHub"
    url: "https://github.com/datawranglerai/talk-data-to-me"
---

I built Talk Data to Me for the Google Gemma 3n Impact Challenge in July 2025. It is a real-time commentary system for multi-agent workflows: as agents plan, call tools and hand off to one another, a commentator agent watches the event stream and narrates what is happening in plain spoken English, in the register of a sports broadcaster. The demo is a wildfire emergency simulation in which a coordinator and four specialist agents follow emergency-management protocols while the commentator explains each decision as it is made.

## Making a workflow legible

Multi-step agent systems make consequential choices while the people affected see only a final output, or logs that read like a microwave manual. The entry argues that transparency is a presentation problem as much as a logging problem. A line such as "agent executed resource_allocation_optimization with parameter_set_7" becomes "the system just realised it needs more ambulances on the north side because traffic is backing up the evacuation route". One of those builds trust.

The architecture has a second point to make. Gemma 3n, quantised to 4-bit and served locally through LM Studio, runs the agents that make the sensitive decisions, so that reasoning never leaves the device. Gemini Live handles the commentary, which is public by design. Keeping the private part local and the explanatory part in the cloud is the hybrid the write-up proposes for healthcare, emergency and financial settings, and the whole thing runs on a MacBook Air with 8 GB of memory.

## The hackathon entry

The system is built on Google's Agent Development Kit (ADK). Tool calls, tool results and model reasoning are captured through ADK callbacks and pushed onto an asynchronous queue that the commentator consumes in parallel with the workflow, so commentary never blocks the agents. Commentary is generated with a bounded memory of what has already been said to stop repetition, and rotates between personas to stay listenable. Audio streams through a callback-based player after a thread-based version produced audible glitches, and the measured latency from event to spoken explanation is under half a second.

I worked on it alone, from an earlier June 2025 prototype of the commentator to the Gemma 3n integration and the crisis-response use case. The honest finding from the local-model work was that Gemma 3n could not match cloud models on the hardest coordination tasks at the time, which is why the final design is hybrid rather than fully on-device.
