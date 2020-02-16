import sys
import os
import re
import logging

# parse options
root_dir = sys.argv[1]
exclude_dir = sys.argv[2].split(",") if len(sys.argv) >= 3 else None
exclude_files = sys.argv[3].split(",") if len(sys.argv) == 4 else None

# hard-coded regex for pattern search
rxf = re.compile("[^a-z0-9_\.\/]")

def is_ignored(entry):
    if exclude_dir is not None:
        for _ in exclude_dir:
            if _ in entry:
                return True
    if exclude_files is not None:
        for _ in exclude_files:
            if _ in entry:
                return True
    return False


# Set the directory you want to start from
for dir_name, subdir_list, file_list in os.walk(root_dir):
    if not is_ignored(dir_name):
        if rxf.search(dir_name):
            logging.error("invalid directory name: %s" % dir_name)
            sys.exit(-1)
        else:
            for fname in file_list:
                if not is_ignored(fname) and rxf.search(fname):
                    logging.error("invalid file name: %s" % os.path.join(dir_name,fname))
                    sys.exit(-1)
sys.exit(0)

