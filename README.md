# HBV-BMI

Basic Model Interface (BMI) HBV model compatible with [eWaterCycle](https://github.com/eWaterCycle)

 HBV (Hydrologiska Byråns Vattenbalansavdelning) is a conceptual hydrological model. For more information on it's history, see this [paper](https://hess.copernicus.org/articles/26/1371/2022/).

This current implementation is _without_ a snow reservoir. 

Actual eWatercycle model wrapper can be found on [github](https://github.com/Daafip/ewatercycle-hbv)


## seperate use
Can also be used as a standalone package in theory:

```console
pip install HBV
```

Then HBV becomes available as one of the eWaterCycle models

```python
from HBV import HBV

model = HBV()

....
```

Be aware of the non intuitive [BMI](https://github.com/eWaterCycle/grpc4bmi) implementation as this package is designed to run in a [docker](https://github.com/Daafip/HBV-bmi/pkgs/container/hbv-bmi-grpc4bmi) container. 


