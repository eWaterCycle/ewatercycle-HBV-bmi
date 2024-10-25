import xarray as xr
from pathlib import Path
import json
import dask


def read_config(config_file: str) -> dict:
    with open(config_file) as cfg:
        config = json.load(cfg)
    return config


def load_var(ncfile: str | Path, varname: str) -> xr.DataArray:
    """Load the precipitation data file generated by GenericLumpedForcing.


    .. code-block:: python

        from ewatercycle.base.forcing import GenericLumpedForcing

        shape = Path("./src/ewatercycle/testing/data/Rhine/Rhine.shp")
        cmip_dataset = {
            "dataset": "EC-Earth3",
            "project": "CMIP6",
            "grid": "gr",
            "exp": ["historical",],
            "ensemble": "r6i1p1f1",
        }

        forcing = GenericLumpedForcing.generate(
            dataset=cmip_dataset,
            start_time="2000-01-01T00:00:00Z",
            end_time="2001-01-01T00:00:00Z",
            shape=shape.absolute(),
        )

        data = load_precip(forcing.directory / forcing.pr)
    """
    with dask.config.set(scheduler="synchronous"):
        data: xr.Dataset = xr.load_dataset(ncfile)

    if "time" not in data.dims:
        msg = "No time dim in data!"
        raise ValueError(msg)
    if varname not in data.dims:
        msg = f"Variable '{varname} is missing from the forcing data!"
        raise ValueError(msg)

    da = data[varname]

    if "unit" in da.attrs:  ## CF-convention is 'units' not 'unit'
        da.attrs["units"] = da.attrs.pop("unit")

    if "units" in da.attrs:  # Must have units attr to be able to check
        if da.attrs["units"] in ["kg m-2 s-1", "kg s-1 m-2"]:
            with xr.set_options(keep_attrs=True):
                da = da * 86400
            da.attrs.update({"units": "mm/d"})
        elif da.attrs["units"] == "K":
            with xr.set_options(keep_attrs=True):
                da -= 273.15
            da.attrs.update({"units": "degC"})

    return da
