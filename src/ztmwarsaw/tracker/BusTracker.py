import json
import time
from typing import Any, List, Optional

from pydantic import ValidationError
from tqdm import tqdm

from ztmwarsaw.api.ICaller import ICaller, LocationRequest
from ztmwarsaw.tracker.ITracker import ITracker


class BusTracker(ITracker):
    """
    A concrete implementation of the ITracker interface for tracking buses.
    Utilizes an API caller to fetch real-time bus location data.
    """

    def __init__(self, apicaller: ICaller):
        """
        Initializes the BusTracker with a specific API caller.

        :param apicaller: An instance of a class that implements the ICaller interface.
        """
        super().__init__(apicaller)

    def __append_to_file(self, filepath: str, data: Any) -> None:
        """
        Appends a piece of data to a file.

        :param filepath: The path to the file where data should be appended.
        :param data: The data to append to the file.
        """
        try:
            with open(filepath, "a") as f:
                json.dump(data, f)
                f.write("\n")
        except Exception as e:
            print(f"Error appending data to file: {e}")

    def track(
        self,
        *args: Any,
        line: Optional[str] = None,
        brigade: Optional[str] = None,
        duration: int = 60,
        frequency: int = 10,
        vehicle_number: Optional[str] = None,
        filepath: Optional[str] = None,
        **kwargs: Any,
    ) -> List[Any]:
        """
        Tracks bus locations for a specified duration and frequency, optionally filtering
        by line, brigade, or vehicle number. Results can be saved to a file.

        :param line: Filter by bus line.
        :param brigade: Filter by brigade.
        :param duration: The tracking duration in seconds.
        :param frequency: The frequency of data collection in seconds.
        :param vehicle_number: Filter by vehicle number.
        :param filepath: Path to a file where results will be saved.
        :return: A list of collected data points.
        """
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
                    response = self.api_caller.get_location(params)
                    if response is not None:
                        for location in response:
                            if (
                                location["VehicleNumber"] == vehicle_number
                                or vehicle_number is None
                            ):
                                result.append(location)
                                if filepath:
                                    self.__append_to_file(filepath, location)
                except Exception as e:
                    print(f"Error occurred: {e}")
                pbar.update(1)
                time.sleep(frequency)
        return result
