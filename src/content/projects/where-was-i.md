---
title: "Where Was I?"
screenshot:
  src: "../../assets/projects/where-was-i.png"
  alt: "Where Was I? book upload form with a stopping-page field and a spoiler-free recap preview."
summary: "A free web app for readers who have abandoned a book mid-way: upload the PDF or EPUB, mark where you stopped, and get a recap of the story so far with nothing from beyond that point."
context: "Personal"
role: "Creator: product design, retrieval pipeline and web app"
status: "Live, free to use"
order: 2
featured: false
tags:
  - "retrieval_augmented_generation"
  - "reading_accessibility"
  - "consumer_product"
links:
  - label: "Open Where Was I?"
    url: "https://app.wherewasi.co.uk/"
---

Where Was I? is my personal project for readers who have lost the thread of a book and want to pick it up again rather than start over. I built it with readers with ADHD especially in mind, for whom a long gap between chapters is the normal case rather than the exception. A reader drops in the PDF or EPUB they are reading, marks how far they have got, and asks for a recap of what has happened up to that point. The app is live, free, and supported by donations.

## The reading problem

Returning to a book after a break means reconstructing characters, events and unresolved threads before the story makes sense again. The obvious shortcuts all fail. A synopsis online covers the whole book and gives away the ending. Re-reading from the start is exactly the barrier that made the book stall. Asking a general chatbot about a novel trades on its training data, which may be wrong, may be a different edition, and does not know where you stopped.

The useful answer is bounded by the reader's position, not by the book. That single constraint shaped everything else: the app works from the reader's own copy, and the stopping point is the primary input rather than an afterthought.

## The approach

The app is built around retrieval-augmented generation (RAG) over the uploaded file. The text is parsed and chunked with its position preserved, so retrieval can be cut off hard at the reader's marker and the recap is generated only from passages before it. That is a stricter design than asking a model to "avoid spoilers": the material after the stopping point is never in the prompt, so it cannot leak. The reader's file is the only source of truth, which also means the recap follows the edition in their hands rather than a remembered version of the book.

The product decisions were about restraint. The recap is the one job. There is no account, no library and no social layer, because the reader has arrived with a single question and wants to get back to the book. The tone is deliberately warm and unjudgemental, since the target user has usually already decided they are the problem.
