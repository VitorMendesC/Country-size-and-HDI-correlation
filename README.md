# Country size and HDI correlation
This is a data analysis learning project where I explore the correlation between a country's size (land only) and its human development index (HDI).

<br/><br/>

## Hypothesis:
Smaller countries would have an easier task covering their population with access to essential services like hospitals and schools but also commodities, cultural centers, and quality of life related services.
All of the above contributes to a higher HDI. So on average smaller countries may have a higher HDI.
<br/><br/>
<br/><br/>

## Methodology:
Gathered data from Wikipedia using web scraping, cleaned the data, statistically analyzed it, and plotted it.
<br/><br/>
<br/><br/>

## Results:
In total, I collected the data from 188 countries, doing a linear regression on the data and plotting it gives us the following result:

<img src="https://user-images.githubusercontent.com/105181657/167732656-2266c443-0691-409e-9de1-55401bc66d69.png" width="600">

This result contradicts the hypothesis that smaller countries would have higher HDI, which is evident by the positive slope that suggests that the bigger the land, the higher the HDI.

It's also clear that we have 6 outliers and their effects on the analysis are quite drastic, with a very low r squared (r²=0.009718).

![size_diff](https://user-images.githubusercontent.com/105181657/167732694-fc29b8ad-666d-49f6-ae48-75fc3482da05.png)

We can illustrate their effects by running a second analysis removing the outliners:
Which shows a negative slope and a better, but still low, fitting (r²=0.02088).

<img src="https://user-images.githubusercontent.com/105181657/167734086-2cab3e58-50e1-4d91-89b8-9c3be256cadd.png" width="600">

This second result is more in line with what I expected but with a coefficient of determination this low it can't be said that there is any type of association between those two variables.
<br/><br/>
<br/><br/>

## Conclusion:
Although higher population density means an easier task of covering the population with access to services, which in turn leads to a higher HDI, a small country doesn't necessarily have a dense population, and a large country doesn't necessarily have a sparse population.
On top of that HDI is a complex metric and numerous factors contribute to a country's HDI.

Based on this simple analysis it can't be argued that a country's land size has a direct influence on the country's HDI, even though it can have positive impacts on logistics.
<br/><br/>
<br/><br/>

## What have I learned:
- Web scrapping
- Data cleaning
- Statistical analysis
- Data visualization
<br/><br/>
<br/><br/>

## How to run:
You only need 'main.py', 'scraper.py', and 'requirements.txt'.

If you don't want to install all the necessary modules system-wide create a virtual environment first and run:
```
pip install -r requirements.txt
```
For the full data set analysis, on the downloaded directory, do:
```
py .\main.py
```
In the first run, or if you delete the .CSV, it will generate a .CSV with all the data that you can analyze separately if you want.

For the analysis excluding the outliners you just need to pass a 1 as an argument:
```
py .\main.py 1
```
