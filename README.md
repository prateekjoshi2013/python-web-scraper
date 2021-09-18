#Web Scraper Using Python
##Objective
The KGB has noticed a resurgence of overly excited reviews for a McKaig Chevrolet Buick, a dealership they have planted in the United States. In order to avoid attracting unwanted attention, you’ve been enlisted to scrape reviews for this dealership from DealerRater.com and uncover the top three worst offenders of these overly positive endorsements.

## Features

- Scrape HTML files with urls
- Calculation of positive sentiment in reviews
- Used textblob library for text sentiment analysis 
- Used beautiful soup library for parsing html file
- Used aiohttp library for asynchronus fetch
- Used asynchronus and multithreading constructs for efficiency
- Provided code for both sequential and parallel flow for the task to show the performance gain

##Objectives Accomplished
- Created an efficient webscraper using concurrency constructs
- Calculated of positive sentiment in reviews
- Provided code for both sequential and parallel flow for the task to show the performance gain

<p align = "center">
<img src = "https://drive.google.com/uc?export=view&id=1hXPK_WMzZiV9MS4GvOT7yEYVhRaijnAA">
</p>
<p align = "center">
PARALLEL FLOW EXECUTION RESULT - 1.02 sec
</p>

<p align = "center">
<img src = "https://drive.google.com/uc?export=view&id=1IRTqxYx3B-9zLW8FKqC70idacecH0Ihs">
</p>
<p align = "center">
SEQUENTIAL FLOW EXECUTION RESULT - 3.44 sec
</p>

## Positivity Calculation
The ranking of reviews is based on a positivity_score :

#### Star Ratings
- It is based on  star ratings provided by user on criteria like experience,customer_service,friendliness & pricing which are normalized to a value of 50 with recommendation being a yes/no rating normalized to a 0 or 50 
then these values are averaged out and then divided by 50 to
give us a rating a decimal between [0,1]

#### Polarity Value from Review Comments
- It is calculated using the
    polarity ,by using the textblob sentiment analysis library a value
    between (-1 to 1) and divide it by 2 giving us a value between
    [-0.5,0.5] and add it to the overall positivity rating






## Installation

This application requires python  v3.8.2+ to run.

Make sure you’ve got Python & pip and upgrade if needed
```sh
$ python --version
$ pip --version
```
On mac:

```sh
$ brew install pipenv
```

If you're using Debian Buster+:

```sh
$ sudo apt install pipenv
```
Or, if you're using Fedora:
```sh
$ sudo dnf install pipenv
```

Or, if you're using FreeBSD:
```sh
$ pkg install py36-pipenv
```

Or, if you're using Windows:
```sh
$ pip install --user pipenv
```

clone the repository
and go to the directory and execute to create virtual 
env and download dependencies needed 
```sh
$ pipenv install 
```

change to pipenv shell
```sh
$ pipenv shell 
```


for running tests
```sh
$ pipenv run python run_test.py
```

for running concurrent flow
```sh
$ pipenv run python driver_concurrent.py
```

for running sequential flow
```sh
$ pipenv run python driver_sequential.py
```








