from sys import maxsize

class Project:
    def __init__(self, name=None, description=None, id=None):
        self.name = name
        self.description = description
        # self.status = status
        # self.viewstate = viewstate
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.name, self.description)# self.status, self.viewstate,

    def __eq__(self, other):
        return (self.name == other.name and self.description == other.description)# and self.status == other.status and self.viewstate == other.viewstate


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize