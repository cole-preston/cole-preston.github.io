---
# ============================================================
# PLACEHOLDER: copy this file to start a new entry.
#   1. Copy it to _projects/YYYY-MM-DD-short-title.md
#   2. Fill in the fields below and write the body.
#   3. Set published: true (or delete that line).
# With published: false, this file only appears when you run
#   bundle exec jekyll serve --unpublished
# ============================================================
published: false
title: "[PLACEHOLDER] Example project — copy this file"
kind: paper            # paper | data | essay  (sets the section on /projects/)
date: 2026-01-01
course:                # optional, e.g. course number and term
excerpt: "One or two sentences summarizing the project. Shown on the Projects & Writing page."
paperurl:              # optional, e.g. /files/your-paper.pdf (put the PDF in files/)
codeurl:               # optional, e.g. a GitHub repository URL
---

{% if page.course %}*{{ page.course }}*

{% endif %}{% if page.paperurl %}[Read the PDF]({{ page.paperurl }}){% endif %}{% if page.paperurl and page.codeurl %} · {% endif %}{% if page.codeurl %}[Code]({{ page.codeurl }}){% endif %}

## Question

## Approach

## Findings
