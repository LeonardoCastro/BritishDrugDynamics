# Data

## Drugs usage data

### NHS hospital admissions

We split drugs usage data depending on the geographical resolution.

#### National (English) resolution

- NHS finished admissions (three types) in England (2009-2019) in [`admissions_England.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/admissions_England.csv).
- NHS finished admissions (three types) per 100k capita in England (2009-2019) in [`admissions_100k_England.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/admissions_100k_England.csv).
- Time series by age group in England (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/primary_age.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/secondary_age.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/misuse_age.csv) admissions.
- Primary diagnoses for [misuse admissions](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/misuse_diagnoses.csv) (2013-2019) and for [primary admissions](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/primary_diagnoses.csv) (2009-2019).

#### Local resolution

We use the topology described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

- Time series (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/primary.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/secondary.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/misuse.csv) admissions.
- Time series (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/primary_100k.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/secondary_100k.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/misuse_100k.csv) admissions per 100k capita.


**Source:** Finished NHS admissions data is available in the [NHS Statistics on Drug Misuse (England only)](https://digital.nhs.uk/data-and-information/publications/statistical/statistics-on-drug-misuse).

### Drug related deaths

#### National resolution

We use the topology described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

- Time series (2009-2018) for deaths related to drug poisoning in England and its nine regions, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_poisoning_England_and_regions.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_poisoning_England_and_regions_100k.csv).
- Time series (2009-2018) for deaths related to drug misuse in England and its nine regions, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_misuse_England_and_regions.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_misuse_England_and_regions_100k.csv).
- Time series (2009-2018) of the total deaths in England for poisoning and/or misuse of drugs, [by age group](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_ages_England.csv).
- Time series (2009-2018) of the total deaths in England for poisoning and/or misuse of drugs, [by underlying cause when registering the death](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_underlyingCause_England.csv).
- Time Series (2009-2018) of the total deaths in England and Wales, [by drug(s) registered at the moment of death and group age](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/drug_age)


#### Local resolution

We use the topology described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

- Time series (2009-2018) for deaths related to drug poisoning, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_poisoning.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_poisoning_100k.csv).
- Time series (2009-2018) for deaths related to drug misuse, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_misuse.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_misuse_100k.csv).

**Source:** The [ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/deathsrelatedtodrugpoisoninginenglandandwales/2018registrations)

## Police data

### Drug related data

Police forces publish an important number of data each year. In this case, we are interested in data related to illicit drugs activities. At this moment, we have collected the reported [seizures involving illicit drugs](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/police_data/seizures) with local polices resolution per year. Respectively, we have also collected the [total amount of drugs captured](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/police_data/quantities) in seizures over the whole fiscal year.

Drugs are classified in three different classes according to the Misuse of Drugs Act 1971. Drugs can be included and reclassified over time. The most important ones for this study are:
- Class A: Cocaine (kg), Crack (kg), Ecstasy (doses), Heroin (kg), LSD (doses), Methadone (doses), Morphine (doses).
- Class B: Herbal Cannabis (kg), Cannabis Resin (kg), Cannabis Plants (plants), Amphetamines (kg), Barbiturates (doses).
- Class C: Anabolic steroids (kg), Benzodiazephines (doses), GHB (doses), Ketamine (kg), Temazepam (doses).

The (kg) or (dose) is the unit used by the police to measure the quantity seized.

Another important aspect that we have included is [the details about the size of the seizures, by kg, doses or plants, from 2010 to 2019](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/weights_EW). These files are for England and Wales as a whole.

**Source:** [Home Office](https://www.gov.uk/government/collections/seizures-of-drugs-in-england-and-wales) and [data.police.gov.uk](https://data.police.uk/).

### Police workforce data

We also include the [mean](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_mean.csv) and [standard deviation](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_std.csv) of police officers over each year from fiscal years 2009-2010 to 2018-2019. [data.police.gov.uk](https://data.police.uk/) publishes twice a year a report about the 45 police forces acting in England and Wales. We compiled a time series of the active officers from the start to the end of a specific year, for 41 forces acting in England. We also included the same police workforce information for every 100 thousands inhabitants [here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_mean_100k.csv) and [here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_mean_100k.csv).

We have also included a separate file including [the workforce for England and its nine regions from 2010 to 2019](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_mean_England_and_regions.csv) and its [standard deviation](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_std_England_and_regions.csv), with their respective files with number for every 100 thousands inhabitants ([here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_mean_England_and_regions_100k.csv) and [here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_std_England_and_regions_100k.csv)).

**Note:** We have not included any standard deviation for the fiscal year 2008-2009 as there is no published data about that year. However, we included the number of active officers by March 2009.

**Source:** [Home Office](https://www.gov.uk/government/collections/police-workforce-england-and-wales)


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

File [`population_la.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/demographic/population_la.csv) contains data for the chosen topology of local authorities described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

File [`population_policeforces.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/demographic/population_policeforces.csv) contains the population from 2009 to 2019 for the regions covering the 39 different local police forces in England. The list of police forces and how they relate to the topology discussed above is found in file [`Police_forces.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Police_forces.md)

**Source:** All population data is obtained from the [ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland).

## Geographic data

We include three different `geojson` files with a `name` property and a `geometry`.
The `geojson` files correspond to:
- [`England_regions.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/England_regions.geojson): 9 regions of England (see above for the names of them).
- [`England_counties.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/England_counties.geojson): topology chosen as in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).
- [`Scotland_Wales.geojson`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/Scotland_Wales.geojson): Local authorities of Scotland and Wales to complement any map.

We also include a [`locations.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/geographic/locations.csv), which is a simil to [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md) in a `csv` format.


**Current problems:** The size of the three `geojson` files are too big to display in github and github pages.

**Source:** All `geojson` files were processed with datasets from the [ONS](https://geoportal.statistics.gov.uk/search?collection=Document&sort=name&tags=all(MAP_ADM)).


## Missing data

- Deprivation levels
- time series for arrests related to drugs
- quality index for NHS hospitals (# of beds)
- travel time from one local authority to another
