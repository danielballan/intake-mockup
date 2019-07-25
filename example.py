import intake
local_cat = intake.open_catalog('catalog.yml')
local_datasource = local_cat['example']
remote_cat = intake.open_catalog('intake://localhost:5000')
remote_datasource = remote_cat['example']
