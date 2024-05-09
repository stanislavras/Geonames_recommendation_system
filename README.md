# Geonames recommendation system

## Project status

Done.

## Task 

To create a recommendation system that receives a random city name as a query and returns a list of tuples with recommended names in unified spelling and geonameid's for these locations.

## Project description 

The career center needs to be able to match random city names with the unified geonames for internal use. The cities in question might be located in Russia, Belarus, Armenia, Kazakhstan, Kyrgyzstan, Georgia or Serbia. The operator should receive a list of recommended names which also contains a geonameid, a region, a country and a cosine similarity score for each city name. 

Four datasets are merged into one full dataset, which is then filtered for the required countries and the working dataset is created. A function for translating cities names from any language into Latin is written and applied to the `name` column. The `name` column of the working dataset is also cleared from any special symbols and internet links.

A decision is made to use the Sentence Transformer for the task. Embeddings are created using LaBSE. Semantic search for the 'Санкт-Петербург' query demonstrates a suitable match ('Sankt-Petersburg') in the first row with the score of 0.96 and an optimal match ('Saint Petersburg') in the fourth row with the score of 0.95.

The resulting dataset is sorted by the population and converted into the list of tuples as per requirement. The `geoname` function is created for optimizing the further use of the solution.

Five random queries are chosen from the test dataset and tried with the `geonames` function. For all five queries the solution finds a location with the correct geonameid in the first row. In terms of spelling, one is a full match with the recommended geoname (score=0.95); three have a minor difference of one letter each (scores from 0.91 to 0.93); and one is a bit off (score=0.89), but still fully recognizable. 

All in all, considering that the solution will be used as a recommendation system for a human operator, the Sentence Transformer works quite well for this task and will be suitable for the customer's needs.

 
The test dataset is loaded. Five random queries are chosen from it and tested with the `geonames` function. For all five queries the solution finds a location with the correct geonameid in the first row. In terms of spelling, "Новоалтайск" is a full match with the recommended geoname (score=0.95); "Каспийск", "Павловск" and "Уссурийск" have a minor difference of one letter each (scores from 0.91 to 0.93); "Ахалцихе" is a bit off (score=0.89), but still fully recognizable. 

Considering that the algorithm will be used as a recommendation system for a human operator, the Sentence Transformer based solution works quite well and might be used for the designated task.

## Data description

Datasets from download.geonames.org which contain geonameid's, region and country info, etc. (admin1CodesASCII, alternateNamesV2, cities15000, countryInfo).

## Used libraries
*pandas*

*re*

*sentencetransformer*

*sqlalchemy*
