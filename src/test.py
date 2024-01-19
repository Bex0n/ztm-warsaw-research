from ztmwarsaw.api.bus_caller import BusCaller

buscaller = BusCaller(apikey="54b839d9-364d-4877-ae15-a624352175a3")
params = {
    "type": 1,
    "line": 157
}
try:
    result = buscaller.get_location(params)
    print(result)
except Exception as e:
    print("Bus caller error:", e)
