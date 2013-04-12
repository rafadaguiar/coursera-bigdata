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
    for line in value.splitlines():
        for word in line.split():
            yield word.lower(), 1


def reducefn(key, value):
    return key, len(value)
