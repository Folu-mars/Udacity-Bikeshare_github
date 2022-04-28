# Project Overview: Overview
In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States - Chicago, New York, and Washington. I have written code to import the data and answer questions about it by computing descriptive statistics. I have also written a script that takes in raw input to create an interactive session for the user in the terminal.

Divvy is a bicycle sharing system in the City of Chicago and two adjacent suburbs (image: [Wikipedia](https://en.wikipedia.org/wiki/Divvy))

## What Software Do I Use?
To complete this project, i used the following softwares:
* I had Python 3, NumPy, and pandas installed using Anaconda navigation.
* A text editor,  [Atom](https://atom.io/) was used.
* A terminal application (Terminal on Mac).

# Project Details: Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I used data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover the bike share usage patterns. I compared the system usage between three cities: Chicago, New York City, and Washington DC.

## The Datasets
* Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
    * Start Time (e.g., 2017-01-01 00:07:57)
    * End Time (e.g., 2017-01-01 00:20:53)
    * Trip Duration (in seconds - e.g., 776)
    * Start Station (e.g., Broadway & Barry Ave)
    * End Station (e.g., Sedgwick St & North Ave)
    * User Type (Subscriber or Customer)
* The Chicago and New York City files also have the following two columns:
    * Gender
    * Birth Year
* The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data)). 

## Statistics Computed
I learned about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, I wrote code to provide the following information:
* Popular times of travel (i.e., occurs most often in the start time)
    * most common month
    * most common day of week
    * most common hour of day
* Popular stations and trip
    * most common start station
    * most common end station
    * most common trip from start to end (i.e., most frequent combination of start station and end station)
* Trip duration
    * total travel time
    * average travel time
* User info
    * counts of each user type
    * counts of each gender (only available for NYC and Chicago)
    * earliest, most recent, most common year of birth (only available for NYC and Chicago)

# How to run the project
* Clone the project
* Prerequisite
    * You must have installed python and libraries like numpy and pandas.
* Complete the TO-DO lists
    * Open the terminal
    * And run
    ```python bikeshare_2.py```

# Extra Links that helped me solve the project are:
* https://www.python-course.eu/python3_input.php
* https://stackoverflow.com/questions/2847386/python-string-and-integer-concatenation
* https://www.w3schools.com/python/python_datetime.asp

* This project was written by Folusho for Udacity's Programming for Data Science with Python Nanodegree.