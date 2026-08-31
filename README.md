# Flask_basic_Cd

A small Flask learning exercise from May 2021.

## What it is

A single `main.py` demonstrating basic Flask routing and Jinja templates: a route with an optional URL parameter (`/` and `/<user>` both map to the same view), a `/list` route rendering a food list, and templates for a user page, a list page, and a profile page (the profile route itself is commented out). `old_main.py` is an earlier version kept alongside it. This is a set of routing exercises, not an application with a real purpose.

## Stack

- Python, Flask
- Jinja2 templates, plain CSS

## Running it

`pip install flask`, then `python main.py` and visit `http://127.0.0.1:5000/`. Not executed as part of this review, but the code is simple enough that this should work as-is with Flask installed.

## Status

Written in May 2021 while learning Flask basics (routing, templates, URL parameters). Not maintained.
