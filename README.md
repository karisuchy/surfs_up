# Surfs_up

## Overview

The goal of this project is to help others develop a plan to open a Surf n' Shake Shop on Hawaii's [which island?] island. The shop will serve surf boards and ice cream to locals and tourists. 

I analyzed weather patterns to make sure precipitation and temperatures are ideal for this type of shop.   

## Resources

- Data Sources:climate_analysis.ipynb, hawaii.sqlite  
- Software: Python 3.7, VS Studio Code 1.62.3, Jupyter 6.3.0, Pandas 1.2.4, SQLite, SQLAlchemy, Flask 

## Results


### Precipitation
After importing dependencies, I set up SQLAlchemy and developed code to look at 12 previous months of precipitation. 

![image](https://user-images.githubusercontent.com/90162669/142765463-5dabc870-6e91-4e57-bf93-125af1914e47.png)


### Temperatures

I next looked at temperatures and created a histogram to summarize the frequency of temperature ranges over the previous year. By looking at the bins to the right of 67 degrees, we can see there were about 325 days where the temperature was at least 67 degrees Fahrenheit.   

![temp_histogram](https://user-images.githubusercontent.com/90162669/142774788-273b57ce-9fcf-438f-8b4b-2b1962b9e656.png)

### Weather by Season

Since the overall year round data looked so promising, I next looked for results for the months of June and December. 

![jun_dec_temp_chart](https://user-images.githubusercontent.com/90162669/142744770-5d942b94-2660-4bd5-8682-2f21e9c91bf4.png)

Hawaii does not experience the same seasonal temperature fluctuates as many other locales, such as my home state of Minnesota. Specific temperature comparisons between June and December are: 

- The low temperature in December is 56 degrees Fahrenheit which is 8 degrees cooler than the June low of 64.
- The high temperature in December is 83 which is only 2 degrees lower than June's high of 85.
- The average temperature in December is 71, which is only 3.9 degrees lower than June's average of 74.9. 

### Flask

The final step in this process was to use Flask to upload the results to the web for others to view as demonstrated by the examples below. 

This web page shows the daily levels of precipitation:

![image](https://user-images.githubusercontent.com/90162669/142773887-1bc72eff-a24a-40e7-99f2-06220f013a85.png)

This page shows the weather stations available for which to choose temperature data:

![flask_stations](https://user-images.githubusercontent.com/90162669/142773536-8d6a88cc-0939-44b3-97f4-f018717bb408.png)

This page shows the low, average, and high temperatures for dates specified by the user. The results below are for June 2017.

![Flask_temps_spec_dates](https://user-images.githubusercontent.com/90162669/142772057-69f35819-d461-4298-a50e-abaf66224ab3.png)

## Summary

Levels of precipitation and temperatures on the Hawaiian island of XXX are ideal for a Surf n' Shake Shop. Once potential sites have been located for this shop, I suggest looking specifically at the weather station(s) closest to the potential sites. In addition, analyzing weather data by year, for the last few years would be beneficial to understand what impact, if any, climate change has had or may have on the island in the near future.  

All information is available for review on Git Hub.
