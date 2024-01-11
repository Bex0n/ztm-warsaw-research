import json

from .api_caller import APICaller
from urllib.request import urlopen


class BusCaller(APICaller):
    def __init__(self):
        APICaller.__init__(self)

    def build(self,
              url='https://api.um.warszawa.pl/api/action/datastore_search',
              api_key=None):
        self.url = url
        self.api_key = api_key

    def call(self, *args):
        with urlopen(self.url) as url:
            response = url.read()
        return json.loads(response.decode("utf-8"))
