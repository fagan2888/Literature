import sys, re
from collections import Counter

upper_counter = Counter()
total_counter = Counter()
document_frequencies = Counter()
lines = 0

for line in open(sys.argv[1]):
    (id, tags, text) = line.split("\t")

    tokens = re.findall(r"\w[\'\-\w]*\w", text, re.UNICODE)
    lower_tokens = re.findall(r"\w[\'\-\w]*\w", text.lower(), re.UNICODE)
    
    for token in tokens:
        lc_token = token.lower()
        if lc_token != token:
            upper_counter[lc_token] += 1
        total_counter[lc_token] += 1

    lower_counts = Counter(lower_tokens)
    
    for lc_token in lower_counts:
        document_frequencies[lc_token] += 1

    lines += 1

for lc_token_pair in document_frequencies.most_common():
    lc_token = lc_token_pair[0]
    if document_frequencies[lc_token] > lines * 0.2:
        print lc_token
    elif upper_counter[lc_token] > total_counter[lc_token] * 0.9:
        print lc_token




        

