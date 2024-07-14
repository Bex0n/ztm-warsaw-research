# ztm-warsaw-research

![Alt Text](notebooks/vehicle_9424_tracking.gif)


**ztmwarsaw** is a Python package created to make analyzing Warsaw's public transport data a breeze. The goal is to make data collection quick and simple, helping anyone interested to easily dig into how the city moves.

## Installation

Getting started with **ztmwarsaw** is easy. You can install it directly from the source using pip or with the convenience of a Makefile.

### Install with pip

To install the package in editable mode (which means you can make changes to the source code and have them immediately reflected in the installed package), use:

```bash
pip install -e .
```

## Usage

Here's a quick example to get you started:

```python
from ztmwarsaw.api.BusCaller import BusCaller
from ztmwarsaw.tracker.BusTracker import BusTracker

buscaller = BusCaller(apikey=<YOUR API KEY HERE>)
bustracker = BusTracker(buscaller)
bustracker.track(duration=180, frequency=10, filepath="data.txt")
```

## Testing

To run tests, ensure you have the necessary testing libraries installed Then, you can use the following command:

```bash
make test
```

## License

**ztmwarsaw** is released under the [MIT License]. See the LICENSE file for more details.
