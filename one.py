class One:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def __repr__(self):
        return ""+self.name+" "+str(self.age)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_years(self, years):
        if not type(years) is int:
            raise ValueError("years must be of type int")
        return self.age+years


i = One("Pendo",10)
#print (i.get_name())
#print (str(i))
#print (i.get_age())
#print (One("Dave", 34).get_name())