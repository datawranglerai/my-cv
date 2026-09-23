---
title: "Where Was I?"
screenshot:
  src: "../../assets/projects/where-was-i.png"
  alt: "Where Was I? book upload form with a stopping-page field and a spoiler-free recap preview."
summary: "An AI reading assistant for half-finished books. Upload a PDF or EPUB, tell it where you stopped, and get a recap to help you pick it back up."
context: "Personal"
role: "Co-creator: product design, retrieval and summarisation pipeline, and web app"
collaborators:
  - "Adrian"
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

You're 200 pages into a book. Life happens. Two weeks later, you pick it up and have no idea who anyone is or why they're arguing. Google the book and risk spoiling the ending. Start again and probably abandon it in exactly the same place.

I built Where Was I? with my friend Adrian because this kept happening to me. ADHD plus a growing stack of half-finished books meant I was giving up on things I actually enjoyed. Upload a PDF or EPUB, enter your current page, get a recap. No sign-up.

<a class="product-hunt-badge" href="https://www.producthunt.com/products/where-was-i?utm_source=badge-follow&amp;utm_medium=badge&amp;utm_source=badge-where-was-i" target="_blank" rel="noopener noreferrer" aria-label="Follow Where Was I? on Product Hunt (opens in a new tab)" data-goatcounter-click="project_where-was-i_product_hunt_clicked" data-goatcounter-no-session="1">
  <img class="product-hunt-badge-dark" src="https://api.producthunt.com/widgets/embed-image/v1/follow.svg?product_id=1129836&amp;theme=dark" alt="Where was I? - Remember what the hell was happening in that book | Product Hunt" width="250" height="54" decoding="async" />
  <img class="product-hunt-badge-light" src="https://api.producthunt.com/widgets/embed-image/v1/follow.svg?product_id=1129836&amp;theme=light" alt="Where was I? - Remember what the hell was happening in that book | Product Hunt" width="250" height="54" decoding="async" />
</a>

## The surprisingly hard bit

Spoiler prevention gets complicated quickly. The pipeline works from the uploaded book, carries page numbers through processing, and applies page filters when retrieving passages. The stopping point influences what reaches the model as well as what the prompt asks it to do. There are still edge cases to test.

Fiction also needs more care than splitting text into equal-sized blocks. I use semantic chunking with overlap to preserve context, then search for different kinds of story event: discoveries, decisions, conflicts and consequences. The retrieval stage balances relevance with variety, removes repetition, and puts the selected passages back into story order.

## A recap I can actually use

The recap needs to be easy to scan when your working memory has already clocked off. Short sections, character names in bold, clear connections between events. Enough to remember why the butler seemed suspicious.

For longer inputs, the summariser splits the retrieved material to fit the model's token budget, summarises sections in parallel, then combines them into one chronological recap. An optional shortcut handles smaller inputs in a single call.

## Keeping it free

Completed recaps and embeddings are cached so repeat requests can reuse work. The backend checks whether previously processed text is still compatible with the current model and chunking settings before reusing it. Related searches are batched, and embeddings can run locally or through an API.

It's live, free to use and supported by donations. Try the built-in example before digging out a book. Getting back to those books keeps me working on it.
