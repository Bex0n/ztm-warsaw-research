from ztmwarsaw.api.bus_caller import BusCaller
from ztmwarsaw.tracker.bus_tracker import BusTracker

buscaller = BusCaller(apikey="54b839d9-364d-4877-ae15-a624352175a3")
bustracker = BusTracker(buscaller)

result = bustracker.track(line="157", duration=60, frequency=10, vehicle_number="9417")

print(result)
