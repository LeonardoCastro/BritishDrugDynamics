# Discovering dynamics of the illicit drug market in the UK

**Proposed title:** Understanding, Predicting and Preventing Drug-related Problems in the UK: A Data-centric Approach

**Authors**: Leonardo Castro Gonzalez (UoB/ATI), [Ganna Pogrebna](http://www.gannapogrebna.com/) ([UoB](https://www.birmingham.ac.uk/staff/profiles/business/pogrebna-ganna.aspx)/[ATI](https://www.turing.ac.uk/people/researchers/ganna-pogrebna))

The aim of this project is to explore the illicit drug market in the UK using different sources of open data. The project is still in an early phase and it will be updated as frequent as possible, depending on the advances obtained.

****Update:**** There will be a poster of the project displayed in the [AI-UK conference](https://www.turing.ac.uk/ai-uk) organised by the Alan Turing Institute (March 24 and 25, 2020).

## Content
- At the moment we are only uploading the database comprised of the NHS data, ONS data, and a provisional [Local Authorities](https://en.wikipedia.org/wiki/Local_government_in_England) list allowing to homogenise different NHS databases.

## Database

The present data was compiled from different public websites. Data was not altered, and was only compiled in an _ad hoc_ database for the purposes of our project.  

### Sources:

- [NHS Statistics on Drug Misuse (England only)](https://digital.nhs.uk/data-and-information/publications/statistical/statistics-on-drug-misuse)

- [Ministry of Housing, Communities & Local Government - English indices of deprivation (England only)](https://www.gov.uk/government/collections/english-indices-of-deprivation)

### Geographical locations:

Up until the [Health and Social Care Act 2012](https://en.wikipedia.org/wiki/Health_and_Social_Care_Act_2012), the administrative bodies of the NHS was divided in _Strategic Health Areas_ ([SHAs](https://en.wikipedia.org/wiki/Strategic_health_authority)). Within these areas, we could find the _Primary Care Trusts_ ([PCTs](https://en.wikipedia.org/wiki/NHS_primary_care_trust)), which was a second division of the SHAs to cover the whole territory. Before their abolition, there were 10 SHAs and 152 PCTs covering England. With the Health and Social Care Act 2012, the administrative responsibilities were then passed to the [Local Authorities](https://en.wikipedia.org/wiki/Local_government_in_Englan) in England, resulting in 151 bodies.

In order to have a homogenised database that comprises pre-2012 and post-2012 data, we compiled [a list of both PCTs and Local Authorities](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md), allowing us to obtain a homogenised list of 134 England zones.

### NHS hospital admissions:

Data on Drug Misuse was compiled for three different cases of hospital admissions. The timeframe spans from the fiscal year 2008/2009 to the fiscal year 2018/2019. There are numbers for each Merged Location described in the [`Locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md) file.

1. NHS hospital finished admissions where there was a **primary diagnosis of drug related mental health and behavioural disorders**, by region and merged location.

2. NHS hospital finished admission episodes with a **primary or secondary diagnosis of drug related mental and behavioural disorders**, by region and merged location.

3. NHS hospital finished admissions where a **primary diagnosis of poisoning by drugs**, by region and merged location.

In addition to the total number of admissions by region and merged locations from 2008 to 2019, we also have the total number of admissions by primary diagnosis and by age group. We present the data available in the following table, showing the timeframe and the geographical resolution (merged locations, regions, national)

|   | Primary diagnosis  | Age group          |
|---|--------------------|--------------------|
|1. | 2008-2019, national| 2008-2019, national|
|2. | -                  | 2008-2019, national|
|3. | 2012-2019, national| 2008-2019, national|

### Deprivation levels:

Deprivation levels in the UK have been computed since 2000. During the timeframe we are analysing (2008-2019), three different reports have been published: 2010, 2015, 2019. The 2015 and 2019 versions used the same variables, while the 2010 version differs in certain aspects. We present those elements that can be homogenised for the complete timeframe used.

The 2010 version states that the results used 2008 data. This puts out the question about the time interval in which the results published are valid.

The geographical divisions has the same resolution as for the NHS database. Before 2012, the finest resolution found is the PCTs. After 2012, we can find Local Authorities and Lower Layer Super Output Areas (LSOAs). From the PCTs and the Local Authorities we can reconstruct the merged locations list described at [`Locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/Locations.md).

The variables that can be recovered and homogenised from the three different versions are (**descriptions from the 2019 version**):

1. **Average rank** and its respective _Rank of average rank_

    Population weighted average of the combined ranks for the LSOAs in a larger area.

    This measure is calculated by averaging all of the LSOA ranks in each larger area after they have been population weighted. The ‘average rank’ scores for the larger areas are then ranked, where the rank of 1 (most deprived) is given to the area with the highest score. (For the purpose of calculating the score for the larger area, LSOAs are ranked such that the most deprived LSOA is given the rank of 32,844.)

    The nature of this measure – using all areas, and using ranks rather than scores – means that a highly polarised larger area would not tend to score highly, because extremely deprived and less deprived LSOAs will ‘average out’. Conversely, a larger area that is more uniformly deprived will tend to score highly on the measure.


2. **Average score** and its respective _Rank of average score_

   Population weighted average of the combined scores for the LSOAs in a larger area.

   The average score summary measure is calculated by averaging the LSOA scores in each larger area after they have been population weighted. The resultant scores for the larger areas are then ranked, where the rank of 1 (most deprived) is given to the area with the highest score.

   This gives a measure of the whole area covering both deprived and non-deprived areas. The main difference from the average rank measure described above is that more deprived LSOAs tend to have more ‘extreme’ scores than ranks. So highly deprived areas will not tend to average out to the same extent as when using ranks; highly polarised areas will therefore tend to score higher on the average score measure than on the average rank.

3. **Employment and Income Scale** and their respective _Rank of employment/income scale_

   Income Scale is the number of people who are income deprived; Employment Scale is the number of people who are employment deprived.

   These measures are designed to give an indication of the number of people experiencing income deprivation and employment deprivation in the local area. For example, if two areas have the same percentage of income deprived people, the larger area will be ranked as more deprived on the income scale measure because more people are experiencing the deprivation.

4. **Extent** and its respective _Rank of Extent_

   Proportion of a larger area’s population living in the most deprived LSOAs in the country.
 
   This is a weighted measure of the population in the most deprived 30 per cent of all areas:  
   - The population living in the most deprived 10 per cent of LSOAs in England receive a ‘weight’ of 1.0;  
   - The population living in the most deprived 11 to 30 per cent of LSOAs receive a sliding weight, ranging from 0.95 for those in the eleventh percentile, to 0.05 for those in the thirtieth percentile.   

   The ‘extent’ scores for the larger areas are then ranked, where the rank of 1 (most deprived) is given to the area with the highest score. (Higher-level areas which have no LSOAs in the most deprived 30 per cent of all areas in England have a score of zero for this summary measure.)
 
   The extent measure is a more sophisticated version of the proportion of LSOAs in the most deprived 10 per cent nationally measure, and is designed to avoid the sharp cut-off seen in that measure, whereby areas ranked only a single place outside the most deprived 10 per cent are not counted at all.

5. **Local concentration** and its respective _Rank of local concentration_

   Population weighted average of the ranks of a larger area’s most deprived LSOAs that contain exactly 10% of the larger area’s population.

   The ‘local concentration’ score for the larger area is ranked, where the rank of 1 (most deprived) is given to the area with the highest score. (For the purpose of calculating the score for the larger area, LSOAs are first ranked such that the most deprived LSOA is given the rank of 32,844.)

   Similar to the proportion of LSOAs in the most deprived 10 per cent nationally and extent measures, the local concentration measure is based on only the most deprived LSOAs in the larger area, rather than on all areas. By contrast to these measures however, the local concentration measure gives additional weight to very highly deprived areas.


**Usage of deprivation levels:**

The report of the 2019 version states some very interesting insights (found in the FAQs of the 2019 version).
When talking about comparing over time:
> For example, an area can be said to have become more deprived relative to other areas if it was within the most deprived 20 per cent of areas nationally according to the IMD2015 but within the most deprived 10 per cent according to the IMD2019.

> However, it would not necessarily be correct to state that the level of deprivation in the area has increased on some absolute scale, as it may be the case that all areas had improved, but that this area had improved more slowly than other areas and so had been ‘overtaken’ by those areas.

> All of the Indices of Deprivation measure relative deprivation at small area level as accurately as possible, but they are not designed to provide ‘backwards’ comparability with previous iterations (2015, 2010, 2007, 2004 and 2000). However, because there is a broadly consistent methodology between the IoD2019 and previous versions, you can compare the rankings as determined at the relevant time point by each of the versions, as if comparing snapshots in time.




## Bulletpoints for methods and objectives

- Public health data allows to geographically locate misuse, overdoses and drug-related diagnostics.
- Crosslinked with levels of deprivation and population, we obtain a comprehensive database that spans from 2013 to 2018.
- **_note_:** Actual work consists in homogenise older databases to increase our temporal span to 2008-2018.
- Visualisation of the data in understandable and interactive maps.
- Analyse data to predict sensitive counties to public health (and violence?) problems. This would be done using Machine Learning in combination with geographical networks models ([BLV model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607465/)).
- Create a set of recommendations for public policy with respect to our results.
