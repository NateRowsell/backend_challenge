import json
import requests
import api.config as config


#import rankings_api_key from config
api_key=config.rankings_api_key

"""
The following functions are used in the Response class in response.py
They are duplicated here for testing purposes
"""



def get_all_rankings(api_key:str):
    """
    variables: api_key: str
    
    This function makes a call to an NFL rankings API and returns
    json of all teams current ranking
    
    rtype: dict
    """
    
    url = 'https://delivery.chalk247.com/team_rankings/NFL.json'
    payload = {'api_key':api_key}
    #makes api GET request
    request = requests.get(url,params=payload)
    #turns request json data into json string
    r = request.text
    #load json text string data
    json_data = json.loads(r)
    teams = json_data['results']['data']
    return teams
    

def get_team_ranking(team_id:str,team_rankings:dict):
    """
    variables:  team_id:str
                team_rankings: dict
    This function intakes a team id and returns that teams
    ranking statistics in json
    
    rtype:dict
    """
    
    for team in team_rankings:
        if team['team_id'] == team_id:
            return team

team_rankings = get_all_rankings(api_key=api_key)

#TEST CASES
LA_Rams = get_team_ranking(team_id='64', team_rankings=team_rankings)
print('LA_Rams = '+LA_Rams['team'])
New_England = get_team_ranking(team_id='44', team_rankings=team_rankings)
print('New_England = '+New_England['team'])
Buffalo = get_team_ranking(team_id='53', team_rankings=team_rankings)
print('Buffalo = '+Buffalo['team'])
Dallas = get_team_ranking(team_id='56', team_rankings=team_rankings)
print('Dallas = '+Dallas['team'])
Miami = get_team_ranking(team_id='65', team_rankings=team_rankings)
print('Miami = '+Miami['team'])
Cincinnati = get_team_ranking(team_id='41', team_rankings=team_rankings)
print('Cincinnati = '+Cincinnati['team'])
Detroit = get_team_ranking(team_id='50', team_rankings=team_rankings)
print('Detroit = '+Detroit['team'])
Incorrect = get_team_ranking(team_id='2', team_rankings=team_rankings)
print(Incorrect)
EmptyString = get_team_ranking(team_id='', team_rankings=team_rankings)
print(EmptyString)

#All tests with correct team ids are correct
#Incorrect and EmptyString return None