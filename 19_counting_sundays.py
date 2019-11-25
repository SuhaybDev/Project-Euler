'''
Program to find how many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)
'''


# Function getSundays() iterates through all the days between 1901 to 2000 to find which days satisfy the condition
def getSundays():

    # Creating lists for days of the week, months of an year and years from 1901 to 2000
    days = ['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    years = []

    for i in range(1901, 2001):
        years.append(i)

    # List daysPassed cotains all the days of the week from 1901 to 2000 in order
    daysPassed = []
    # List firstOfMonth contains all the days of the week that fell on the first of a month from 1901 to 2000
    firstOfMonth = []
    # isfirstOfMonth is set to a boolean value True so we can use it in a loop to add all the days falling on 
    # the first of all months from 1901 to 2000 to the firstOfMonth list and later change it to false.
    isfirstOfMonth = True

    # Looping through all the months of all years in the twentieth century
    for year in years:
        for month in months:
            isfirstOfMonth = True
            # Looping through each day of all the months in the twentieth century
            for day in range(monthDays(month, year)):
                if isfirstOfMonth:
                    # Getting the first day of the week of all months and adding it to the firstOfMonth list 
                    firstOfMonth.append(days[0])
                    isfirstOfMonth = False
                # Adding all the days the program has looped through to the daysPassed list
                daysPassed.append(days[0])
                days.append(days.pop(0))

    # Finding the total number of Sundays in the firstOfMonth list
    count = 0
    for i in firstOfMonth:
        if i == 'Sun':
            count += 1
    # Printing the number of sundays that fell on the first of the month during the twentieth century
    print(count)


# Function monthDays(month, year) finds the number of days in the inputted month of the inputted year
def monthDays(month, year):

    # Creating lists with months containing 30, 31 and 28 days. Instances where Feb contains 29 days are dealt with separately
    days30 = ['Sep', 'Apr', 'Jun', 'Nov']
    days31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
    days28 = ['Feb']

    # Returning 30 if the inputted month is in the days30 list
    if month in days30:
        return 30
    # Returning 31 if the inputted month is in the days31 list
    elif month in days31:
        return 31
    # Checking whether the year is a leap year and returning the value based on the result for the inputted month Feb
    elif month in days28:
        if year % 400 == 0:
            return 29
        elif year % 4 == 0:
            return 29
        else:
            return 28


# Calling the getSundays() function to get the answer
getSundays()