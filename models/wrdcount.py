### wrdcount.py
# server


import glob

text_files = glob.glob('Gutenberg Small/*.txt')


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
    w = {}
    for line in value.splitlines():
        for word in line.split():
            word = word.lower()
            if word in w.keys():
                w.update({word: w.get(word)+1})
            else:
                w[word] = 1
    for k in w.keys():
        yield k, w[k]


def reducefn(key, value):
    return key, sum(value)
