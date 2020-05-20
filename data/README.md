# Data

## Drugs usage data

We split drugs usage data depending on the geographical resolution.

### National (English) resolution

- NHS finished admissions (three types) in England (2009-2019) in [`admissions_England.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/national_resolution/admissions_England.csv).
- NHS finished admissions (three types) per 100k capita in England (2009-2019) in [`admissions_100k_England.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/national_resolution/admissions_100k_England.csv).
- Time series by age group in England (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/national_resolution/primary_age.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/national_resolution/secondary_age.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/national_resolution/misuse_age.csv) admissions.
- Primary diagnoses for [misuse admissions](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/national_resolution/misuse_diagnoses.csv) (2013-2019) and for [primary admissions](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/national_resolution/primary_diagnoses.csv) (2009-2019).

### Local resolution

We use the topology described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md).

- Time series (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/local_resolution/primary.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/local_resolution/secondary.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/local_resolution/misuse.csv) admissions.
- Time series (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/local_resolution/primary_100k.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/local_resolution/secondary_100k.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/local_resolution/misuse_100k.csv) admissions per 100k capita.

We also include a `deprecated/` directory with files containing the same information.

## Demographic data

We include the **population data in England from 2009 to 2019**. File [`population_England_and_regions.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/demographic/population_England_and_regions.csv) contains data for England and its nine regions, being these:
- East of England
- East Midlands
- London
- North East
- North West
- South East
- South West
- West Midlands
- Yorkshire and the Humber

On the other hand, file [`population_la.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/demographic/population_la.csv) contains data for the chosen topology of local authorities described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md).

**Source:** All population data is obtained from the [ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland).

## Geographic data

We include three different `geojson` files with a `name` property and a `geometry`.
The `geojson` files correspond to:
- [`England_regions.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/England_regions.geojson): 9 regions of England (see above for the names of them).
- [`England_counties.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/England_counties.geojson): topology chosen as in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md).
- [`Scotland_Wales.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/Scotland_Wales.geojson): Local authorities of Scotland and Wales to complement any map.

We also include a [`locations.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/locations.csv), which is a simil to [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md) in a `csv` format.

**Source:** All `geojson` files were processed with datasets from the [ONS](https://geoportal.statistics.gov.uk/search?collection=Document&sort=name&tags=all(MAP_ADM)).

**Current problems:** The size of the three `geojson` files are too big to display in github and github pages.
