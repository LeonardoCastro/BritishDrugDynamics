### Deprivation levels:

**Source:** [Ministry of Housing, Communities & Local Government - English indices of deprivation (England only)](https://www.gov.uk/government/collections/english-indices-of-deprivation)

Deprivation levels in the UK have been computed since 2000. During the timeframe we are analysing (2008-2019), three different reports have been published: 2010, 2015, 2019. The 2015 and 2019 versions used the same variables, while the 2010 version differs in certain aspects. We present those elements that can be homogenised for the complete timeframe used.

The 2010 version states that the results used 2008 data. This puts out the question about the time interval in which the results published are valid.

The geographical divisions has the same resolution as for the NHS database. Before 2012, the finest resolution found is the PCTs. After 2012, we can find Local Authorities and Lower Layer Super Output Areas (LSOAs). From the PCTs and the Local Authorities we can reconstruct the merged locations list described at [`Locations.md`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables/Locations.md).

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
