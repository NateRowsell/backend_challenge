from fastapi import FastAPI
from modules import validate_date as vd
from modules import response
import config as cfg

app = FastAPI()

#root was used for testing purposes 
@app.get('/')
def read_root():
    return {"testing":"test"}

#results will return a list of events with relevant information regarding event(game),teams and rankings
@app.get('/results')
async def read_results(datefrom: str,dateto:str,apikey:str):
    
    
    if apikey != 'resulta':
        return {"error": "incorrect api key"}

    #proper date formatting YYYY-MM-DD
    #handle the incorrect date formatting
    if vd.validate(datefrom) == False or vd.validate(dateto) == False:

        return {"error":"Formatting error with datefrom or dateto parameters",
                "date_format":"YYYY-MM-DD"}
    
    #handle datefrom being after dateto
    if dateto < datefrom:

        return {"error":"The datefrom parameter passed is a date occuring before dateto"}
    
    #handle date range being greater than 7 days, this is a limitation of scoreboard API
    if vd.difference(datefrom=datefrom,dateto=dateto) > 7:

        return {"error":"The date range entered exceeded the allowed maximum of 7 days"}

    
    #initialize class to build response object
    init_obj = response.Response(cfg.rankings_api_key,cfg.scoreboard_api_key,datefrom,dateto)
  
    return_obj = await response.Response.build_response(init_obj)

    return {"results":return_obj}
