import dask.array
import intake.catalog.base
import intake.container.base
import intake_xarray.base
import xarray

class MockupDataSource(intake_xarray.base.DataSourceMixin):
    container = 'xarray'
    name = 'mockup'
    version = '0.0.1'
    partition_access = True
    def __init__(self, *args, **kwargs):
        self._ds = None  # set by _open_dataset below
        self.urlpath = ''  # Work around assumption in intake-xarray we should generalize.
        super().__init__(*args, **kwargs)

    def _open_dataset(self):
        data_array = xarray.DataArray(dask.array.random.random((5000000,)))
        self._ds = xarray.Dataset({'x': data_array})
