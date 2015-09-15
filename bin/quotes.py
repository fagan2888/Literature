import sys

text = ""

for line in open(sys.argv[1]):
    text += line.rstrip() + " "

quote_segments = text.split("\"")

is_quote = False
for segment in quote_segments:
    print "{0}\t{1}\t{2}\n".format("Q" if is_quote else "N", len(segment), segment)
    ## every other segment is a quotation
    is_quote = not is_quote


