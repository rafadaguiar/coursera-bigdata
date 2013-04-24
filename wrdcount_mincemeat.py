### wrdcount.py
# server


import glob
import mincemeat
import time

text_files = glob.glob('hw3data/c0001')


def file_contents(file_name):
    try:
        f = open(file_name)
        return f.read()
    except IOError:
        print 'cannot open', file_name
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
              for file_name in text_files)

f = open('outfile', 'w')


def final(key, value):
    print key, value
    f.write(str((key, value)))

# client


def mapfn(key, value):
    # mapfn does not get outside imports
    from models.parser import parse_entry
    from models.stopwords import allStopWords, replace_all

    w = {}

    for line in value.splitlines():
        d = parse_entry(line)
        title = replace_all(d['title'])
        for word in title and word not in allStopWords:
            word = word.lower()
            if word in w.keys():
                w.update({word: w.get(word)+1})
            else:
                w[word] = 1
    for k in w.keys():
        yield k, w[k]


def reducefn(key, value):
    return key, sum(value)

# Start Server
starttime = time.time()
s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn
results = s.run_server(password="mylla")
print results
print (time.time() - starttime)/60, "min"
