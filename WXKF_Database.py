# =================================================================================================================================================================================
# DEPENDENCIES

import sys # to close on command
from datetime import date # to get current day
import random # to generate random user IDs
import pandas as pd # to export
import os

# =================================================================================================================================================================================

# =================================================================================================================================================================================
# CLASSES

class Student: # holds student information
    def __init__(self, content, new=False):
        c = content.split()
        self.name = c[0]
        self.age = c[1]
        self.rank = c[2]
        self.nexttest = c[3]
        if new:
            self.alias = self.name
            self.id = f"{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}"
            while self.id in ids or len(str(self.id)) != 4:
                self.id = f"{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}"
            ids.append(self.id)
        else:
            self.alias = c[4]; self.id = c[5]

    def __repr__(self):
        return f"{self.name} | age : {self.age} | rank : {self.rank} | next test : {self.nexttest} | alias : {self.alias}"

class Command: # a struct that refers to a function, its name for the end user, and number of expected arguments
    def __init__(self, func, args : int, name):
        self.name = name
        self.xargs = args
        self.func = func

# =================================================================================================================================================================================

# =================================================================================================================================================================================
# INIT

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# read list of Student objects from students.txt
S = []
with open(os.path.join(__location__,'students.txt'),'r') as f:
    students = f.readlines()
f.close()
for s in students:
    S.append(Student(s.lower()))

today = date.today().strftime("%m/%d/%y") # get current day
print(today)

with open(os.path.join(__location__,'ids.txt'),'r') as f:
    ids = f.readlines()
f.close()


# read attendance list
with open(os.path.join(__location__,'./attendance.txt'),'r') as f:
    days = f.readlines()
f.close()
while '\n' in days:
    days.remove('\n')

D = [d[:8] for d in days]

# hard coded the months because I'm not bothering with doing it procedurally anymore
sm = ['01/22','02/22','03/22','04/22','05/22','06/22','07/22','08/22','09/22','10/22','11/22','12/22','01/23','02/23','03/23','04/23','05/23','06/23','07/23','08/23','09/23','10/23','11/23','12/23',
'01/24','02/24','03/24','04/24','05/24','06/24','07/24','08/24','09/24','10/24','11/24','12/24','01/25','02/25','03/25','04/25','05/25','06/25','07/25','08/25','09/25','10/25','11/25','12/25','01/26',
'02/26','03/26','04/26','05/26','06/26','07/26','08/26','09/26','10/26','11/26','12/26']

csm = sm[:]

months = [] # list of months
while len(sm) > 0:
    months.append([])
    for day in days:
        if f"{day[:2]}/{day[6:8]}" == sm[0]:
            months[-1].append(day.replace('\n',''))
    sm.pop(0)

def md(d):
    # monthI is the index of the current month in months
    # todayI is the index of the current day in months[monthI]
    mI = -1
    t = 0
    for i,day in enumerate(days):
        t += 1
        if day[3:5] == '01':
            mI += 1
            t = 0
        if day[:8] == today:
            tI = t
            return mI, tI
            break

monthI, todayI = md(today)

# =================================================================================================================================================================================

# =================================================================================================================================================================================
# FUNCTIONS AND COMMANDS

def validStudent(student,talk=True): # used to check if a requested student exists, used by multiple commands and is not its own command
    stu = 0
    for i,x in enumerate(S): # check if the student exists
        if student in [x.name,x.alias]:
            stu = x
            break
    if stu == 0:
        print(f"ERROR: '{student}' is not a student.")
        return 0
    return i,stu

def attend(student):
    ''' > Add a student to the attendance list for today.'''
    pass

def exit():
    ''' > Save changes and close the program.'''
    with open(os.path.join(__location__,'students.txt'),'w') as f:
        for s in S:
            f.write(f"{s.name} {s.age} {s.rank} {s.nexttest} {s.alias} {s.id}\n")
    f.close()
    with open(os.path.join(__location__,'attendance.txt'),'w') as f:
        for day in days:
            if day[:8] == months[monthI][todayI][:8]:
                day = months[monthI][todayI] + '\n'
            f.write(day)
    f.close()
    with open(os.path.join(__location__,'ids.txt'),'w') as f:
        for i in ids:
            f.write(str(i)+'\n')
    f.close()
    sys.exit("Exited.")

def alias(student, alias):
    ''' > Give aliases to students so you can refer to them faster.\n > Args: <student> <alias> where <student> is the full name of the student and <alias> is the new alias.'''
    for x in S:
        if alias == x.alias:
            print(f"ERROR: The alias '{alias}' is already used for {x.name}.")
            return 0
    for x in S:
        if x.name == student.lower():
            s = x
            s.alias = alias
            print(f"{s.name} was given the alias '{alias}'")
            return 0
    print(f"ERROR: {student} is not a student. You have to use a student's real name for this command.")

def students(L=S):
    ''' > Show a list of all the students.'''
    for s in S: print(s)

def modstudent(student, mode, content):
    ''' > Change a student's information.\n > Args: <student> <mode> <content> where <mode> is the attribute [name,age,rank,nexttest] and <content> is the new value to assign.\n > It is recommended that the name be a student's full name, ie peter-parker. The nexttest attribute can be a date, ie 03/15.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]

    if mode not in ['name','age','rank','nexttest']:
        print(f"ERROR: '{mode}' is not a valid attribute.")
        if mode == 'alias': print("You can change a student's alias with the 'alias' command.")
        return 0

    if mode == 'name':
        print(f"{S[i].name} (name): {S[i].name} -> ",end='')
        S[i].name = content
        print(f"{S[i].name}")
    elif mode == 'age':
        print(f"{S[i].name} (age): {S[i].age} -> ",end='')
        S[i].age = content
        print(f"{S[i].age}")
    elif mode == 'rank':
        print(f"{S[i].name} (rank): {S[i].rank} -> ",end='')
        S[i].rank = content
        print(f"{S[i].rank}")
    elif mode == 'nexttest':
        print(f"{S[i].name} (nexttest): {S[i].nexttest} -> ",end='')
        S[i].nexttest = content
        print(f"{S[i].nexttest}")

def addstudent(student, age, rank):
    ''' > Add a student to the database.\n > Args: <name> <age> <rank>. nexttest defaults to 'TBD' and the alias defaults to the given name.'''
    for i,x in enumerate(S): # check if the student exists
        if student in [x.name,x.alias]:
            print(f"ERROR: '{student}' already exists. There cannot be duplicate names.")
            return 0
    S.append(Student(f"{student} {age} {rank} TBD",True))
    print(f"{S[-1]} was added to the database.")

def removestudent(student):
    ''' > Permanently remove a student from the database.\n > Args: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]
    if len(S) == 1:
        print("ERROR: At least one student must exist at all times."); return 0
    confirm = str(input(f"Do you want to PERMANENTLY REMOVE:\n{S[i]}\nType 'yes' to confirm. > "))
    if confirm == 'yes':
        print(f"{S[i].name} was removed from the database.")
        S.pop(i)

def info(student):
    ''' > Get the information of a specific student.\n > Args: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    print(validStudent(student)[1])

def man():
    ''' > Bring up this man page.'''
    for c in C:
        print(f"{c.name}\n{c.func.__doc__}\n")

def attendance(timeframe):
    ''' > Show the attendance list.\n > Args: <timeframe> where timeframe is 'today' or 'month'.'''
    if timeframe not in ['today','month']:
        print(f"ERROR: '{timeframe}' is not a valid timeframe. Valid timeframes are 'today' and 'month'.")
        return 0
    elif timeframe == 'today':
        t = months[monthI][todayI]
        print(today)
        t = t.split()
        t.pop(0)
        appearances = {} # {name: num of appearances}
        for s in t:
            for p in S:
                if p.id == s:
                    if p.name not in appearances:
                        appearances[p.name] = t.count(p.id)
        for student in appearances:
            print(f" > {student} x{appearances[student]}")

    elif timeframe == 'month':
        month = months[monthI]
        for i in range(len(month)):
            t = months[monthI][i]
            print(t[:8])
            t = t.split()
            t.pop(0)
            appearances = {} # {name: num of appearances}
            for s in t:
                for p in S:
                    if p.id == s:
                        if p.name not in appearances: appearances[p.name] = t.count(p.id)
            for student in appearances:
                print(f" > {student} x{appearances[student]}")

def attend(student):
    ''' > Attend a student once for today. Count multiple appearances by running this command multiple times.\n > Args: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]
    months[monthI][todayI] += ' ' + S[i].id
    print(f"{S[i].name} was attended for today.")

def unattend(student):
    ''' > Remove a student appearance from attendance.\n > Args: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]
    months[monthI][todayI] = months[monthI][todayI].split()
    if S[i].id in months[monthI][todayI]:
        months[monthI][todayI].remove(S[i].id)
    months[monthI][todayI] = ' '.join(months[monthI][todayI])
    print(f"{S[i].name} has one apearance removed from attendance.")

def export(month):
    ''' > Export attendance data to an xlsx file.\n > Args: <month> which is a month of recorded attendance given in mm/yy form.'''
    if month not in csm:
        print(f"ERROR: '{month}' is not a valid month. Exampled of valid months are 10/21 or 05/22."); return 0
    for m in months:
        if f"{m[0][:2]}/{m[0][6:8]}" == month:
            data = m; break

    raw = ' '.join(data).split()
    raw = [i for i in raw if len(i) == 4]
    rows = [] # list of students who showed up at all this month
    for s in raw:
        for p in S:
            if p.id == s:
                if p.name not in rows: rows.append(p.name)

    d = [] # list of dicts, one dict per day, each dict is {name: num of appearances that day}
    for t in data:
        t = t.split()
        t.pop(0)
        appearances = {}
        for s in t:
            for p in S: appearances[p.name] = t.count(p.id)
        d.append(appearances)

    frame = [] # a 2d array of appearances of students
    for student in rows:
        frame.append([])
        for i in range(len(m)):
            try: frame[-1].append(d[i][student])
            except KeyError: frame[-1].append(0)

    F = pd.DataFrame(frame,index=rows,columns=[d[:8] for d in data])
    F.to_excel(os.path.join(__location__,'attendance.xlsx'))
    print(f"Attendance for the month of {month} was exported to attendance.xlsx.")

# list of recognized commands
C = [Command(man,0,'man'), Command(exit,0,'exit'), Command(students,0,'students'), Command(info,1,'info'),
    Command(modstudent,3,'modstudent'), Command(alias,2,'alias'), Command(addstudent,3,'addstudent'), Command(removestudent,1,'rmstudent'),
    Command(attend,1,'attend'), Command(unattend,1,'unattend'), Command(attendance,1,'attendance'), Command(export,1,'export')]
cmds = [c.name for c in C]

# =================================================================================================================================================================================

# =================================================================================================================================================================================
# EVENT LOOP

print("Welcome to the WXKF Database™. See the manual by typing 'man'. Use 'attendance <'today' or 'month'>' to see the attendance. Use 'export <month>' to export the attendance. Leave using 'exit', changes will not be saved if you force quit this program.")

while True: # main event loop
    raw = str(input("> "))
    if raw != '': # if enter was hit, just give the prompt again
        st = raw.split() # split input into words
        cm = st[0] # command name
        c = 0 # commmand to be used, starts as 0
        for cmd in C: # find the command
            if cm == cmd.name:
                c = cmd
        if c == 0: # if it wasn't found, give error
            print(f"ERROR: '{cm}' is not a command.")
        else: # if the command was valid
            st.pop(0) # remove command from words, st is now a list of arguments
            # check for the right number of arguments
            if len(st) < c.xargs:
                print("ERROR: Too few arguments.")
            elif len(st) > c.xargs:
                print("ERROR: Too many arguments.")
            else: # if there was a correct number of arguments, invoke the command
                if c.xargs == 0:
                    c.func()
                elif c.xargs == 1:
                    c.func(st[0])
                elif c.xargs == 2:
                    c.func(st[0],st[1])
                elif c.xargs == 3:
                    c.func(st[0],st[1],st[2])
                elif c.xargs == 4:
                    c.func(st[0],st[1],st[2],st[3])
    print()

# =================================================================================================================================================================================
