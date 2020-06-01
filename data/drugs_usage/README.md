# Drugs usage data

## NHS hospital admissions

We split drugs usage data depending on the geographical resolution.

### National (English) resolution

- NHS finished admissions (three types) in England (2009-2019) in [`admissions_England.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/admissions_England.csv).
- NHS finished admissions (three types) per 100k capita in England (2009-2019) in [`admissions_100k_England.csv`](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/admissions_100k_England.csv).
- Time series by age group in England (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/primary_age.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/secondary_age.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/misuse_age.csv) admissions.
- Primary diagnoses for [misuse admissions](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/misuse_diagnoses.csv) (2013-2019) and for [primary admissions](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/national_resolution/primary_diagnoses.csv) (2009-2019).

### Local resolution

We use the topology described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

- Time series (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/primary.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/secondary.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/misuse.csv) admissions.
- Time series (2009-2019) for [primary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/primary_100k.csv), [secondary](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/secondary_100k.csv) and [misuse](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/hospital_admissions/local_resolution/misuse_100k.csv) admissions per 100k capita.


**Source:** Finished NHS admissions data is available in the [NHS Statistics on Drug Misuse (England only)](https://digital.nhs.uk/data-and-information/publications/statistical/statistics-on-drug-misuse).

## Drug related deaths

### National resolution

We use the topology described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

- Time series (2009-2018) for deaths related to drug poisoning in England and its nine regions, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_poisoning_England_and_regions.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_poisoning_England_and_regions_100k.csv).
- Time series (2009-2018) for deaths related to drug misuse in England and its nine regions, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_misuse_England_and_regions.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_misuse_England_and_regions_100k.csv).
- Time series (2009-2018) of the total deaths in England for poisoning and/or misuse of drugs, [by age group](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_ages_England.csv).
- Time series (2009-2018) of the total deaths in England for poisoning and/or misuse of drugs, [by underlying cause when registering the death](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/deaths_underlyingCause_England.csv).
- Time Series (2009-2018) of the total deaths in England and Wales, [by drug(s) registered at the moment of death and group age](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/national_resolution/drug_age)


### Local resolution

We use the topology described in [`locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

- Time series (2009-2018) for deaths related to drug poisoning, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_poisoning.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_poisoning_100k.csv).
- Time series (2009-2018) for deaths related to drug misuse, in [total numbers](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_misuse.csv) and in [deaths per 100k inhabitants](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/drugs_usage/deaths/local_resolution/deaths_misuse_100k.csv).

**Source:** The [ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/deathsrelatedtodrugpoisoninginenglandandwales/2018registrations)
