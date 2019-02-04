# bungalow-challenge-api

This has been my first introduction to Django, and I am so grateful for the opportunity to learn this skillset.

In the process of creating this API, I have made a few assumptions.

1. Authentication of users is not necessary, therefore all data is public and accessible by anyone.

2. Prices in the data set should be numeric for better querying. Therefore, ingesting the dataset parses values in a manner congruent with such. 

3. The given dateformat in the data set is arbitray. Therefore, dates originally in the format M/D/YYYY will be represented in responses as YYYY/M/D
