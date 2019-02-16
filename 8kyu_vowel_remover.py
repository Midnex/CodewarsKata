#! python3

# https://www.codewars.com/kata/5547929140907378f9000039/solutions/python
# Test.assert_equals(shortcut('hello'),'hll')

import re
def shortcut(message):
    # messageReg = re.compile(r'[aeiouAEIOU]')
    # return messageReg.sub('', message)

    print(re.sub('[aeiou]',"", message)) # nice way of doing it, much shorter.
    return re.sub('[aeiou]',"", message)

shortcut("This website is for losers LOL!")
shortcut('hello')
