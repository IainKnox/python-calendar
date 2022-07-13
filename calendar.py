'''
a command line calendar that allows a user
to view the calendar, add an event,
update an event or delete an event. A very
simple prototype for my P4 project.
'''
# imports to handle the pauses and datetime strings
from time import sleep, strftime

USER = 'name'
calendar = {}


def welcome():
    '''
    function to get user details and start
    the calendar.
    '''
    print(f'Welcome to the Calendar {USER}')
    print('The calendar is starting up...')
    sleep(1)
    print('Today is ' + strftime('%A %m %d %Y'))
    print('The current time is: ' + strftime('%H:%M:%S'))
    sleep(1)
    print('What would you like to do? ')

