import requests
from lxml import html
from collections import Counter


class TagParser:
    def __init__(self, url):
        self.url = url

    def get_tags(self):
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        all_elems = tree.cssselect('*')
        all_tags = [elem.tag for elem in all_elems]
        return all_tags

    def tags_count(self, tags):
        tags_counter = Counter(tags)
        return tags_counter

    @property
    def parse_tags(self):
        try:
            tags = self.get_tags()
        except:
            return {'Error': True}
        tags_quantity = self.tags_count(tags)
        return tags_quantity
