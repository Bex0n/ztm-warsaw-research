from .api_caller import APICaller
import urllib


class BusCaller(APICaller):
    def __init__(self):
        APICaller.__init__(self)

    def build(self, url='https://api.um.warszawa.pl/api/action/datastore_search'):
        self.url = url

    def call(self, **kwargs):
        fileobj = urllib.urlopen(self.url)
        return fileobj.read()
