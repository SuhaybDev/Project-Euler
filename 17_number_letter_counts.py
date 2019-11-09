'''
 Program to find how many letters would be used if all the numbers from 1 to 1000 (one thousand) 
 inclusive were written out in words. Spaces and hyphens are not counted.
'''


# The getSum() function iterates through all the numbers from 1 to 1000 and using the converter() function converts the integers into words
def getSum():

# Creating dictionaries with the key being the digit and the value being the digit in words
# There are dictionaries for units place digits, tens place digits and teens place digits
    units = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    tens = {0:'', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    teens = {0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}


    numbers_in_words = []
    numbers = []
    # Iterating through all the numbers from 1 to 1000 and adding them to the numbers list
    for i in range(1,1001):
        numbers.append(i)
    # Converting all the numbers to words using the converter()
    for i in numbers:
        numbers_in_words.append(converter(i, units, tens, teens))
    letter_sum = 0
    # Finding the total number of letters in the numbers_in_words list
    for i in numbers_in_words:
        letter_sum += len(str(i))

    # Printing the sum found
    print(letter_sum)


# The converter(number, units, tens, teens) function converts a given number from its integer form to words
def converter(number, units, tens, teens):
    num_in_word = ''
    str_num = str(number)
    while len(str_num) < 4:
        str_num = '0' + str_num
    # Converting the digits in the thousands place to its word form using the units dictionary and adding them to the num_in_word list
    if int(str_num[0]) != 0:
        num_in_word += units.get(int(str_num[0]))
        num_in_word += 'thousand' 

    # Converting the digits in the hundreds place to its word form using the units dictionary and adding them to the num_in_word list
    if int(str_num[1]) != 0:
        num_in_word += units.get(int(str_num[1]))
        num_in_word += 'hundred'

    # Converting the digits in the tens and units place to its word form using all the dictionaries and adding them to the num_in_word list
    if int(str_num[2]) != 0:
        if int(str_num[0]) != 0 or int(str_num[1]) != 0:
            num_in_word += 'and'
        # The below loop converts the digits in tens and units place and adds them to the num_in_word list provided the digit in tens place is not 1 and the digit in units place is not 0
        if int(str_num[2]) != 1:
            num_in_word += tens.get(int(str_num[2]))
            if int(str_num[3]) != 0:
                num_in_word += units.get(int(str_num[3]))
        # Converting the digits in tens and units place with the tens place having a 1 and adding them to the num_in_word list
        else:
            num_in_word += teens.get(int(str_num[3]))
    # Converting the digit in the units place provided it isn't 0 and thousands place or hundreds place isn't 0 and adding it to the num_in_word list
    elif int(str_num[3]) != 0:
        if int(str_num[0]) != 0 or int(str_num[1]) != 0:
            num_in_word += 'and'
        num_in_word += units.get(int(str_num[3]))

    return num_in_word

# Calling the getSum() function to print the total number of letters used
getSum()