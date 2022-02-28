class Person:
    def __init__(self, name, id, points):
        self.name = name
        self.id = id
        self.points = points

    def __repr__(self):
        return "Name"+self.name+". ID: "+self.id+". Points: "+self.points+"."