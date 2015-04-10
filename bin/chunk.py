import sys

metadata = dict()

for line in open("metadata.tsv"):
    fields = line.split("\t")
    metadata[ fields[0] ] = fields

for i in range(1, len(sys.argv)):
    tokens = []
    chunk = 1
    filename = sys.argv[i]

    title = metadata[ filename ][1]

    tag = "NOT_HISTORY"
    if "history" in title:
        tag = "HISTORY"

    display_filename = filename.replace("txt/", "").replace(".txt", "")

    for line in open(filename):
        tokens.extend(line.replace("--", " ").rstrip().split())

        if len(tokens) > 1000:
            chunk_name = "{0}_{1}".format(display_filename, chunk)
            print "{0}\t{1}\t{2}".format(chunk_name, tag, " ".join(tokens))
            tokens = []
            chunk += 1

    ## Get the last chunk
    chunk_name = "{0}_{1}".format(display_filename, chunk)
    print "{0}\t{1}\t{2}".format(chunk_name, tag, " ".join(tokens))

