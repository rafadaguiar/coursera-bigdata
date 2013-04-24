import re


def parse_entry(s):
    m = re.search("(?P<dir>(\w+/)*\w+):::(?P<authors>.+):::(?P<title>.+).", s)
    d = m.groupdict()
    d['authors'] = d['authors'].split('::')
    return d
