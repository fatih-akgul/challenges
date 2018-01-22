from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open("rss.xml") as rss_file:
        return TAG_HTML.findall(rss_file.read().lower().replace('-', ' '))


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common(TOP_NUMBER)


def _is_junk(check_str: str):
    return check_str is None or check_str.strip() == ""


def get_similarities(check_tags: list):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    similarities = []
    check_tags.sort()
    for t1, t2 in product(check_tags, check_tags):
        if t1 != t2 and (t1, t2) not in similarities and (t2, t1) not in similarities \
                and SequenceMatcher(_is_junk, t1, t2).ratio() > SIMILAR:
            similarities.append((t1, t2))
    return similarities


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
