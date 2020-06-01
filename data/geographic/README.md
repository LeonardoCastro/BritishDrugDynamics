# Geographic data

We include three different `geojson` files with a `name` property and a `geometry`.
The `geojson` files correspond to:
- [`England_regions.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/England_regions.geojson): 9 regions of England (see above for the names of them).
- [`England_counties.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/England_counties.geojson): topology chosen as in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).
- [`Scotland_Wales.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/Scotland_Wales.geojson): Local authorities of Scotland and Wales to complement any map.

We also include a [`locations.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/locations.csv), which is a simil to [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md) in a `csv` format.


**Current problems:** Geographic data (`.geojson` files) is at the moment not present in the repository, as the files are too large (>250mb). Because of [GitHub large files management](https://help.github.com/en/github/managing-large-files/working-with-large-files), we are not uploading it until a better solution is found.

**Source:** All `geojson` files were processed with datasets from the [ONS](https://geoportal.statistics.gov.uk/search?collection=Document&sort=name&tags=all(MAP_ADM)).
