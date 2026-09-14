---
title: "Declassified Reclassified"
summary: "An evidence pipeline and journalistic report over eight decades of declassified US UAP records, scoring each artefact for documentary strength rather than for the likelihood of anything exotic."
context: "Personal"
role: "Researcher, pipeline author and writer"
status: "Ongoing; run 34 published August 2026"
order: 5
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

Declassified Reclassified is a personal research project that reads recently declassified US government files on unidentified anomalous phenomena (UAP) the way a sceptical journalist would, with the difference that the reading is done by a pipeline with an audit trail. The corpus runs from a 1947 Air Materiel Command memo, through the CIA's 1953 scientific panel, Project Blue Book and the FBI's Socorro file, to US Central Command mission reports from 2020 to 2024. The public output is a ranked report of the twenty most compelling cases, published as a GitHub Gist with its evidence records, citations and file hashes alongside.

## The question behind it

Declassification makes records available. It does not make their meaning clear, and it makes an attractive interpretation easy. The question I wanted to answer is narrower than "what is out there": what does each document actually establish, how good is its provenance, and where does the record stop. The report says this plainly. Scores measure the strength of each artefact, not the probability of an exotic origin, and the ranking rewards institutional provenance, contemporaneous documentation, physical traces and sensor data. Most of what has been released is reports about evidence, not the films, track files or samples themselves, and the report treats that gap as a finding in its own right.

## The format

The pipeline OCRs the scanned PDFs, records deterministic technical observations per artefact, runs a structured analysis against a four-part rubric, and writes everything to a SQLite audit database. The rendered report is generated from that database, so every claim links to a citation row and every citation to a source artefact. Processing limitations travel with the records: several large files were OCRed in page-image chunks at low resolution, so equations, small table entries and handwriting may be mistranscribed, and the report says so rather than smoothing it over.

Publishing as a Gist is a deliberate choice. It lets me share the rendered report, the embedded evidence images and curated JSON exports for discussion with other developers, without publishing source code, credentials, the full database or raw model requests. It is the same discipline I apply in professional research systems, applied to a subject where the temptation to over-read the evidence is strongest.
