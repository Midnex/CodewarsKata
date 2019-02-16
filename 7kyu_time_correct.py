#! python3
# Correct time-string
# https://www.codewars.com/kata/correct-the-time-string/train/python

# Test.describe('Basic Tests')
# Test.it('None or empty')
# Test.assert_equals(time_correct(None), None)
# Test.assert_equals(time_correct(''), '')
# Test.it('Invalid Format')
# Test.assert_equals(time_correct('001122'), None)
# Test.assert_equals(time_correct('00;11;22'), None)
# Test.assert_equals(time_correct('0a:1c:22'), None)
# Test.it('Correction Tests')
# Test.assert_equals(time_correct('09:10:01'), '09:10:01')
# Test.assert_equals(time_correct('11:70:10'), '12:10:10')
# Test.assert_equals(time_correct('19:99:99'), '20:40:39')
# Test.assert_equals(time_correct('24:01:01'), '00:01:01')
# Test.assert_equals(time_correct('52:01:01'), '04:01:01')

def time_correct(t):
    if t == None:
        print(str(t) + ' is equal to None')
        return None
    elif t == '':
        print('')
        return ''
    elif len(t) != 8:
        print(str(t) + ' is equal to None')
        return None
    else:
        try:
            x = ()
            x = t.split(':')
            if x[0].isnumeric() == True:
                print(x[0] + ':' + x[1] + ':' + x[2])
                return x[0] + ':' + x[1] + ':' + x[2]
            else:
                print('None')
                return None
        except:
            print('None')
            return None



time_correct(None)
time_correct('')
time_correct('001122')
time_correct('00;11;22')
time_correct('0a:1c:22')
time_correct('09:10:01')
time_correct('11:70:10')
time_correct('19:99:99')
time_correct('24:01:01')
time_correct('52:01:01')
