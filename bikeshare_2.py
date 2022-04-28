import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\'s explore some US bikeshare data!")
    city = ''

    while city not in CITY_DATA.keys():

        print("\nPlease choose your city of interest to analyze:")
        print("\n1. New York City 2. Washington 3. Chicago")
        print("\nPlease enter the name of the city you wish to analyze from above\n")
        
        # all inputs converted to lowercases with method below to avoid non standardization of inputs and variables
        city = input().lower()

        if city not in CITY_DATA.keys():
            
            print("\nPlease check your City input and try again (Ps. Grammatical errors)")
#print("\nRestarting...")
            time.sleep(2.0)
    print("\nYou have chosen {} as your city of interest.".format(city.title()))

    # Creating a dictionary below to store all the months including the 'all' option
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3,
                  'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter your month of interest, from January through June, to aggregate analyzed data:")
        print("NB: (If you choose to get analysis for all months, type in 'all'.)")
        # all inputs converted to lowercases with method below to avoid non standardization of inputs and variables
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. Kindly try again with accepted format(s) or check for grammatical errors.")
#print("\nRestarting...")
            time.sleep(2.0)
            
    print("\nYour selected month of interest: {}.".format(month.title()))

    # Creating a list to store all the days including the 'all' option
    DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_DATA:
        print("\nEnter a day of the week to analyze its data:")
        print("NB: (Enter 'All' to get insight for all days in a week.)")
        day = input().lower()

        if day not in DAY_DATA:
            print("\nInvalid input. Kindly try again in the accepted input format(s) or check grammatical errors.")
#print("\nRestarting...")
            time.sleep(2.0)
            
    print("\nYour selected Day of interest: {}.".format(day.title()))
    print("\nYou have requested aggregated data for city: {}, month/s: {} and day(s): {}.".format(city.upper(), month.upper(), day.upper()))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading requested data...")
    df = pd.read_csv(CITY_DATA[city])
    
    #Convert the Start Time column in data given to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month (if) applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]
    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    #Returns the selected file as a dataframe (df) with relevant columns
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Display the most common month
    #popular_month = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print(f"\nMost Common month of Travel: {popular_month}")
    
    #Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"\nMost Common Day: {popular_day}")

    #Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"\nMost Common Start Hour: {popular_hour}")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations & trip."""

    print('\nCalculating The Most Popular Stations and Travel Trip...\n')
    start_time = time.time()

    #Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")

    #Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {common_end_station}")

    #Display most frequent combination of start station & end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of start station and end station trip are from {combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total & average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display the total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)

    print(f"The total travel time is {hour} hours, {minute} minutes and {second} seconds.")

    # Display average travel time
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)

    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average travel time is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average travel time is {mins} minutes and {sec} seconds.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display the counts of user types
    user_type = df['User Type'].value_counts()
    print("Count of user types are shown below:\n{}".format(user_type))

    # Display counts of gender
    print('\n Aggregating Gender statistics....')
    try:
        gender = df['Gender'].value_counts()
        print(f"\nCount of user genders are shown below:\n{gender}")
    except:
        print("\nIn this file, there's no 'Gender' column.")

    # Display earliest, most recent & most common year of birth
    print('\n Aggregating Birth Year statistics....')
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\nThe most recent year of birth: {recent}\nThe most common year of birth: {common_year}")
    except:
        print("\nIn this file, there's no information about the year of birth of bikeshare users.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Function to display lines of data as per user request
def raw_data(df):
    
    RESPONSE_MAT = ['yes', 'no']
    view_data = ''
    
    counter = 0
    while view_data not in RESPONSE_MAT:
        print("\nDo you wish to view raw data?")
        print("\nAccepted responses:\nYes \nNo ")
        view_data = input().lower()

        #the raw data from the df is displayed if user requests for it
        if view_data == "yes":
            #head() function is used to get the first n rows. 
            #This function returns the rows for the data requested
            print(df.head())
        elif view_data not in RESPONSE_MAT:
            print("\nSomething is wrong; Please check your response and try again.")
            print("Input does not match any of the accepted responses.")
            print("\nReinitiating request...\n")

    #While loop keeps prompting user incase of more raw data requests
    while view_data == 'yes':
        print("Do you wish to view more lines of raw data?")
        counter += 5
        view_data = input().lower()
        
        #If user accepts yes it displays next 5 rows of raw data
        if view_data == "yes":
             print(df[counter:counter+5])
        elif view_data != "yes":
             break

    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

