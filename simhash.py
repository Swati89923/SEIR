import requests
import sys
from bs4 import BeautifulSoup
import re
# I have created a list of name STOP_WORD and addeed words as I able to add 
STOP_WORDS = [
    "the", "is", "in", "at", "of", "a", "and", "to", "for", "on", "with",
    "by", "an", "be", "this", "that", "it", "as", "are", "was", "were",
    "from", "or", "which", "but", "not", "have", "has", "had", "their",
    "its", "they", "them", "also", "can", "may", "such", "other", "than",
    "these", "those", "into", "about", "between", "within", "over"
]
# now this funcn will dowload page with the help of link 
def to_get_page(url):
    headers = {"User-Agent": "Mozilla/5.0"} # here I am giving there fake identity then site will not block ..I was facing problem that's why I have added it 
    page = requests.get(url, headers=headers, timeout=10)  # here sending request
    return page.text

# now this funcn will convert html to clear text it will be better for us in further count freq and others
def to_get_clean_text(html_code):
    soup = BeautifulSoup(html_code, "html.parser")
    for script_or_style in soup(["script", "style"]):  
        script_or_style.decompose()                  # here I am removing stylle and script tags
    full_text = soup.get_text(separator=" ")

    clean_lines = []
    for line in full_text.splitlines():  # i am removing extra empty lines
        if line.strip():
            clean_lines.append(line.strip())
            
    return " ".join(clean_lines)
# now this funcn will count word frequency
def get_word_counts(text):
    text = text.lower() # as in qn there were given that wee have not to consider cases either in lower or upper both will be considered same 
    all_words = re.findall(r"[a-z0-9]+", text)    # I am fetching only alphanumeric words
    counts = {}
    for w in all_words:
        if w not in STOP_WORDS: # ignore stop words
            if w in counts:
                counts[w] += 1
            else:
                counts[w] = 1
    return counts
# now this funcn will calculate simHash 
def calculate_simhash(word_counts):
    vector = [0] * 64  # I am initialising an array for 64 bits
    
    for word, count in word_counts.items():  #for each words
        word_hash = hash(word)  # now i am finding hash of word
        
        for i in range(64):  # chcking bit position 
            if (word_hash >> i) & 1:
                vector[i] += count  # if bit 1 then add
            else:
                vector[i] -= count  # if bit 0 then subtract
    fingerprint = 0
    for i in range(64):                   # here generating simhash 
        if vector[i] > 0:
            fingerprint |= (1 << i)
            
    return fingerprint

if __name__ == "__main__":
    if len(sys.argv) != 3:                  # checking there should be only two url 
        print("Usage: python script.py <url1> <url2>")
        sys.exit()

    link1 = sys.argv[1]
    link2 = sys.argv[2]

    try:

        # downloading html of both pages
        raw1 = to_get_page(link1)
        raw2 = to_get_page(link2)


        # now converting html to clean text
        text1 = to_get_clean_text(raw1)
        text2 = to_get_clean_text(raw2)
        
        # finding word frequency
        freq1 = get_word_counts(text1)
        freq2 = get_word_counts(text2)
        
        # now calculating simhash
        hash1 = calculate_simhash(freq1)
        hash2 = calculate_simhash(freq2)
        # calc distance
        diff = bin(hash1 ^ hash2).count("1")
        same_bits = 64 - diff
        score = (same_bits / 64) * 100  # finally calculating similarity percentage

        print(f"URL 1 unique words: {len(freq1)}")
        print(f"URL 2 unique words: {len(freq2)}")
        print(f"Similarity Score: {score:.1f}%")

    except Exception as error:
        print(f"Ohh no, Something went wrong: {error}")