---
layout: single
title: "Reading"
permalink: /reading/
author_profile: true
# Covers live in images/books/ (about 300px tall, metadata stripped).
# Leave cover blank to show a plain title block instead.
currently_reading:
  - title: "How Asia Works"
    author: "Joe Studwell"
    cover: "how-asia-works.jpg"
  - title: "The Prize: The Epic Quest for Oil, Money, and Power"
    author: "Daniel Yergin"
    cover: "the-prize.jpg"
  - title: "The Brothers Karamazov"
    author: "Fyodor Dostoevsky"
    translator: "Richard Pevear and Larissa Volokhonsky"
    cover: "the-brothers-karamazov.jpg"
read:
  - title: "Capitalism and Freedom"
    author: "Milton Friedman"
    cover: "capitalism-and-freedom.jpg"
  - title: "Crime and Punishment"
    author: "Fyodor Dostoevsky"
    cover: "crime-and-punishment.jpg"
  - title: "The Stranger"
    author: "Albert Camus"
    cover: "the-stranger.jpg"
  - title: "1984"
    author: "George Orwell"
    cover: "1984.jpg"
up_next:
  - title: "MITI and the Japanese Miracle"
    author: "Chalmers Johnson"
    cover: "miti-and-the-japanese-miracle.jpg"
  - title: "Dilemmas of a Trading Nation"
    author: "Mireya Solís"
    cover:
  - title: "Gödel, Escher, Bach: An Eternal Golden Braid"
    author: "Douglas Hofstadter"
    cover: "godel-escher-bach.jpg"
---

{% include base_path %}

Books I've read, am reading, and plan to read.

{% assign sections = "currently_reading:Currently Reading|read:Read|up_next:Up Next" | split: "|" %}
{% for section in sections %}
{% assign parts = section | split: ":" %}
{% assign key = parts[0] %}
{% assign books = page[key] %}

## {{ parts[1] }}

<div class="book-grid">
{% for book in books %}
<figure class="book-card">
{% if book.cover %}<img class="book-card__cover" src="{{ base_path }}/images/books/{{ book.cover }}" alt="Cover of {{ book.title | escape }}" loading="lazy">{% else %}<div class="book-card__cover book-card__cover--blank" role="img" aria-label="Cover of {{ book.title | escape }}"><span>{{ book.title | escape }}</span></div>{% endif %}
<figcaption><cite>{{ book.title | escape }}</cite><span class="book-card__author">{{ book.author | escape }}</span>{% if book.translator %}<span class="book-card__translator">trans. {{ book.translator | escape }}</span>{% endif %}</figcaption>
</figure>
{% endfor %}
</div>
{% endfor %}
