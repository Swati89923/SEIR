# SEIR

##  SEIR – Assignment Repository

This repository contains academic assignments related to Search Engine & Information Retrieval (SEIR).
It includes implementation-based programs developed using Python.

Note: This repository is strictly maintained for assignment submission purposes only.
## Files Included

### Assignment1_scrap_142.py → Web Scraping Program
### simhash.py → SimHash Algorithm Implementation

 Web Scraping Program
Description
This Python program takes a webpage URL as a command-line argument, fetches the webpage, and extracts:
Page Title (clean text, without HTML tags)
Page Body (plain readable text)
All hyperlinks present on that webpage

## Libraries Used 
* sys:- to take command line input
* requests :- to download webpage content
* bs4 (BeeautifulSoup) :- to parse HTML
* urllib.parse (urljoin) :- to convert relative URLs to absolute URLs
* urllib3 :- to suppress SSL warning

## How to run 

Firstly open the folder and then run like that python Assignment1_142.py https://example.com
If the URL contains brackets, use quotes: like that python Assignment1_142.py "https://en.wikipedia.org/wiki/Python_(programming_language)"

## How it works

* The program reads the URL from the command line.
* It sends a GET request to fetch the page.
* The HTML is parsed using BeautifulSoup.
* The title, body text, and links are extracted.
* The output is printed to the terminal.

## Notes 

Some modern websites use JavaScript to load content dynamically.
In such cases, the program may not extract full content because requests does not execute JavaScript.
SSL verification was disabled in this project to avoid local certificate errors during development.


## SimHash Calculation Program
 Description

This program implements the SimHash algorithm, which is commonly used to detect similarity between documents.

### Purpose
Generate a fingerprint of textual data
Compare similarity between documents
Detect near-duplicate content

## Academic Declaration
This repository is created for academic coursework submission under SEIR.
All implementations are developed for learning and demonstration purposes.
