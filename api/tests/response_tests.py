import api.modules.response as response
import api.config as config
"""
The following are test cases for the Response class. 
Testing the response object built by the class
"""
#dates will be taken from the the API parameters in production

#correct date format
datefrom1 = '2021-10-01'
dateto1 = '2021-10-08'
#test result is correct

#date from after dateto
datefrom2 = '2021-10-12'
dateto2 = '2021-10-10'
#test result is an empty list response

#incomplete date formatting
datefrom3 = '2021-10'
dateto3 = '2021-10'
#test result is an empty response

#passing the same date for both values
datefrom4 = '2021-10-03'
dateto4 = '2021-10-03'
#test result is correct and returns response for the day passed to both

#empty date params
datefrom5 = ''
dateto5 = ''
#test result is a traceback error

check_response_1 = response.Response.build_response(response.Response(config.rankings_api_key,config.scoreboard_api_key,datefrom1,dateto1))
print('test1 = ')
print(check_response_1)
print(' ')
check_response_2 = response.Response.build_response(response.Response(config.rankings_api_key,config.scoreboard_api_key,datefrom2,dateto2))
print('test2 = ')
print(check_response_2)
print(' ')
check_response_3 = response.Response.build_response(response.Response(config.rankings_api_key,config.scoreboard_api_key,datefrom3,dateto3))
print('test3 = ')
print(check_response_3)
print(' ')
check_response_4 = response.Response.build_response(response.Response(config.rankings_api_key,config.scoreboard_api_key,datefrom4,dateto4))
print('test4 = ')
print(check_response_4)
print(' ')
check_response_5 = response.Response.build_response(response.Response(config.rankings_api_key,config.scoreboard_api_key,datefrom5,dateto5))
print('test5 = ')
print(check_response_5)