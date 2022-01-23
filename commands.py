from init import *

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
    '''Add a student to the attendance list for today.'''
    pass

def exit():
    '''Save changes and close the program.'''
    with open('students.txt','w') as f:
        for s in S:
            f.write(f"{s.name} {s.age} {s.rank} {s.nexttest} {s.alias} {s.id}\n")
    f.close()
    with open('attendance.txt','w') as f:
        for day in days:
            if day[:8] == months[monthI][todayI][:8]:
                day = months[monthI][todayI] + '\n'
                #print(months[monthI][todayI])
            f.write(day+'\n')
    f.close()
    sys.exit("Exited.")

def alias(student, alias):
    '''Give aliases to students so you can refer to them faster.\nArgs: <student> <alias> where <student> is the full name of the student and <alias> is the new alias.'''
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
    '''Show a list of all the students.'''
    for s in S: print(s)

def modstudent(student, mode, content):
    '''Change a student's information.\nArgs: <student> <mode> <content> where <mode> is the attribute [name,age,rank,nexttest] and <content> is the new value to assign.\nIt is recommended that the name be a student's full name, ie peter-parker. The nexttest attribute can be a date, ie 03/15.'''
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
    '''Add a student to the database.\nArgs: <name> <age> <rank>. nexttest defaults to 'TBD' and the alias defaults to the given name.'''
    for i,x in enumerate(S): # check if the student exists
        if student in [x.name,x.alias]:
            print(f"ERROR: '{student}' already exists. There cannot be duplicate names.")
            return 0
    S.append(Student(f"{student} {age} {rank} TBD",True))
    print(f"{S[-1]} was added to the database.")

def removestudent(student):
    '''Permanently remove a student from the database.\nArgs: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]
    confirm = str(input(f"Do you want to PERMANENTLY REMOVE:\n{S[i]}\nType 'yes' to confirm. > "))
    if confirm == 'yes':
        print(f"{S[i].name} was removed from the database.")
        S.pop(i)


def info(student):
    '''Get the information of a specific student.\nArgs: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    print(validStudent(student)[1])


def man():
    '''Bring up this man page.'''
    for c in C:
        print(f"↪ {c.name}\n{c.func.__doc__}\n")

def attendance(timeframe):
    '''Show the attendance list.\nArgs: <timeframe> where timeframe is 'today' or 'month'.'''
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
            print(f"  ↪ {student} x{appearances[student]}")

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
                print(f"  ↪ {student} x{appearances[student]}")

def attend(student):
    '''Attend a student once for today. Count multiple appearances by running this command multiple times.\nArgs: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]
    months[monthI][todayI] += ' ' + S[i].id
    print(f"{S[i].name} was attended for today.")

def unattend(student):
    '''Remove a student appearance from attendance.\nArgs: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]
    months[monthI][todayI] = months[monthI][todayI].split()
    months[monthI][todayI].remove(S[i].id)
    months[monthI][todayI] = ' '.join(months[monthI][todayI])
    print(f"{S[i].name} has one apearance removed from attendance.")


def export(month):
    '''Export attendance data to an xlsx file.\nArgs: <month> which is a month of recorded data.'''
    if month not in sm:
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

    F = pd.DataFrame(frame,index=rows,columns=data)
    F.to_excel('attendance.xlsx')
    print(f"Attendance for the month of {month} was exported to attendance.xlsx.")

# list of recognized commands
C = [Command(man,0,'man'), Command(exit,0,'exit'), Command(students,0,'students'), Command(info,1,'info'),
    Command(modstudent,3,'modstudent'), Command(alias,2,'alias'), Command(addstudent,3,'addstudent'), Command(removestudent,1,'rmstudent'),
    Command(attend,1,'attend'), Command(unattend,1,'unattend'), Command(attendance,1,'attendance'), Command(export,1,'export')]
cmds = [c.name for c in C]
