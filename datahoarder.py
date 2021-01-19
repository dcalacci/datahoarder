import requests, json, re, time, itertools, datetime, sys, os, subprocess
import config as c
from random import randint

after = ''
data = list()
user_agent = 'Python.Find_links'+ ':v0.1 (by /u/' + c.reddit_user + ')'


def pullurl(s):
    # regex for urls generally
    rx = "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
    return re.findall(rx, s)

def parseUrls(s):
    urls = pullurl(s)
    urlStrings = []
    for u in urls:
        # our regex splits into http, domain, and path
        urlStrings.append("{}://{}{}".format(u[0], u[1], u[2]))

    # ensure unique
    return list(set(urlStrings))

def find(key, dictionary):
    if not isinstance(dictionary, dict):
        return {}
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result


for thread in c.reddit_threads:
    print("processing thead {}".format(thread))
    headers = {'user-agent': user_agent}

    res = requests.get(thread + 'comments.json', headers=headers)
    res = res.json()

    for json in res:
        output = json['data']['children']
        bodies = [list(find('body', o)) for o in output]
        data = data + bodies
     
    #Wait between 10 and 15 seconds to (?) prevent reddit from blocking the script
    time.sleep(10 + randint(0,5))

data = list(itertools.chain(*data))
allUrls = list(itertools.chain(*[parseUrls(d) for d in data]))
print('found {} total URLs. Pulling media...'.format(len(allUrls)))

curtime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')

urlfile = "data/allurls_{}.txt".format(curtime)
# write parsed urls to file
with open(urlfile, 'w') as f:
    for url in allUrls:
        f.write(url + "\n")

print("parsed URLs from pages. Downloading media...")

# use you-get to download all the media we can
if not os.path.exists('data/media'):
    os.mkdir("data/media")
with open(urlfile, 'r') as f:
    urls = [l.strip() for l in f.readlines()]
    for u in urls:
        subprocess.run(['you-get', '-a', '-o', 'data/media', u])
