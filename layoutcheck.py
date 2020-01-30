import sys
import logging
import pathlib as pl
from collections import defaultdict


def tree():
    return defaultdict(tree)


root = tree()

for _ in open(sys.argv[1]):
    path = pl.Path(_.strip())
    _root = root
    for p in path.parts:
        _root = _root[p]

for _ in open(sys.argv[2]):
    path = pl.Path(_.strip())
    _root = root
    for p in path.parts:
        if p not in _root:
            logging.error("%s is not allowed." % _.strip())
            sys.exit(-1)
        else:
            # it's not a leaf so checking if the path is
            # compatible
            if _root[p]:
                _root = _root[p]
            else:
                # it's a leaf so no further check required
                break
