#jwl4vg Jack Lesemann

import re

# any number of
nospace_r = r'\S+'

# starts with a quote then no space. ends with a quote with no space before it
quotation_r = r'"\S^\s\S"'

nospace = re.compile(nospace_r)
quotation = re.compile(quotation_r)


