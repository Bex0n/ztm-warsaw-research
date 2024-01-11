from ztmwarsaw.tracker import Tracker
from ztmwarsaw.api.api_caller import ApiCaller


class BusTracker(Tracker):
    def __init__(self):
        Tracker.__init__(self)

    def build(self, api_caller: ApiCaller):
        self.api_caller = api_caller
