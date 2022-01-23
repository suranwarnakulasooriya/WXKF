# WXKF Database
A (for now terminal based) program to track student attendance. Written for a private entity.

## Installation ##
First make sure [Python3+](https://www.python.org/downloads/windows/) is installed, then install the following dependencies.
```
pip install sys
pip install datetime
pip install random
pip install pandas # this should be the only dependency not automatically installed with Python
```
Then, clone this repository.
```
git clone --branch production https://github.com/suranwarnakulasooriya/WXKF
```
You can put this in the command line if you have `git` installed or you can download from this page. Make sure to download from the `production` branch. A folder named "WXKF" will be created. Navigate to that folder in the command line and run the program.
```
python3 WXKF_Databse.py
```
The program for now runs entirely in the terminal and there is no need to open any other files in the WXKF directory. The `man` command should tell you everything you need to know to use the program.

## Demo
Now here's a demo of what the WXKF Database can do.

Opening prompt:
```
$ python3 WXKF_Database.py
Welcome to the WXKF Database™. See the manual by typing 'man'. Use 'attendance <'today' or 'month'>' to see the attendance. Use 'export <month>' to export the attendance. Leave using 'exit', changes will not be saved if you force quit this program.
> 
```
The man command:
```
> man
↪ man
Bring up this man page.

↪ exit
Save changes and close the program.

↪ students
Show a list of all the students.

↪ info
Get the information of a specific student.
Args: <student> which is the name or alias of a student.

↪ modstudent
Change a student's information.
Args: <student> <mode> <content> where <mode> is the attribute [name,age,rank,nexttest] and <content> is the new value to assign.
It is recommended that the name be a student's full name, ie peter-parker. The nexttest attribute can be a date, ie 03/15.

↪ alias
Give aliases to students so you can refer to them faster.
Args: <student> <alias> where <student> is the full name of the student and <alias> is the new alias.

↪ addstudent
Add a student to the database.
Args: <name> <age> <rank>. nexttest defaults to 'TBD' and the alias defaults to the given name.

↪ rmstudent
Permanently remove a student from the database.
Args: <student> which is the name or alias of a student.

↪ attend
Attend a student once for today. Count multiple appearances by running this command multiple times.
Args: <student> which is the name or alias of a student.

↪ unattend
Remove a student appearance from attendance.
Args: <student> which is the name or alias of a student.

↪ attendance
Show the attendance list.
Args: <timeframe> where timeframe is 'today' or 'month'.

↪ export
Export attendance data to an xlsx file.
Args: <month> which is a month of recorded data.
```
Viewing student information:
```
> students
name : peter-parker | age : 18 | rank : redshirt | next test : 04/20 | alias : spiderman
name : bruce-wayne | age : 25 | rank : yellowbelt | next test : 06/09 | alias : batman
name : tony-stark | age : 48 | rank : redbelt | next test : 10/18 | alias : ironman
name : bruce-banner | age : 27 | rank : purplebelt | next test : 08/09 | alias : hulk

> info peter-parker
name : peter-parker | age : 18 | rank : redshirt | next test : 04/20 | alias : spiderman

> info batman
name : bruce-wayne | age : 25 | rank : yellowbelt | next test : 06/09 | alias : batman
```
Giving students aliases:
```
> info suran-warnakulasooriya
name : suran-warnakulasooriya | age : 15 | rank : redblack | next test : TBD | alias : suran-warnakulasooriya

> alias suran-warnakulasooriya suran16
suran-warnakulasooriya was given the alias 'suran16'

> info suran16
name : suran-warnakulasooriya | age : 15 | rank : redblack | next test : TBD | alias : suran16
```
Changing student information:
```
> info hulk
name : bruce-banner | age : 27 | rank : whitebelt | next test : 08/09 | alias : hulk

> modstudent hulk rank purplebelt
bruce-banner (rank): whitebelt -> purplebelt

> info hulk
name : bruce-banner | age : 27 | rank : purplebelt | next test : 08/09 | alias : hulk
```
Adding students (test date defaults to TBD and the alias defaults to the name):
```
> students
name : peter-parker | age : 18 | rank : redshirt | next test : 04/20 | alias : spiderman
name : bruce-wayne | age : 25 | rank : yellowbelt | next test : 06/09 | alias : batman

> addstudent suran-warnakulasooriya 15 redblack
name : suran-warnakulasooriya | age : 15 | rank : redblack | next test : TBD | alias : suran-warnakulasooriya was added to the database.

> students
name : peter-parker | age : 18 | rank : redshirt | next test : 04/20 | alias : spiderman
name : bruce-wayne | age : 25 | rank : yellowbelt | next test : 06/09 | alias : batman
name : suran-warnakulasooriya | age : 15 | rank : redblack | next test : TBD | alias : suran-warnakulasooriya
```
Removing students:
```
> students
name : peter-parker | age : 18 | rank : redshirt | next test : 04/20 | alias : spiderman
name : bruce-wayne | age : 25 | rank : yellowbelt | next test : 06/09 | alias : batman
name : suran-warnakulasooriya | age : 15 | rank : redblack | next test : TBD | alias : suran16

> rmstudent suran16
Do you want to PERMANENTLY REMOVE:
name : suran-warnakulasooriya | age : 15 | rank : redblack | next test : TBD | alias : suran16
Type 'yes' to confirm. > yes
suran-warnakulasooriya was removed from the database.

> students
name : peter-parker | age : 18 | rank : redshirt | next test : 04/20 | alias : spiderman
name : bruce-wayne | age : 25 | rank : yellowbelt | next test : 06/09 | alias : batman
```
Viewing attendance (with the 'month' option, every day of the month would be shown, not shown here for brevity):
```
> attendance month
01/20/22
  ↪ tony-stark x1
01/22/22
  ↪ peter-parker x1
  ↪ bruce-banner x1
01/23/22
  ↪ tony-stark x2
  ↪ peter-parker x3
  ↪ bruce-wayne x2

> attendance today
01/23/22
  ↪ tony-stark x2
  ↪ peter-parker x3
  ↪ bruce-wayne x2
```
Attending students:
```
> attendance today
01/23/22
  ↪ tony-stark x2
  ↪ peter-parker x3
  ↪ bruce-wayne x2

> attend hulk
bruce-banner was attended for today.

> attend tony-stark
tony-stark was attended for today.

> unattend spiderman
peter-parker has one apearance removed from attendance.

> attendance today
01/23/22
  ↪ tony-stark x3
  ↪ peter-parker x2
  ↪ bruce-wayne x2
  ↪ bruce-banner x1
```
Exporting attendance (the screenshot is taken from LibreOffice but Microsoft Excel can open xlsx files too):
```
> export 01/22
Attendance for the month of 01/22 was exported to attendance.xlsx.
```
![image](https://user-images.githubusercontent.com/68828123/150699446-21a4b1d3-de6c-4b90-911f-8543f1ca29a5.png)
