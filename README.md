# Geonames recommendation system

## Project status

Done.

## Task 

To create a recommendation system that receives a random city name as a query and returns a list of tuples with recommended names in unified spelling and geonameid's for these locations.

## Project description 

The career center needs to be able to compare random city names with unified geonames for internal use. The cities in question might be located in Russia, Belarus, Armenia, Kazakhstan, Kyrgyzstan, Georgia or Serbia. The operator should receive a list of recommended names which also contains geonameid, region, country and cosine similarity. 

Four datasets are merged into one full dataset, which is then filtered for the required countries and the working dataset is created. The "name" column is cleared from the unnecessary symbols using Re.

A decision is made to use the Sentence Transformer for the task. Embeddings are created using LaBSE. Semantic search for a randomly chosen name 'Киров' demonstrates a match in the first line with the score of 0.9

The resulting dataset is sorted by the population and converted into the list of tuples as per requirement. The "geoname" function is created for optimizing the further use of the solution.

Five random queries are chosen from the test dataset and tested with the "geonames" function. For the Russian city names it gives a stable match inside the top 5 variants with the score ranging from 0.79 to 0.95. For the Georgian name 'Ахалцихе' the function gets a correct geonameid in the first line, but the spelling is a bit off, although still recognizable.

All in all, considering that the solution will be used as a recommendation system for a human operator, the Sentence Transformer works quite well for this task and will be suitable for the customer's needs.

## Data description

Datasets from download.geonames.org which contain geonameid's, region and country info, etc. (admin1CodesASCII, alternateNamesV2, cities15000, countryInfo).

## Used libraries
*pandas*

*re*

*sentencetransformer*

*sqlalchemy*
