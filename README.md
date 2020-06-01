# Discovering dynamics of the illicit drug market in England

**Authors**: [Leonardo Castro-Gonzalez](https://leonardocastro.github.io/about/) (UoB/ATI), [Ganna Pogrebna](http://www.gannapogrebna.com/) ([UoB](https://www.birmingham.ac.uk/staff/profiles/business/pogrebna-ganna.aspx)/[ATI](https://www.turing.ac.uk/people/researchers/ganna-pogrebna)) and Prof. [Weisi Guo](https://www.weisiguo.com/cv) ([Cranfield](https://www.cranfield.ac.uk/people/professor-weisi-guo-24667823)/[ATI](https://www.turing.ac.uk/people/researchers/weisi-guo))

**Update:** A virtual poster will be presented at the [AI UK Conference | 2020 Digital poster exhibition](https://www.turing.ac.uk/events/ai-uk-2020-digital-poster-exhibition) on the 2nd of June, 2020. The poster was going to be presented at the [AI UK Conference](https://www.turing.ac.uk/ai-uk) (24 - 25 March, 2020) before it was postponed.

The illicit drug market in the UK has evolved in past decade, giving birth to new models of drug supply models like deep-web online sales and the county lines model. Combined with a declining workforce from the different polices in the UK, getting a clear snapshot of the supply routes is becoming increasingly difficult. Using open data from the government for England, the aim of this project is to understand how these new supply models evolve over time. By doing this, we aim to understand the geographic structure of the demand of illicit-drugs and project the future routes with high risk of being overtaken by illicit drug suppliers.

Given the availability of data, this analysis is at the moment centred in England.

## Content

This repository serves a public database for the project. All data is included in the directory [`data/`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data). In it we include [demographic](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/demographic), geographic*, [police](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/police_data) and [NHS](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/data/drugs_usage) data.

In order to homogenise the geographic analysis with the resolution used by government data, we created our own division of England based. This division (or topology) of England can be seen in the directory [`tables`](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/tables).

*: Geographic data (`.geojson` files) are at the moment not present in the repository, as the files are too large (>250mb). Because of [GitHub large files management](https://help.github.com/en/github/managing-large-files/working-with-large-files), we are not uploading it until a better solution is found.

## License and sources

This repository has an [MIT License](https://github.com/LeonardoCastro/BritishDrugDynamics/blob/master/LICENSE.md). However, all data compiled here comes from different United Kingdom government offices, published under the [Open Government License for public sector information](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).


**Sources:**
- [NHS digital](https://digital.nhs.uk/data-and-information/publications/statistical/statistics-on-drug-misuse)
- The [ONS people and community](https://www.ons.gov.uk/peoplepopulationandcommunity/)
- The [ONS geoportal](https://geoportal.statistics.gov.uk/search?collection=Document&sort=name&tags=all(MAP_ADM))
- [data.police.gov.uk](https://data.police.uk/)
