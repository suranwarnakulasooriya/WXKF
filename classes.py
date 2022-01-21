import sys

class Student:
    def __init__(self, content):
        c = content.split()
        self.fname = c[0].lower()
        self.lname = c[1].lower()
        self.age = c[2]
        self.rank = c[3]
        self.nexttest = c[4]
        self.name = f"{self.fname}-{self.lname}"
        if len(c) == 6:
            self.alias = c[5]
        else:
            self.alias = None
    def __repr__(self):
        return f"{self.name} | age : {self.age} | rank : {self.rank} | next test : {self.nexttest} | alias : {self.alias}"

class Command:
    def __init__(self, func, args : int, name):
        self.name = name
        self.xargs = args
        self.func = func

S = []
with open('students.txt') as f:
    students = f.readlines()
    for s in students:
        S.append(Student(s.lower()))
