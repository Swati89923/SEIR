# SEIR

This program takes a URL as a command line argument and then fetch webpages, and will prints:
 * Page Title (without html tags)
 * Page Body (plain text and I tried to remove html tags.
 * ALL urls that the page links to

The program uses the requests library to fetch the webpage and BeautifulSoup to parse HTML content.

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
