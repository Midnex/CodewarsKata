import re
def disemvowel(message):
    messageReg = re.compile(r'[^aeiouAEIOU]')
    print(messageReg.findall(message))

disemvowel("This website is for losers LOL!")
