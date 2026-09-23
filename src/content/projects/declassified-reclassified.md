---
title: "Declassified Reclassified"
screenshot:
  src: "../../assets/projects/declassified-reclassified.png"
  alt: "Declassified Reclassified public evidence snapshot listing report files, curated JSON exports and a caveat about interpreting the evidence."
summary: "An evidence pipeline and journalistic report over eight decades of declassified US UAP records, scoring each artefact for documentary strength rather than for the likelihood of anything exotic."
context: "Personal"
role: "Researcher, pipeline author and writer"
status: "Ongoing; run 34 published August 2026"
order: 4
featured: false
tags:
  - "document_analysis"
  - "evidence_provenance"
  - "investigative_writing"
  - "ocr"
highlights:
  - value: "20"
    label: "Ranked cases in the public snapshot"
  - value: "4"
    label: "Rubric dimensions: substantiation, intrigue, technical detail, provenance"
  - value: "1947–2024"
    label: "Span of records in the corpus"
links:
  - label: "Read the public evidence snapshot"
    url: "https://gist.github.com/datawranglerai/562e5abacc232ef9c540dfde913e211c"
---

Declassified Reclassified reads recently released US government files on unidentified anomalous phenomena (UAP) the way a sceptical journalist would, except the journalist is a pipeline with an audit trail. The corpus runs from a 1947 Air Materiel Command memo, via the CIA's 1953 panel, Project Blue Book and the FBI's Socorro file, to US Central Command mission reports from 2020 to 2024. It produces a ranked top twenty, published as a GitHub Gist with its evidence records, citations and file hashes attached.

## What the files establish

Declassification makes records available. It also makes wishful reading easy. So each document is scored on what it establishes and where the record stops, and the ranking rewards institutional provenance, contemporaneous documentation, physical traces and sensor data. A high score means a strong artefact. It says nothing about aliens.

Most of what has been released is paperwork about evidence. The films, track files and samples mostly aren't there, and the report counts that gap as a finding.

## How it's built

The pipeline OCRs the scans, scores each artefact against a four-part rubric and writes everything to a SQLite audit database. Every claim in the report links to a citation in that database, and every citation to a source file.

The Gist carries the report, evidence images and JSON exports and nothing else. No code, credentials, database or raw model calls. It's the discipline I apply to research systems at work, pointed at the subject where over-reading the evidence is most tempting.
