---
title: "Where Was I?"
summary: "A reading catch-up app that uses a reader's PDF or EPUB to produce a spoiler-free recap of the story so far."
context: "Personal"
role: "Creator"
order: 2
featured: false
tags:
  - "retrieval_augmented_generation"
  - "rag"
  - "reading_accessibility"
links:
  - label: "Visit Where Was I?"
    url: "https://wherewasi.co.uk"
---

Where Was I? is my personal project for readers who have lost the thread of a book and want to pick it up again. It is designed with readers with ADHD especially in mind. A reader uploads the PDF or EPUB they are reading and asks for a recap of what has happened up to their current point, without revealing what comes next.

## The reading problem

Returning to a book after a break can mean reconstructing characters, events and unresolved threads before the story makes sense again. Looking for a synopsis online risks revealing later plot points. The useful answer is bounded by where the reader has reached, rather than by the whole book.

## The approach

I built the app around retrieval-augmented generation (RAG) so it can draw on the uploaded book when preparing a recap. The core product decision is to let the reader set the stopping point and make a spoiler-free summary of the story so far the primary task.
