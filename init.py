import sys
from datetime import date
import json
import random

with open('date.txt','r') as f:
    savedate = f.read()
f.close()
if date.today().strftime("%m/%d/%y") != savedate:
    savedate = date.today().strftime("%m/%d/%y")
    with open('date.txt','w') as f:
        f.write(savedate)
        f.close()

class Student:
    def __init__(self, content, new=False):
        c = content.split()
        self.name = c[0]
        self.age = c[1]
        self.rank = c[2]
        self.nexttest = c[3]
        if new:
            self.alias = self.name
            self.id = int(f"{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}")
            ids = [x.id for x in S]
            while self.id in ids or len(str(self.id)) != 4:
                self.id = int(f"{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}")
        else:
            self.alias = c[4]
            self.id = c[5]

    def __repr__(self):
        return f"name : {self.name} | age : {self.age} | rank : {self.rank} | next test : {self.nexttest} | alias : {self.alias}"

class Command:
    def __init__(self, func, args : int, name):
        self.name = name
        self.xargs = args
        self.func = func

S = []
with open('students.txt') as f:
    students = f.readlines()
f.close()
for s in students:
    S.append(Student(s.lower()))
