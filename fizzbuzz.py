
number = 0
print" "
print "Counter to chosen number!"

while True:
    try:
        print" "
        number = int(raw_input("Choose integer number between 1 and 100: "))

        if (number < 1 or number > 100):
            print " "
            print "You did not choose a number between 1 and 100. Please choose again!"
            print " "
        else:
            print "You chose: " + str(number)
            print "Other numbers are: (Can be divided by 3 (fizz), 5 (buzz) or 3 AND 5 (fizzbuzz)!):"
            for number in range (1, 100):
                if (number % 3 == 0 and number % 5 == 0):
                    print "fizzbuzz"
                elif (number % 5 == 0):
                    print "buzz"
                elif (number % 3 == 0):
                    print "fizz"
                else:
                    print number
    except ValueError:
        print " "
        print "You did not choose a number OR chosen number is not an integer. Please choose again!"
        print " "