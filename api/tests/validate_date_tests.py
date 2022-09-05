from api.modules import validate_date as vd

"""
The following a test cases regarding functions inside validate_date.py
"""

#TEST validate()
#correct and should return true
testdate1 = '2020-10-20'
#empty should return false
testdate2 = ''
#backwards should return false
testdate3 = '20-10-2020'

print('True ',vd.validate(testdate1))
print('False ',vd.validate(testdate2))
print('False ',vd.validate(testdate3))

#TEST difference

#should return 10 
date1 = '2021-10-20'
date2 = '2021-10-30'
#should return 5
date3 = '2020-11-1'
date4 = '2020-11-6'
#should return 7
date5 = '2019-12-20'
date6 = '2019-12-27'
#will it return a negative interger = Yes
#we have covered this by checking if dateto < datefrom before running vd.difference()
date7 = '2019-12-27'
date8 = '2019-12-20'


print('10 ',vd.difference(datefrom=date1,dateto=date2))
print('5 ',vd.difference(datefrom=date3,dateto=date4))
print('7 ',vd.difference(datefrom=date5,dateto=date6))
print('-7 ',vd.difference(datefrom=date7,dateto=date8))