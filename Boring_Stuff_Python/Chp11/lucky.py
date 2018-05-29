#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
url1='https://www.google.com/search?q=' + ' '.join(sys.argv[1:])
print(url1)
res = requests.get(url1)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    url='https://www.google.com' + linkElems[i].get('href')
    print(url)
    webbrowser.open(url)

