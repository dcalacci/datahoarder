# datahoarder

Quick and dirty python script to scrape media content (pictures, videos) embedded in any links in Reddit thread comments. I wrote this on Jan 6th, 2021, the day the US capitol was mobbed, to collect social media and livestream videos people posted to crowdsourced threads on Reddit.

Uses the Reddit json API and uses [you-get](https://pypi.org/project/you-get/) to download
media.

## How it works

For every comment in each thread listed in `config.py`, it uses a regular expression to
identify URLs. It then uses `you-get` on each URL to pull any photos or videos we find on the
site.

When you run the script, it'll create a file, e.g. `data/allurls_2021-01-06_19:45:03.txt`,
indicating the time it was run. This is a newline-separated list of every URL pulled from all
the threads from `config.py`.

Each piece of media found is then stored in the `data/media` directory, with its filename
from the source site. `you-get` skips repeat files, so if you run this several times in a
short time period, it won't re-download media or overwrite media you've already downloaded.

## Specify reddit threads

To specify reddit threads to scrape, add them to the array in `config.py`. As of this
writing, it's set up to scrape a selection of megathreads posted after the US Capitol
insurrection on January 6, 2021:

```python
reddit_threads = [
        "https://www.reddit.com/r/AccidentalRenaissance/comments/kryhzt/us_capitol_protests_megathread_please_post_all/",
        "https://www.reddit.com/r/DataHoarder/comments/krx449/megathread_archiving_the_capitol_hill_riots/",
        "https://www.reddit.com/r/news/comments/krvwkf/megathread_protrump_protesters_storm_us_capitol/",
        "https://www.reddit.com/r/politics/comments/kryi79/megathread_us_capitol_locked_down_as_trump/",
        "https://www.reddit.com/r/PublicFreakout/comments/khs5k2/happening_now_trump_supporters_trying_to_destroy/",
        "https://www.reddit.com/r/news/comments/krue9q/capitol_police_order_evacuation_of_some_capitol/",
        "https://www.reddit.com/r/Conservative/comments/krxl6t/for_those_of_you_comparing_these_protests_to/",
        "https://www.reddit.com/r/PublicFreakout/comments/krx7yw/the_police_opened_the_gates_for_capitol_rioters/",
        "https://www.reddit.com/r/news/comments/krzopk/megathread_part_2_trump_supporters_storm_us/",
        "https://www.reddit.com/r/stupidpol/comments/kruuvf/trump_fedayeen_group_sperging_out_and_rioting_at/"
        ]
```

## To run

```bash
pip install -r requirements.txt
python datahoarder.py
```
