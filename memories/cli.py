"""Memories

Usage:
    memories remember DB
    memories forget DB
    memories new DB

Commands:
    remember  Remember all the passed in strings
    forget    Forget all the passed in strings
    new       Given a list of passed in strings, print the ones not previously
              known. Much like a diff.

Memories simply remembers each line of text piped to it.
The idea is you can feed it a list of keys, one per line.
This way you can quickly remember, forget, or
tell what's new since the last time you remembered.

Parameters:
    DB        Path to a database file to store your memories.
"""

from docopt import docopt
from memories.version import __package_version__, __package_name__
import lmdb
import sys

def remember(arguments, db):
    for line in sys.stdin:
        line = line.strip()
        if line:
            db.put(line, '_')

def new(arguments, db):
    for line in sys.stdin:
        line = line.strip()
        if line:
            if not db.get(line):
                print(line)

def forget(arguments, db):
    for line in sys.stdin:
        line = line.strip()
        if line:
            db.delete(line)

def main():
    arguments = docopt(__doc__, version="{0} {1}".format(__package_name__, __package_version__))
    env = lmdb.Environment(arguments['DB'], subdir=False, map_size=2*1024*1024*1024)
    txn = lmdb.Transaction(env)
    for key in arguments.keys():
        if key in globals() and arguments[key]:
            globals()[key](arguments, txn.open())
    txn.commit()
