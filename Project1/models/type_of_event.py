

class TypeOfEvent:

    def __init__(self, event_type=""):
        self.event_type = event_type

    def json(self):
        return {
            "eventType": self.event_type
        }

    @staticmethod
    def json_parse(json):
        event = TypeOfEvent()
        event.event_type = json["eventType"]
        return event

    def __repr__(self):
        return str(self.json())

