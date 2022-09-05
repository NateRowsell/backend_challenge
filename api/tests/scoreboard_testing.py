import json 
import requests
import api.config as config
"""
These functions are used in the Response class inside response.py

These tests will check the return values of the functions.

The desired goal of these tests is only to test responses from 
the scoreboard API so any rankings data will be redacted and "0000"
in its place. There are seperate tests for both APIs
"""


#import scoreboard_api_key from config
api_key = config.scoreboard_api_key


def get_scoreboard(api_key:str,date_from:str,date_to:str):
    """
    variables:  api_key: str
                date_from: str 
                date_to: str
    formatting: dates should be in the following
                format - YYYY-MM-DD
    
    This functions makes a call to an NFL scoreboard API and returns
    json of all games played during the given date range
    
    rtype: dict
    """
    url = ('https://delivery.chalk247.com/scoreboard/NFL/'+
           date_from+
           '/'+
           date_to+
           '.json')
    payload = {'api_key':api_key}
    #makes api GET request
    request = requests.get(url,params=payload)
    #turns request json data into json string
    r = request.text
    #load json text string data
    json_data = json.loads(r)
    return json_data['results']
    

def build_response(api_key:str,date_from:str,date_to:str):
    
    response = []
    days = get_scoreboard(api_key=api_key,date_from=date_from,date_to=date_to)
    
    for day in days:
        
        
        # the api will return empty lists on days with no events
        # to avoid key errors we skip anything that is list type
        if isinstance(days[day],list):
            continue
        else:
            daily_data = days[day]
        
        
        for data in daily_data:
            #daily data contains columns and data, we only require the data object
            if data != 'data':
                continue
            
            event_data = daily_data[data]
            
            for event in event_data:
                #set all required variables for response object
                
                event_id = event_data[event]['event_id']
                #strip the date time into DD-MM-YYYY and HH:MM
                event_date = event_data[event]['event_date'].split(' ')[0]
                event_time = event_data[event]['event_date'].split(' ')[1]
                away_team_id = event_data[event]['away_team_id']
                away_nick_name = event_data[event]['away_nick_name']
                away_city = event_data[event]['away_city']
                away_rank = 0000 # redacted
                away_rank_points = 0000 # redacted
                home_team_id = event_data[event]['home_team_id']
                home_nick_name = event_data[event]['home_nick_name']
                home_city = event_data[event]['home_city']
                home_rank = 0000 # redacted
                home_rank_points = 0000 # redacted
                
                #build response object
                eventDict = {
                    "event_id": event_id,
                    "event_date": event_date,
                    "event_time": event_time,
                    "away_team_id": away_team_id,
                    "away_nick_name": away_nick_name,
                    "away_city": away_city,
                    "away_rank": away_rank,
                    "away_rank_points": away_rank_points,
                    "home_team_id": home_team_id,
                    "home_nick_name": home_nick_name,
                    "home_city": home_city,
                    "home_rank": home_rank,
                    "home_rank_points": home_rank_points
                    
                    }
                
                response.append(eventDict)

    return response

#TEST 1
#correct date format
datefrom1 = '2021-10-01'
dateto1 = '2021-10-08'
#test result is correct

#TEST 2
#date from after dateto
datefrom2 = '2021-10-12'
dateto2 = '2021-10-10'
#test result is an empty list response

#TEST 3
#incomplete date formatting
datefrom3 = '2021-10'
dateto3 = '2021-10'
#test result is an empty list response

#TEST4
#empty date params
datefrom4 = ''
dateto4 = ''
#test result is a traceback error

print('function response 1')
function_response_1 = build_response(api_key=api_key,date_from=datefrom1,date_to=dateto1)
print(function_response_1)
print('/n')

print('function response 2')
function_response_2 = build_response(api_key=api_key,date_from=datefrom2,date_to=dateto2)
print(function_response_2)
print('/n')

print('function response 3')
function_response_3 = build_response(api_key=api_key,date_from=datefrom3,date_to=dateto3)
print(function_response_3)
print('/n') 

print('function response 4')
function_response_4 = build_response(api_key=api_key,date_from=datefrom4,date_to=dateto4) 
print(function_response_4)
print('/n')