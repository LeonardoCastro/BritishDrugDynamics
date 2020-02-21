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



## Bulletpoints for methods and objectives

- Public health data allows to geographically locate misuse, overdoses and drug-related diagnostics.
- Crosslinked with levels of deprivation and population, we obtain a comprehensive database that spans from 2013 to 2018.
- **_note_:** Actual work consists in homogenise older databases to increase our temporal span to 2008-2018.
- Visualisation of the data in understandable and interactive maps.
- Analyse data to predict sensitive counties to public health (and violence?) problems. This would be done using Machine Learning in combination with geographical networks models ([BLV model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607465/)).
- Create a set of recommendations for public policy with respect to our results.
