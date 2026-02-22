#  Firstly I am importing some libraries which will be required:
#  sys :- to take command  line arguments 
#  requests :- to download websites from internet
#  bs4 : to parse html , there we need title, Body, Links that's why I used here
#  urljoin : to print each url in proper way(Basicall relative links to absolute url).
# urllib3 :- to avoid local system issue, by disabling it..

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# this funcn will fetch html page by taking url as input
def to_get_page(url):                               
    headrs = {                                            # I was getting forbidden error while giving wikipedia link as input thats why i have used fake idntity 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    responses = requests.get(url, headers=headrs, verify=False)   # here I passed headers properly, and verify=false because I was getting an SSL certificate verification error in my environment that's why i disabled ssl verification to allow request to complete.
    responses.raise_for_status()   # if there will be any error like that 404 or 500 or any other in this case it will raise error.
    return responses.text      # now I'm returning content of html


# Now this funcn will fetch the title of the page.
def to_get_title(soup):
    if soup.title: # if there is title then it will return by converting it into string and by removing space.
        return soup.title.string.strip()
    return "No Title Found"  # otherwise it will return not found


# now this funcn will fetch whole content of the page by passing input as parsed html object in this funcn
def to_get_body_contents(soup):
    text = soup.get_text(separator="\n")
     
    # remove extra blank lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    return "\n".join(lines)

# Now this funcn will extract links of that page 
def to_get_links(soup, base_url):
    links = []
    for tag in soup.find_all("a", href=True): # currently by iterating over we are finding anchor tags and basically those which are containing href
        full_url = urljoin(base_url, tag["href"]) # now here we are doing conversion of relative url to absolute url.
        links.append(full_url)
    return links


# this is the main funcn starting point of my program
def main():
    if len(sys.argv) != 2:  # here i have checked for length =2 becz at first index there will pe py file and second one will be link
        print("Usage: python script.py <URL>")
        return
    
    url = sys.argv[1]  # from command line fetching url
    
    html = to_get_page(url)        #html content fetch\

    if not html:   # small safety check
        return

    soup = BeautifulSoup(html, "html.parser") # now parsing html
    
    print("Title:\n")    
    print(to_get_title(soup)) # now print title
    
    print("\nBody:\n")
    print(to_get_body_contents(soup))  # noow print body text
    
    print("\nLinks:\n")
    for link in to_get_links(soup, url):
        print(link)  # now print all links


if __name__ == "__main__":   # it will ensure that if file will direct run then main will be executed 
    main()