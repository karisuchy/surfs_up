# surfs_up

## Overview

The goal of this project is to help otherws develop a plan to move to open a Surf n' Shake Shop in [which island?] Hawii. The shop will serve surf boards and ice cream to locals and tourists. I analyzed weather patterns to make sure precipitation and temperatures are ideal for this type of shop.   

## Resources

- Data Sources:climate_analysis.ipynb, hawaii.sqlite  
- Software: Python 3.7, VS Studio Code 1.62.3, Jupyter 6.3.0, Pandas 1.2.4, SQLite, SQLAlchemy, Flask 

## Results


### Precipitaton
After importing dependancies, I set up SQLAlchemy and developed code to look at 12 previous months of precipation. 

![image](https://user-images.githubusercontent.com/90162669/142765423-4a12e47d-b2b9-425e-a835-8ee019ea8708.png)

![image](https://user-images.githubusercontent.com/90162669/142765463-5dabc870-6e91-4e57-bf93-125af1914e47.png)



### Temperatures

I next looked at temperatures for the previous year and mapped those results.  

![image](https://user-images.githubusercontent.com/90162669/142772466-afd41f84-7816-43f5-b0e0-36926d7d2b32.png)


![image](https://user-images.githubusercontent.com/90162669/142765904-9effb192-9400-40d2-801b-ecf59d7f2367.png)

### Weather by Season

Since the overall year round data looked so promising, I next looked for results for the months of June and December. 

![jun_dec_temp_chart](https://user-images.githubusercontent.com/90162669/142744770-5d942b94-2660-4bd5-8682-2f21e9c91bf4.png)


There is a bulleted list that addresses the three key differences in weather between June and December. (6 pt)

### Flask

The final step in this process was to use Flask to upload the results to the web for others to view. 


As examples, the print screen below show:
- 
- The weather staions available for which to choose temperature data
- The low, average, and high temperatures for the month of June 2017. 

![flask_temps](https://user-images.githubusercontent.com/90162669/142773528-1bbdc1f6-b5d1-487b-bd57-5399caabdf6d.png)

![flask_stations](https://user-images.githubusercontent.com/90162669/142773536-8d6a88cc-0939-44b3-97f4-f018717bb408.png)

![Flask_temps_spec_dates](https://user-images.githubusercontent.com/90162669/142772057-69f35819-d461-4298-a50e-abaf66224ab3.png)

## Summary

Instructions:  Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

Levels of precipation and temperatures on the Hawiian island of XXX are ideal for a Surf n' Shake Shop. 


All information is available for review on Git Hub.
