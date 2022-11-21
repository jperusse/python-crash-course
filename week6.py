""" Week6 exercises """
class User:
    """ User object """
    def __init__(self,username:str, userid:str):
        name = username
        login_id = userid

class Event:
    """ Event class can be login or logout """

    def __init__(self,event_date:str, event_type:str, machine:str, event_user:User):
        """ set event attributes """
        ev_date = event_date
        ev__type = event_type
        mac = machine
        user = event_user
        

def create_user_report(event_list):
    """ Create a user report from an event list """
    if len(event_list) == 0:
        return "no events found"
    next_event = event_list[0]
    report = next_event.mac
    return report