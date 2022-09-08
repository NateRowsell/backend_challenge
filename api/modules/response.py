import json
import requests
import re

class Response:
    """
    variables:  rankings_api_key:str
                scoreboard_api_key:str
                datefrom:str
                dateto:str
                
    formatting: date variables YYYY-MM-DD
    
    rtype: Dict
    
    This class is used to create dict type responses containg NFL game data.
    It uses a scorebaord API for all games and a rankings API for all rankings.
    The new response is a combination of both sets of data.
    """
    
    def __init__(self,rankings_api_key,scoreboard_api_key,datefrom,dateto):
        self.rankings_api_key = rankings_api_key
        self.scoreboard_api_key = scoreboard_api_key
        self.datefrom = datefrom
        self.dateto = dateto
        self.team_rankings = None
        
    # rankings functions
    def get_all_rankings(self):
        """
        variables: api_key: str
        
        This function makes a call to an NFL rankings API and returns
        json of all teams current ranking
        
        rtype: dict
        """
        
        url = 'https://delivery.chalk247.com/team_rankings/NFL.json'
        payload = {'api_key':self.rankings_api_key}
        request = requests.get(url,params=payload)
        r = request.text
        json_data = json.loads(r)
        teams = json_data['results']['data']
        return teams
    

    def get_team_ranking(self,team_id:str,team_rankings:dict):
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
    
    #scoreboard functions
    
    def get_scoreboard(self):
        """
        variables:  api_key: str
                    date_from: str 
                    date_to: str
        formatting: dates should be in the following
                    format - YYYY-MM-DD
        
        This functions makes a call to an NFL scoreboard API and returns
        a dict of all games played during the given date range
        
        rtype: dict
        """
        url = ('https://delivery.chalk247.com/scoreboard/NFL/'+
               self.datefrom+
               '/'+
               self.dateto+
               '.json')
        payload = {'api_key':self.scoreboard_api_key}
        request = requests.get(url,params=payload)
        r = request.text
        json_data = json.loads(r)
        return json_data['results']
    
    def round_string(self,arg1:str):
        """
        variables: arg1:str
        
        This function intakes a float in string form and rounds the value 
        to 2 decimal places. It returns the rounded float as a string.
        
        rtype: str
        """
        
        rounded = round(float(arg1),2)
        return str(rounded)

    def change_date_format(self,dt:str):
        """
        variables: dt:str

        Intakes a date string in format YYYY-MM-DD and returns it 
        in the format DD-MM-YYYY

        rtype: str
        """
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
    
    async def build_response(self):
        """
        Parses and combines both sets of JSON data required to form
        the dict object to return
        """
        
        response = []
        all_rankings = self.get_all_rankings()
        
        days = self.get_scoreboard()
        
        for day in days:
            
            
            # the api will return empty lists on days with no events
            # to avoid key errors we skip anything that is list type
            if isinstance(days[day],list):
                continue
            else:
                daily_data = days[day]
            
            
            for data in daily_data:
                #daily data contains columns and data keys, we only require the data value
                if data != 'data':
                    continue
                
                event_data = daily_data[data]
                
                for event in event_data:
                    #set all required variables for response object
                    
                    #EVENT DATA
                    event_id = event_data[event]['event_id']
                    #strip the date time into YYYY-MM-DD and HH:MM
                    event_date_original = event_data[event]['event_date'].split(' ')[0]
                    #reverse the string for new format YYYY-MM-DD --> DD-MM-YYYY 
                    event_date = self.change_date_format(event_date_original)
                    event_time = event_data[event]['event_date'].split(' ')[1]
                    
                    #AWAY TEAM DATA
                    away_team_id = event_data[event]['away_team_id']
                    away_nick_name = event_data[event]['away_nick_name']
                    away_city = event_data[event]['away_city']
                    #retrieve away teams rank data
                    away_team_rank_data = self.get_team_ranking(team_id=away_team_id, team_rankings=all_rankings)
                    away_rank = away_team_rank_data['rank']
                    away_rank_points = self.round_string(away_team_rank_data['adjusted_points'])
                    
                    #HOME TEAM DATA
                    home_team_id = event_data[event]['home_team_id']
                    home_nick_name = event_data[event]['home_nick_name']
                    home_city = event_data[event]['home_city']
                    #retrieve home teams rank data
                    home_team_rank_data = self.get_team_ranking(team_id=home_team_id, team_rankings=all_rankings)
                    home_rank = home_team_rank_data['rank']
                    home_rank_points = self.round_string(home_team_rank_data['adjusted_points'])
                    
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

        
