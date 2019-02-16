#! python3

# Test.describe("Basic tests")
# Test.assert_equals(shorten_to_date("Monday February 2, 8pm"), "Monday February 2")
# Test.assert_equals(shorten_to_date("Tuesday May 29, 8pm"), "Tuesday May 29")
# Test.assert_equals(shorten_to_date("Wed September 1, 3am"), "Wed September 1")
# Test.assert_equals(shorten_to_date("Friday May 2, 9am"), "Friday May 2")
# Test.assert_equals(shorten_to_date("Tuesday January 29, 10pm"), "Tuesday January 29")

def shorten_to_date(long_date):
    print(long_date[:long_date.find(',')])
    return long_date[:long_date.find(',')]

# return long_date.split(',')[0] splitting it into ('Friday May 2', '9am') nifty

shorten_to_date("Monday February 2, 8pm"), "Monday February 2"
shorten_to_date("Tuesday May 29, 8pm"), "Tuesday May 29"
shorten_to_date("Wed September 1, 3am"), "Wed September 1"
shorten_to_date("Friday May 2, 9am"), "Friday May 2"
shorten_to_date("Tuesday January 29, 10pm"), "Tuesday January 29"
