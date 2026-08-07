from functools import total_ordering
@total_ordering
class Student:
    def __init__(self,name,gpa):
        self.name,self.gpa=name,gpa
    def __str__(self):
        return f"{self.name},{self.gpa}"
    def __eq__(self, other):
        return self.gpa==other.gpa
    def __lt__(self,other):
        return self.gpa<other.gpa