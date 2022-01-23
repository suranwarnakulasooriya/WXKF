import sys
from datetime import date
import json
import random
import os

class Student:
    def __init__(self, content, new=False):
        c = content.split()
        self.name = c[0]
        self.age = c[1]
        self.rank = c[2]
        self.nexttest = c[3]
        if new:
            self.alias = self.name
            self.id = f"{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}"
            ids = [x.id for x in S]
            while self.id in ids or len(str(self.id)) != 4:
                self.id = f"{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}"
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

class Attendance:
    def __init__(self, day, appearances):
        self.day = day
        self.appearances = appearances
        self.readable = []
        self.export = []
        for s in S:
            if s.id in self.appearances:
                self.readable.append(f"{s.name} : {self.appearances.count(s.id)}")
                self.export = 0

class Date:
    def __init__(self, s):
        self.month = s[:2]
        self.day = s[3:5]
        self.year = s[6:8]
        self.im = int(self.month)
        self.id = int(self.day)
        self.iy = int(self.year)
        self.long = ['01','03','05','07','08','10','12']
        self.short = ['04','06','09','11']
        self.feb = ['02']

    def __repr__(self):
        return f"{self.month}/{self.day}/{self.year}"

    def rewrite(self, month, day, year):
        self.month = month
        self.day = day
        if len(self.month) == 1:
            self.month = '0'+self.month
        if len(self.day) == 1:
            self.day = '0'+self.day
        self.year = year
        self.im = int(self.month)
        self.id = int(self.day)
        self.iy = int(self.year)

    def increment(self):
        if self.month in self.long and self.day == '31':
            if self.month == '12':
                self.rewrite('01','01',str(self.iy+1))
            else:
                self.rewrite(str(self.im+1),'01',self.year)
        elif self.month in self.short and self.day == '30':
            self.rewrite(str(self.im+1),'01',self.year)
        elif self.month == '02': # fuck you february
            if int('20'+self.year)%4 == 0 and self.day == '29':
                    self.rewrite('03','01',self.year)
            elif self.day == '28':
                    self.rewrite('03','01',self.year)
        else:
            self.rewrite(self.month,str(self.id+1),self.year)

# reat list of students from students.txt
S = []
with open('students.txt','r') as f:
    students = f.readlines()
f.close()
for s in students:
    S.append(Student(s.lower()))

today = date.today().strftime("%m/%d/%y")
print(today)

with open('attendance.txt','r') as f:
    days = f.readlines()
f.close()
while '\n' in days:
    days.remove('\n')


um = [] # list of unique months
um = [f"{d[:2]}/{d[6:8]}" for d in days if f"{d[:2]}/{d[6:8]}" not in um]
months = [] # list of months
while len(um) > 0:
    months.append([])
    for day in days:
        if f"{day[:2]}/{day[6:8]}" == um[0]:
            months[-1].append(day.replace('\n',''))
    um.pop(0)

# monthI is the index of the current month in months
# todayI is the index of the current day in months[monthI]
monthI = -1
for i,day in enumerate(days):
    if day[3:5] == '01':
        monthI += 1
    if day[:8] == today:
        todayI = i
        break
