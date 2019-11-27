import urllib.request
import re

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')

for line in stream:
    decoded = line.decode('UTF-8').strip()

email_pattern = r"([a-zA-Z]\S.*)(at|@).*(dot|\.|DOT)(edu|EDU|ca|com|rentals)"
regex = re.compile(email_pattern)

emails = regex.findall(decoded)
