# surfs_up

## Overview

Develop a plan to move to [which island?] Hawii and open a Surf n' Shake Shop that will serve surf boards and ice cream to locals and tourists. I have already developed a business plan and am now analyzing weather patterns to make sure precipitation and temperatures are ideal for this type of shop.   

In addition to using my personal savings, I will need investor backing. 

## Resources

- Data Sources:climate_analysis.ipynb, hawaii.sqlite  
- Software: Python 3.7, VS Studio Code 1.62.3, Jupyter 6.3.0, Pandas 1.2.4, SQLite, SQLAlchemy, Flask 

## Results
After importing dependancies, I set up SQLAlchemy. 

![image](https://user-images.githubusercontent.com/90162669/142765385-b9762017-bab2-4e7c-8be5-5932aa77b504.png)



### Precipitaton
I then developed code to look at 12 previous months of precipation and mapped the results. 

![image](https://user-images.githubusercontent.com/90162669/142765423-4a12e47d-b2b9-425e-a835-8ee019ea8708.png)

![image](https://user-images.githubusercontent.com/90162669/142765463-5dabc870-6e91-4e57-bf93-125af1914e47.png)



### Temperatures

I next looked at temperatures for the previous year, turned the results into a dataframe and mapped the results.  

![image](https://user-images.githubusercontent.com/90162669/142772466-afd41f84-7816-43f5-b0e0-36926d7d2b32.png)




![image](https://user-images.githubusercontent.com/90162669/142765904-9effb192-9400-40d2-801b-ecf59d7f2367.png)

Since the overall year round data looked so promising, I next looked for results for the months of June and December. 

![jun_dec_temp_chart](https://user-images.githubusercontent.com/90162669/142744770-5d942b94-2660-4bd5-8682-2f21e9c91bf4.png)


### Flask

The final step in this process was to use Flask to upload the results to te web for others to view. 


The print screen below shows the low, average, and high temperatures for the month of June 2017. 

![Flask_temps_spec_dates](https://user-images.githubusercontent.com/90162669/142772057-69f35819-d461-4298-a50e-abaf66224ab3.png)

## Summary

Instructions:  Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

Levels of precipation and temperatures on the Hawiian island of XXX are ideal for a Surf n' Shake Shop. 


All information is available for review on Git Hub.
