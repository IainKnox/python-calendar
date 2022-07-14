'''
a command line calendar that allows a user
to view the calendar, add an event,
update an event or delete an event. A very
simple prototype for my P4 project.
'''
# imports to handle the pauses and datetime strings
from time import sleep, strftime

USER = 'name'
calendar = {}   # create an empty dict to hold day:event pairs


def welcome():
    '''
    function to welcomew a user, get user details and start
    the calendar.
    '''
    print(f'Welcome to the Calendar {USER}')
    print('The calendar is starting up...')
    # let the user know the app is starting
    sleep(1)
    print('Today is ' + strftime('%A %m %d %Y'))
    # print Full weekday name, Month, Day, Year
    print('The current time is: ' + strftime('%H:%M:%S'))
    # print Hour:Minutes:Seconds
    sleep(1)
    print('What would you like to do? ')


def start_calendar():
    '''
    this function holds all the calendar functionality
    to view, add, update, delete and exit the app.
    '''
    welcome()   # here I call welcome, to welcome the user.
    start = True
    # the User can decide when to exit the app, so the
    # start variable holds a boolean to test when the
    # user opts to close the app.
    while start:
        # create the functionality a user can choose from
        user_choice = input('Press A to add, \
        U to Update, \
        V to View, \
        D to Delete or \
        X to exit: ')
        user_choice = user_choice.upper()   # change to uppercase
        if user_choice == 'V':  # view calendar
            if len(calendar.keys()) < 1:
                # check if there are existing entries by checking
                # that the length of the array is greater than 1
                print('Your calendar is empty')
            else:
                print(calendar)
        elif user_choice == 'U':    # update calendar
            date = input('Which date would you like to update? ')
            update = input('Enter the update: ')
            # allow the user to enter a string as an update
            calendar[date] = update  # adds the update to the specified date
            print('Calendar updated successfully.')
            print(calendar)  # to display the update
