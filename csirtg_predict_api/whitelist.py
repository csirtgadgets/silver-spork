import os, sys
import re

me = os.path.dirname(__file__)

WHITELIST_PATH = '%s/../data/whitelist.txt' % me
if os.path.exists(os.path.join(sys.prefix, 'csirtg_predict_api', 'data', 'whitelist.txt')):
    WHITELIST_PATH = os.path.join(sys.prefix, 'csirtg_predict_api', 'data', 'whitelist.txt')

elif os.path.exists(os.path.join('usr', 'local', 'csirtg_predict_api', 'data', 'whitelist.txt')):
    WHITELIST_PATH = os.path.join('usr', 'local', 'csirtg_predict_api', 'data', 'whitelist.txt')


GOOD = {
    'csirtg.io',
}

with open(WHITELIST_PATH) as F:
    for l in F.readlines():
        GOOD.add(l.strip('\n'))

LOOKUPS = []
for G in GOOD:
    LOOKUPS.append(re.compile(r'^(.*\.)?%s' % G))


def lookup(d):
    for l in LOOKUPS:
        if l.search(d):
            return True

    return False
