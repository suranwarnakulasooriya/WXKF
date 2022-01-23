from init import *

def validStudent(student): # used to check if a requested student exists, used by multiple commands and is not its own command
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
    '''Close the program.'''
    sys.exit("Exited.")

def alias(student, alias):
    '''Give aliases to students so you can refer to them faster.\nUse: <student> <alias> where <student> is the full name of the student and <alias> is the new alias.'''
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
    '''Change a student's information./nUse: <student> <mode> <content> where <mode> is the attribute [name,age,rank,nexttest] and <content> is the new value to assign.'''
    if not validStudent(student): return 0
    i = validStudent(student)[0]

    if mode not in ['name','age','rank','nexttest']:
        print(f"ERROR: '{mode}' is not a valid attribute.")
        if mode == 'alias': print("You can change a student's alias with the 'alias' command.")
        return 0

    if mode == 'name':
        print(f"{S[i].name} : {S[i].name} -> ",end='')
        S[i].name = content
        print(f"{S[i].name}")
    elif mode == 'age':
        print(f"{S[i].name} : {S[i].age} -> ",end='')
        S[i].age = content
        print(f"{S[i].age}")
    elif mode == 'rank':
        print(f"{S[i].name} : {S[i].rank} -> ",end='')
        S[i].rank = content
        print(f"{S[i].rank}")
    elif mode == 'nexttest':
        print(f"{S[i].name} : {S[i].nexttest} -> ",end='')
        S[i].nexttest = content
        print(f"{S[i].nexttest}")

def addstudent(student, age, rank, nexttest):
    '''Add a student to the database.\nUse: <name> <age> <rank> <nexttest>.'''
    if validStudent(student):
        print(f"ERROR: A student with the name {student} already exists.")
        return 0
    S.append(Student([student,age,rank,nexttest],True))


def info(student):
    '''Get the information of a specific student.\nUse: <student> which is the name or alias of a student.'''
    if not validStudent(student): return 0
    print(validStudent(student)[1])


def man():
    '''Bring up this man page.'''
    for c in C:
        print(f"↪ {c.name}\n{c.func.__doc__}\n")

def attendance():
    '''Show the attendance list for today.'''


C = [Command(man,0,'man'), Command(exit,0,'exit'), Command(students,0,'students'),
    Command(attend,1,'attend'), Command(info,1,'info'),
    Command(alias,2,'alias'),
    Command(modstudent,3,'modstudent'),
    Command(addstudent,4,'addstudent')


    ]



#C.insert(0,Command(man,0,'man'))

cmds = [c.name for c in C]
