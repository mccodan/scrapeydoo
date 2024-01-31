import re
from urllib.request import urlopen

'''Open denver7.com and return headlines.'''
url = "https://denver7.com"
page = urlopen(url)
html = page.read().decode("utf-8")


#Get the top 4 related stories
pattern = "BigLittle-title.*?>.*</h3>"
match_results = re.findall(pattern, html, re.IGNORECASE)

print("Related Stories:" + "\n")
for x in match_results:
    title = re.sub("<.*?>", "", x)
    title = title.removeprefix("BigLittle-title\">")
    print(title)

#Get the remaining stories
pattern = "ListItem-title.*?>.*</h3>"
match_results = re.findall(pattern, html, re.IGNORECASE)

print("\n\nOther Stories:" + "\n")
for x in match_results:
    title = re.sub("<.*?>", "", x)
    title = title.removeprefix("ListItem-title\">")
    print(title)  