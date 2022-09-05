import datetime

def validate(date:str):
    """
    variables: date:str

    Intakes a string type date and confirms the format 
    is YYYY-MM-DD. Returns True if true and False if false

    rtype: Boolean 
    """
    try:
        datetime.datetime.strptime(date,'%Y-%m-%d')
        return True
    except ValueError:
        return False

def difference(datefrom:str,dateto:str):
    """
    variables: datefrom:str
               dateto:str
    Calculates the difference in days between 2 dates in string
    form and formatted as follows: YYYY-MM-DD

    rtype: int
    """
    dt1 = datetime.datetime.strptime(datefrom,'%Y-%m-%d')
    dt2 = datetime.datetime.strptime(dateto,'%Y-%m-%d')
    return (dt2 - dt1).days

