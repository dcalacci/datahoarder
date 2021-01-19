import sys, os, subprocess

urlfile = sys.argv[1]

with open(urlfile, 'r') as f:
    urls = [l.strip() for l in f.readlines()]

    for u in urls:
        subprocess.run(['you-get', '-o', 'data/media', u])
