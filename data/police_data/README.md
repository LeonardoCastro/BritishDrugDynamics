# Police data

## Drug related data

Police forces publish an important number of data each year. In this case, we are interested in data related to illicit drugs activities. At this moment, we have collected the reported [seizures involving illicit drugs](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/police_data/seizures) with local polices resolution per year. Respectively, we have also collected the [total amount of drugs captured](https://github.com/LeonardoCastro/BritishDrugDynamics/tree/master/data/police_data/quantities) in seizures over the whole fiscal year.

Drugs are classified in three different classes according to the Misuse of Drugs Act 1971. Drugs can be included and reclassified over time. The most important ones for this study are:
- Class A: Cocaine (kg), Crack (kg), Ecstasy (doses), Heroin (kg), LSD (doses), Methadone (doses), Morphine (doses).
- Class B: Herbal Cannabis (kg), Cannabis Resin (kg), Cannabis Plants (plants), Amphetamines (kg), Barbiturates (doses).
- Class C: Anabolic steroids (kg), Benzodiazephines (doses), GHB (doses), Ketamine (kg), Temazepam (doses).

The (kg) or (dose) is the unit used by the police to measure the quantity seized.

Another important aspect that we have included is [the details about the size of the seizures, by kg, doses or plants, from 2010 to 2019](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/weights_EW). These files are for England and Wales as a whole.

**Source:** [Home Office](https://www.gov.uk/government/collections/seizures-of-drugs-in-england-and-wales) and [data.police.gov.uk](https://data.police.uk/).

## Police workforce data

We also include the [mean](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_mean.csv) and [standard deviation](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_std.csv) of police officers over each year from fiscal years 2009-2010 to 2018-2019. [data.police.gov.uk](https://data.police.uk/) publishes twice a year a report about the 45 police forces acting in England and Wales. We compiled a time series of the active officers from the start to the end of a specific year, for 41 forces acting in England. We also included the same police workforce information for every 100 thousands inhabitants [here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_mean_100k.csv) and [here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/local_resolution/workforce/workforce_mean_100k.csv).

We have also included a separate file including [the workforce for England and its nine regions from 2010 to 2019](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_mean_England_and_regions.csv) and its [standard deviation](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_std_England_and_regions.csv), with their respective files with number for every 100 thousands inhabitants ([here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_mean_England_and_regions_100k.csv) and [here](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data/national_resolution/workforce_std_England_and_regions_100k.csv)).

**Note:** We have not included any standard deviation for the fiscal year 2008-2009 as there is no published data about that year. However, we included the number of active officers by March 2009.

**Source:** [Home Office](https://www.gov.uk/government/collections/police-workforce-england-and-wales)
