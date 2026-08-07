class Person:
    def __init__(self,age):
        self._age=age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if value<0:
            print("Negative age")
        else:
            print("Positive age")
            self._age=value