from classes import *

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
    print(f"ERROR: {student} is not a student.")

def students(L=S):
    '''Show a list of all the students.'''
    for s in S: print(s)

def modstudent(student, mode, content):
    '''Change a student's information.'''
    stu = 0
    for x in S: # check if the student exists
        if student in [x.name,x.alias]:
            stu = x
    if stu == 0:
        print(f"ERROR: '{student}' is not a student.")
        return 0

    mod = 0 # check if the mode is valid
    if mode in ['fistname','lastname','age','rank','nexttest']:
        mod = 1
    if mod == 0:
        print(f"ERROR: '{mode}' is not a valid attribute.")
        if mode == 'alias': print("You can change a student's alias with the 'alias' command.")
        return 0

    if mode == 'firstname':
        stu.fname = content
        print("")


C = [Command(exit,0,'exit'), Command(students,0,'students'),
    Command(attend,1,'attend'),
    Command(alias,2,'alias')


    ]

def man():
    '''Bring up this man page.'''
    for c in C:
        print(f"> {c.name}\n{c.func.__doc__}\n")

C.insert(0,Command(man,0,'man'))

cmds = [c.name for c in C]
