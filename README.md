# Discovering dynamics of the illicit drug market in the UK

**Proposed title:** Understanding, Predicting and Preventing Drug-related Problems in the UK: A Data-centric Approach

**Authors**: Leonardo Castro Gonzalez (UoB/ATI), [Ganna Pogrebna](http://www.gannapogrebna.com/) ([UoB](https://www.birmingham.ac.uk/staff/profiles/business/pogrebna-ganna.aspx)/[ATI](https://www.turing.ac.uk/people/researchers/ganna-pogrebna))

The aim of this project is to explore the illicit drug market in the UK using different sources of open data. The project is still in an early phase and it will be updated as frequent as possible, depending on the advances obtained.

****Update:**** There will be a poster of the project displayed in the [AI-UK conference](https://www.turing.ac.uk/ai-uk) organised by the Alan Turing Institute (March 24 and 25, 2020).

## Content
- At the moment we are only uploading the database comprised of the NHS data, ONS data, and a provisional [Local Authorities](https://en.wikipedia.org/wiki/Local_government_in_England) list allowing to homogenise different NHS databases.

## Database

The present data was compiled from different open-source websites. Data was not altered, and was only compiled in an _ad hoc_ database for the purposes of our project.  

**Sources:**

- [NHS Statistics on Drug Misuse (England only)](https://digital.nhs.uk/data-and-information/publications/statistical/statistics-on-drug-misuse)

- [Ministry of Housing, Communities & Local Government - English indices of deprivation (England only)](https://www.gov.uk/government/collections/english-indices-of-deprivation)

**Geographical locations:**

Up until the [Health and Social Care Act 2012](https://en.wikipedia.org/wiki/Health_and_Social_Care_Act_2012), the administrative bodies of the NHS was divided in _Strategic Health Areas_ ([SHAs](https://en.wikipedia.org/wiki/Strategic_health_authority)). Within these areas, we could find the _Primary Care Trusts_ ([PCTs](https://en.wikipedia.org/wiki/NHS_primary_care_trust)), which was a second division of the SHAs to cover the whole territory. Before their abolition, there were 10 SHAs and 152 PCTs covering England. With the Health and Social Care Act 2012, the administrative responsibilities were then passed to the [Local Authorities](https://en.wikipedia.org/wiki/Local_government_in_Englan) in England, resulting in 151 bodies.

In order to have a homogenised database that comprises pre-2012 and post-2012 data, we compiled [a list of both PCTs and Local Authorities](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md), allowing us to obtain a homogenised list of 134 England zones.

**NHS hospital admissions:**

Data on Drug Misuse was compiled for three different cases of hospital admissions. The timeframe spans from the fiscal year 2008/2009 to the fiscal year 2018/2019. There are numbers for each Merged Location described in the [locations.md](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md) file.

- [1] NHS hospital finished admissions where there was a **primary diagnosis of drug related mental health and behavioural disorders**, by region and merged location.

- [2] NHS hospital finished admission episodes with a **primary or secondary diagnosis of drug related mental and behavioural disorders**, by region and merged location.

- [3] NHS hospital finished admissions where a **primary diagnosis of poisoning by drugs**, by region and merged location.

In addition to the total number of admissions by region and merged locations from 2008 to 2019, we also have the total number of admissions by primary diagnosis and by age group. We present the data available in the following table, showing the timeframe and the geographical resolution (merged locations, regions, national)

|   | Primary diagnosis  | Age group          |
|---|--------------------|--------------------|
|[1]| 2008-2019, national| 2008-2019, national|
|[2]| -                  | 2008-2019, national|
|[3]| 2012-2019, national| 2008-2019, national|

**Deprivation levels:**

## Bulletpoints for methods and objectives

- Public health data allows to geographically locate misuse, overdoses and drug-related diagnostics.
- Crosslinked with levels of deprivation and population, we obtain a comprehensive database that spans from 2013 to 2018.
- **_note_:** Actual work consists in homogenise older databases to increase our temporal span to 2008-2018.
- Visualisation of the data in understandable and interactive maps.
- Analyse data to predict sensitive counties to public health (and violence?) problems. This would be done using Machine Learning in combination with geographical networks models ([BLV model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607465/)).
- Create a set of recommendations for public policy with respect to our results.
