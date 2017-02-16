from merch import Merch

def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show list of all Merch items
        2. Add new Merch Item
        3. Add new event/show
        4. Record new sale
        5. Sales Records of Merch items
        6. Sales Records of Events
        q. Quit
    ''' )

    choice = input('Enter your selection: ')

    return choice

def show_list(merchItems):
    '''Format and display a list of merch objects'''

    if len(merchItems) == 0:
        print ('* No Items in DB *')
        return

    merchItems.sort(key = lambda merch: merch.description) #this sorts the merch items by description(type)

    for merch in merchItems:
        print(merch)

    print('* {} merch item(s) *'.format(len(merchItems))

def show_event_list(eventList):
    '''Format and display list of Events'''

    if len(eventList) == 0:
        print('* No Events in DB *')
        return

    for event in eventList:
        print(event)

    print('* {} event(s) *').format(len(eventList))

def get_new_merch_info():
    '''Get Description and Price of Merch Item from user'''

    description = input('Enter Item Description: ')
    price = input('Enter Item Price: ')

    return Merch(description,price)

def get_new_event_info():
    '''Get Venue, Day, Month & Year of New Event from user'''

    venue = input('Enter name of venue: ')
    month = input('Enter month (MM): ')
    day = input('Enter day (DD): ')
    year = input('Enter year (YYYY): ')

    return Event(venue,month,day,year)

def get_new_sale_info():

    merchID = input('Enter MerchID of item sold: ')
    numSold = input('Enter number of items sold: ')
    eventID = input('Enter EventID where item was sold: ')

    return Sale(numSold,merchID,eventID)

def get_id():

    id = input('Enter ID to Search Records: ')

    return id


def message(msg):
    '''Display a message to the user'''
    print(msg)
