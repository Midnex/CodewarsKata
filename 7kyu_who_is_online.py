#! python
# who is online

# https://www.codewars.com/kata/whos-online/train/python

# friends = [{"username": "David", "status": "online", "last_activity": 10},
#            {"username": "Lucy", "status": "offline", "last_activity": 22},
#            {"username": "Bob", "status": "online", "last_activity": 104}]
# Test.assert_equals(who_is_online(friends), {"online": ["David"], "offline": ["Lucy"], "away": ["Bob"]})
#
#
friends = [{"username": "Lucy", "status": "offline", "last_activity": 22},
           {"username": "Bob", "status": "online", "last_activity": 104}]
# Test.assert_equals(who_is_online(friends), {"offline": ["Lucy"], "away": ["Bob"]})


def who_is_online(friends):
    for i in friends:
        if i['status'] == 'offline':
            print('Offline: ' + i['username'])
        elif i['status'] == 'online':
            print('Online: ' + i['username'])
        elif i['status'] == 'away':
            print('Away: ' + i['username'])

who_is_online(friends), {"online": ["David"], "offline": ["Lucy"], "away": ["Bob"]}
who_is_online(friends), {"offline": ["Lucy"], "away": ["Bob"]}
