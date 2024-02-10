import time
from typing import Any, List, Optional

from pydantic import ValidationError
from tqdm import tqdm

from ztmwarsaw.api.ICaller import ICaller, LocationRequest
from ztmwarsaw.tracker.ITracker import ITracker


class BusTracker(ITracker):
    def __init__(self, apicaller: ICaller):
        ITracker.__init__(self, apicaller)

    def track(
        self,
        *args: Any,
        line: str,
        brigade: Optional[str] = None,
        duration: int = 60,
        frequency: int = 10,
        vehicle_number: Optional[str] = None,
        **kwargs: Any,
    ) -> List[Any]:
        try:
            params = LocationRequest(line=line, brigade=brigade)
        except ValidationError as e:
            print(f"Error validating parameters: {e}")
            return []
        result = []
        iterations = int(duration / frequency)
        with tqdm(total=iterations, desc="Tracking Bus") as pbar:
            for _ in range(iterations):
                try:
                    location = self.api_caller.get_location(params)
                    if location is not None:
                        if vehicle_number is not None:
                            for vehicle in location:
                                if vehicle["VehicleNumber"] == vehicle_number:
                                    result.append(vehicle)
                        else:
                            result.append(location)
                except Exception as e:
                    print(f"Error occurred: {e}")
                pbar.update(1)
                time.sleep(frequency)

        return result
