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

'''
# read current day from date.txt, update if outdated
with open('date.txt','r') as f:
    savedate = f.read()
f.close()
today = date.today().strftime("%m/%d/%y")
outdated = False
if today != savedate:
    savedate = today
    outdated = True
    with open('date.txt','w') as f:
        f.write(savedate)
        f.close()
'''

today = date.today().strftime("%m/%d/%y")
with open('attendance.txt','r') as f:
    days = f.readlines()
f.close()
if today != days[-1]:
    now = Date(today)
    yy = now.year
    days.extend([
    f'01/01/{yy}', f'01/02/{yy}', f'01/03/{yy}', f'01/04/{yy}', f'01/05/{yy}', f'01/06/{yy}',
    f'01/07/{yy}', f'01/08/{yy}', f'01/09/{yy}', f'01/10/{yy}', f'01/11/{yy}', f'01/12/{yy}',
    f'01/13/{yy}', f'01/14/{yy}', f'01/15/{yy}', f'01/16/{yy}', f'01/17/{yy}', f'01/18/{yy}',
    f'01/19/{yy}', f'01/20/{yy}', f'01/21/{yy}', f'01/22/{yy}', f'01/23/{yy}', f'01/24/{yy}',
    f'01/25/{yy}', f'01/26/{yy}', f'01/27/{yy}', f'01/28/{yy}', f'01/29/{yy}', f'01/30/{yy}', f'01/31/{yy}',
    f'02/01/{yy}', f'02/02/{yy}', f'02/03/{yy}', f'02/04/{yy}', f'02/05/{yy}', f'02/06/{yy}',
    f'02/07/{yy}', f'02/08/{yy}', f'02/09/{yy}', f'02/10/{yy}', f'02/11/{yy}', f'02/12/{yy}',
    f'02/13/{yy}', f'02/14/{yy}', f'02/15/{yy}', f'02/16/{yy}', f'02/17/{yy}', f'02/18/{yy}',
    f'02/19/{yy}', f'02/20/{yy}', f'02/21/{yy}', f'02/22/{yy}', f'02/23/{yy}', f'02/24/{yy}',
    f'02/25/{yy}', f'02/26/{yy}', f'02/27/{yy}', f'02/28/{yy}', f'02/29/{yy}',
    f'03/01/{yy}', f'03/02/{yy}', f'03/03/{yy}', f'03/04/{yy}', f'03/05/{yy}', f'03/06/{yy}',
    f'03/07/{yy}', f'03/08/{yy}', f'03/09/{yy}', f'03/10/{yy}', f'03/11/{yy}', f'03/12/{yy}',
    f'03/13/{yy}', f'03/14/{yy}', f'03/15/{yy}', f'03/16/{yy}', f'03/17/{yy}', f'03/18/{yy}',
    f'03/19/{yy}', f'03/20/{yy}', f'03/21/{yy}', f'03/22/{yy}', f'03/23/{yy}', f'03/24/{yy}',
    f'03/25/{yy}', f'03/26/{yy}', f'03/27/{yy}', f'03/28/{yy}', f'03/29/{yy}', f'03/30/{yy}', f'03/31/{yy}',
    f'04/01/{yy}', f'04/02/{yy}', f'04/03/{yy}', f'04/04/{yy}', f'04/05/{yy}', f'04/06/{yy}',
    f'04/07/{yy}', f'04/08/{yy}', f'04/09/{yy}', f'04/10/{yy}', f'04/11/{yy}', f'04/12/{yy}',
    f'04/13/{yy}', f'04/14/{yy}', f'04/15/{yy}', f'04/16/{yy}', f'04/17/{yy}', f'04/18/{yy}',
    f'04/19/{yy}', f'04/20/{yy}', f'04/21/{yy}', f'04/22/{yy}', f'04/23/{yy}', f'04/24/{yy}',
    f'04/25/{yy}', f'04/26/{yy}', f'04/27/{yy}', f'04/28/{yy}', f'04/29/{yy}', f'04/30/{yy}',
    f'05/01/{yy}', f'05/02/{yy}', f'05/03/{yy}', f'05/04/{yy}', f'05/05/{yy}', f'05/06/{yy}',
    f'05/07/{yy}', f'05/08/{yy}', f'05/09/{yy}', f'05/10/{yy}', f'05/11/{yy}', f'05/12/{yy}',
    f'05/13/{yy}', f'05/14/{yy}', f'05/15/{yy}', f'05/16/{yy}', f'05/17/{yy}', f'05/18/{yy}',
    f'05/19/{yy}', f'05/20/{yy}', f'05/21/{yy}', f'05/22/{yy}', f'05/23/{yy}', f'05/24/{yy}',
    f'05/25/{yy}', f'05/26/{yy}', f'05/27/{yy}', f'05/28/{yy}', f'05/29/{yy}', f'05/30/{yy}', f'05/31/{yy}',
    f'06/01/{yy}', f'06/02/{yy}', f'06/03/{yy}', f'06/04/{yy}', f'06/05/{yy}', f'06/06/{yy}',
    f'06/07/{yy}', f'06/08/{yy}', f'06/09/{yy}', f'06/10/{yy}', f'06/11/{yy}', f'06/12/{yy}',
    f'06/13/{yy}', f'06/14/{yy}', f'06/15/{yy}', f'06/16/{yy}', f'06/17/{yy}', f'06/18/{yy}',
    f'06/19/{yy}', f'06/20/{yy}', f'06/21/{yy}', f'06/22/{yy}', f'06/23/{yy}', f'06/24/{yy}',
    f'06/25/{yy}', f'06/26/{yy}', f'06/27/{yy}', f'06/28/{yy}', f'06/29/{yy}', f'06/30/{yy}',
    f'07/01/{yy}', f'07/02/{yy}', f'07/03/{yy}', f'07/04/{yy}', f'07/05/{yy}', f'07/06/{yy}',
    f'07/07/{yy}', f'07/08/{yy}', f'07/09/{yy}', f'07/10/{yy}', f'07/11/{yy}', f'07/12/{yy}',
    f'07/13/{yy}', f'07/14/{yy}', f'07/15/{yy}', f'07/16/{yy}', f'07/17/{yy}', f'07/18/{yy}',
    f'07/19/{yy}', f'07/20/{yy}', f'07/21/{yy}', f'07/22/{yy}', f'07/23/{yy}', f'07/24/{yy}',
    f'07/25/{yy}', f'07/26/{yy}', f'07/27/{yy}', f'07/28/{yy}', f'07/29/{yy}', f'07/30/{yy}', f'07/31/{yy}',
    f'08/01/{yy}', f'08/02/{yy}', f'08/03/{yy}', f'08/04/{yy}', f'08/05/{yy}', f'08/06/{yy}',
    f'08/07/{yy}', f'08/08/{yy}', f'08/09/{yy}', f'08/10/{yy}', f'08/11/{yy}', f'08/12/{yy}',
    f'08/13/{yy}', f'08/14/{yy}', f'08/15/{yy}', f'08/16/{yy}', f'08/17/{yy}', f'08/18/{yy}',
    f'08/19/{yy}', f'08/20/{yy}', f'08/21/{yy}', f'08/22/{yy}', f'08/23/{yy}', f'08/24/{yy}',
    f'08/25/{yy}', f'08/26/{yy}', f'08/27/{yy}', f'08/28/{yy}', f'08/29/{yy}', f'08/30/{yy}', f'08/31/{yy}',
    f'09/01/{yy}', f'09/02/{yy}', f'09/03/{yy}', f'09/04/{yy}', f'09/05/{yy}', f'09/06/{yy}',
    f'09/07/{yy}', f'09/08/{yy}', f'09/09/{yy}', f'09/10/{yy}', f'09/11/{yy}', f'09/12/{yy}',
    f'09/13/{yy}', f'09/14/{yy}', f'09/15/{yy}', f'09/16/{yy}', f'09/17/{yy}', f'09/18/{yy}',
    f'09/19/{yy}', f'09/20/{yy}', f'09/21/{yy}', f'09/22/{yy}', f'09/23/{yy}', f'09/24/{yy}',
    f'09/25/{yy}', f'09/26/{yy}', f'09/27/{yy}', f'09/28/{yy}', f'09/29/{yy}', f'09/30/{yy}',
    f'10/01/{yy}', f'10/02/{yy}', f'10/03/{yy}', f'10/04/{yy}', f'10/05/{yy}', f'10/06/{yy}',
    f'10/07/{yy}', f'10/08/{yy}', f'10/09/{yy}', f'10/10/{yy}', f'10/11/{yy}', f'10/12/{yy}',
    f'10/13/{yy}', f'10/14/{yy}', f'10/15/{yy}', f'10/16/{yy}', f'10/17/{yy}', f'10/18/{yy}',
    f'10/19/{yy}', f'10/20/{yy}', f'10/21/{yy}', f'10/22/{yy}', f'10/23/{yy}', f'10/24/{yy}',
    f'10/25/{yy}', f'10/26/{yy}', f'10/27/{yy}', f'10/28/{yy}', f'10/29/{yy}', f'10/30/{yy}', f'10/31/{yy}',
    f'11/01/{yy}', f'11/02/{yy}', f'11/03/{yy}', f'11/04/{yy}', f'11/05/{yy}', f'11/06/{yy}',
    f'11/07/{yy}', f'11/08/{yy}', f'11/09/{yy}', f'11/10/{yy}', f'11/11/{yy}', f'11/12/{yy}',
    f'11/13/{yy}', f'11/14/{yy}', f'11/15/{yy}', f'11/16/{yy}', f'11/17/{yy}', f'11/18/{yy}',
    f'11/19/{yy}', f'11/20/{yy}', f'11/21/{yy}', f'11/22/{yy}', f'11/23/{yy}', f'11/24/{yy}',
    f'11/25/{yy}', f'11/26/{yy}', f'11/27/{yy}', f'11/28/{yy}', f'11/29/{yy}', f'11/30/{yy}',
    f'12/01/{yy}', f'12/02/{yy}', f'12/03/{yy}', f'12/04/{yy}', f'12/05/{yy}', f'12/06/{yy}',
    f'12/07/{yy}', f'12/08/{yy}', f'12/09/{yy}', f'12/10/{yy}', f'12/11/{yy}', f'12/12/{yy}',
    f'12/13/{yy}', f'12/14/{yy}', f'12/15/{yy}', f'12/16/{yy}', f'12/17/{yy}', f'12/18/{yy}',
    f'12/19/{yy}', f'12/20/{yy}', f'12/21/{yy}', f'12/22/{yy}', f'12/23/{yy}', f'12/24/{yy}',
    f'12/25/{yy}', f'12/26/{yy}', f'12/27/{yy}', f'12/28/{yy}', f'12/29/{yy}', f'12/30/{yy}', f'12/31/{yy}',
    ])
    if int('20'+now.year)%4 != 0:
        days.remove(f'02/29/{now.year}')
