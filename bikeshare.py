import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ['january', 'february', 'march', 'april', 'may', 'june','all']
Cities=['chicago','new york','washington']
Days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
def get_filters():
   # pd.show_versions(as_json=False)
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city=input("Would you like to see data for Chicago, New York, or Washington?  ").lower()           
        if city in Cities:            
            print("let's dig in {} city".format(city))
            break
        else:
            print("you can only choose one of those cities (chicago, new york, washington)")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Would you like to filter the data by month,if yes enter the month name if no please enter all? : ").lower()           
        if month in Months:            
            break
        else:
            print("you can choose from (all,january, february, march, april, may, june)")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input(" would you like to filter data by day ? if Yes choose a day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? if No enter all : ").lower()           
        if day in Days:            
            break
        else:
            print("you can choose from (all,Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday")


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
    df=pd.read_csv(CITY_DATA[city])        
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    #if you have pandas version >=0.22  you will have  an error as datetime properties have no object called weekday_name
       #to solve it replace with day_name() instead of weekday_name 
    df['day of week']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    #filtering data by month
    if month!='all': 
        month=Months.index(month)+1
        df=df[df['month']==month]
    #filtering data by day
    if day!='all':
        df=df[df['day of week']==day.title()]
    
    return df
#loading data 
def display_raw_data(df):
    #load data from data frame for the first five rows
    choose=['yes','no']
    i=0
    s=0 #start of range value
    e=5 #end of range value
    while True:
        choice=input(" would you like to see 5 rows of the data (yes/no)").lower()           
        if choice in choose:
            if choice=='no':
                break
            elif choice=='yes':
                for i in range(s,e):
                    print(df.iloc[i,:])
                    print("\n")
                    s=s+5
                    e=e+5
        else:
            print("only enter yes / no")
    
#NEED TO CHECK FOR APPLYING THE ORIGINAL DATA FRAME 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
   # months = ['january', 'february', 'march', 'april', 'may', 'june',all]
    common_month=df['month'].mode().values
    common_month=Months[int(common_month)-1]
    print('the most common month is {}'.format(common_month))
    # TO DO: display the most common day of week
    common_day=df['day of week'].mode().values
    print('the most common day of week is {}'.format(common_day))
    # TO DO: display the most common start hour
    common_hour=df['hour'].mode().values
   # print(common_hour)
    #returning hour in am/pm form
    if common_hour==0:
        common_hour=12
        print('the most common start hour is {} am'.format(int(common_hour)))
    elif common_hour==12:
        common_hour=12
        print('the most common start hour is {} pm'.format(int(common_hour)))
    elif common_hour>12:
        common_hour=common_hour-12
        print('the most common start hour is {} pm'.format(int(common_hour)))
    else:
        print('the most common start hour is {} am'.format(int(common_hour)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Mo`st Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_s=df['Start Station'].mode().values
    print('the most common start station is \n{}'.format(common_start_s))
    # TO DO: display most commonly used end station
    common_end_s=df['End Station'].mode().values
    print('the most common end station is \n{}'.format(common_end_s))

    # TO DO: display most frequent combination of start station and end station trip
    df['merge']='From  '+df['Start Station']+'  To  '+df['End Station']
    common_start_end=df['merge'].mode().values
    print('the most common start_end station is \n{}'.format(common_start_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum().round()
    print("total travel time = {} Sec".format(total_time))


    # TO DO: display mean travel time
    avg_time=df['Trip Duration'].mean().round()
    print("average travel time = {} Sec".format(avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user types are\n{}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Genders are\n{}'.format(gender))
    else:
        print('Gender and Birth year data are not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        print('earliest year is {}'.format(earliest_year))
        recent_year = int(df['Birth Year'].max())
        print('most recent year is {}'.format(recent_year))
        common_year = int(df['Birth Year'].mode())
        print('most common year is {}'.format(common_year))
    else:
        print('Gender and Birth year data are not available for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)     
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()