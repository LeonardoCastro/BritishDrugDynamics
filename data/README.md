# Data

## Content and structure

This directory is divided into four different parts. Each one contains data of a specific kind as their names suggest. In the case of [`drugs_usage/deaths/`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/drugs_usage/deaths), [`drugs_usage/hospital_admissions/`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/drugs_usage/hospital_admissions), [`police_data/seizures`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/seizures) and [`police_data/workforce`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/workforce), we divided data in two: `local_resolution/` and `national_resolution/`. The former contains data with a local authority or police force resolution, while the latter contains data at regional, England or England and Wales resolution.

For more information about the data, please refer to the specific directory.

**Note:** Geographic data (`.geojson` files) is at the moment not present in the repository, as the files are too large (>250mb). Because of [GitHub large files management](https://help.github.com/en/github/managing-large-files/working-with-large-files), we are not uploading it until a better solution is found.

## Missing data

- [Deprivation levels](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/deprivation.md)
- Time series for arrests related to drugs ([data.police.gov.uk](https://data.police.uk/))
- Quality index for NHS hospitals (# of beds) ([NHS digital](https://digital.nhs.uk/data-and-information/publications/statistical/statistics-on-drug-misuse))
- Travel times from one local authority to another (Google Maps API)
