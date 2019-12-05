  # TimetableExcelParser

## Description

Parses timetable of classes(input excel file) to json file:
````javascript
{
    "date"(str): {
        "1": [
            [<prepod_name>(str), [<groups>](list of str), <classroom>(str), <is_computer_class>(bool)],
            ...
            ]  
        "2": [ ... ],  
        "3": [ ... ],  
        "4": [ ... ]  
    },  
    "another date": { ... },  
    ...  
}
````
    
Optional arguments:  
    
  ````-i INPUT, --input INPUT```` - input excel file  
  ````-o OUTPUT, --output OUTPUT```` - output json file (default - stdout)  
  ````-l, --logs```` - logfile (default - stdout)  
  ````-e, --ensure-ascii```` - ensure ascii code instead unicode ("09 января" instead "09 \u044f\u043d\u0432\u0430\u0440\u044f")  

## Example

We have an excel table timetable.xlsx with a schedule of pairs of the format below:

| понедельник |              | date_1                                                                                  |
|-------------|--------------|----------------------------------------------------------------------------------------------|
|             | 09:00 -10:35 | < pair_name >: < pair_type_1 >-< pair_number ><br>ауд. < classroom_1 ><br>гр. < groups_1 >   |                                      |
|             | 10:50 -12:25 | < pair_name >: < pair_type >-< pair_number ><br>ауд. < classroom_2 ><br>гр. < groups_2 >     |                                           |
|             | 12:40 -14:15 |                                                                                              |
|             | 15:15 -16:50 | < pair_name >: < pair_type >-< pair_number ><br>ауд. < classroom_1 ><br>гр. < groups_3 >     |                                                       |
| вторник     |              | date_2                                                                                       |
|             | 09:00 -10:35 |                                                                                              |
|             | 10:50 -12:25 |                                                                                              |
|             | 12:40 -14:15 |                                                                                              |
|             | 15:15 -16:50 |                                                                                              |
| среда       |              | date_3                                                                                       |
|             | 09:00 -10:35 |                                                                                              |
|             | 10:50 -12:25 | < pair_name >: < pair_type >-< pair_number ><br>ауд. < classroom_2 ><br>гр. < groups_4 >     |
|             | 12:40 -14:15 |                                                                                              |
|             | 15:15 -16:50 |                                                                                              |
| четверг     |              | date_4                                                                                       |
|             | 09:00 -10:35 |                                                                                              |
|             | 10:50 -12:25 |                                                                                              |
|             | 12:40 -14:15 |                                                                                              |
|             | 15:15 -16:50 |                                                                                              |
| пятница     |              | date_5                                                                                       |
|             | 09:00 -10:35 |                                                                                              |
|             | 10:50 -12:25 |                                                                                              |
|             | 12:40 -14:15 |                                                                                              |
|             | 15:15 -16:50 |                                                                                              |
| суббота     |              | date_6                                                                                       |
|             | 09:00 -10:35 |                                                                                              |
|             | 10:50 -12:25 | < pair_name >: < pair_type >-< pair_number ><br>ауд. < classroom_1 ><br>гр. < groups_5 >     |                                                                            |
|             | 12:40 -14:15 |                                                                                              |
|             | 15:15 -16:50 |                                                                                              |   

To convert this fragment to json format, you need to run 1 command:
```
timetable2json -i timetable.xlsx -o timetable.json
```
After executing the command, you will get a file of the format described in the description:
````javascript
{
    "date_1": {
        "1": [ [<prepod_name>, [<groups_1>], <classroom_1>, <is_computer_class>] ],  
        "2": [ [<prepod_name>, [<groups_2>], <classroom_2>, <is_computer_class>] ],  
        "3": [],  
        "4": [ [<prepod_name>, [<groups_3>], <classroom_1>, <is_computer_class>] ],   
    },  
    "date_2": { "1": [], "2": [], "3": [], "4": [] },
    "date_3": {
        "1": [],  
        "2": [ [<prepod_name>, [<groups_4>], <classroom_2>, <is_computer_class>] ],  
        "3": [],  
        "4": [],   
    }  
    "date_4": { "1": [], "2": [], "3": [], "4": [] },  
    "date_5": { "1": [], "2": [], "3": [], "4": [] },   
    "date_6": {
        "1": [],  
        "2": [ [<prepod_name>, [<groups_5>], <classroom_1>, <is_computer_class>] ],  
        "3": [],  
        "4": [],   
    }   
}
````
If there are several sheets in the file, the program will take data from all of them.  
Information about skipped cells will be displayed in the stdout. You can specify logging file by setting the -l flag:
```
timetable2json -i timetable.xlsx -o timetable.json -l logs.txt
```

## Usage

- ````git clone https://github.com/LeadNess/TimetableExcelParser.git````
- ```pip3 install TimetableExcelParser```
- ````timetable2json -i <input_excel> [-o <output_json>] [-l <log_file>] [-e]````

## Tests
- **pylint**
```sh
 Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
- **nosetests**
```sh
Name                               Stmts   Miss  Cover
------------------------------------------------------
tests/test_lesson.py                  43      0   100%
tests/test_prepod.py                  16      0   100%
timetable2json/ExcelParser.py         11     11     0%
timetable2json/JSONSerializer.py      31     31     0%
timetable2json/Lesson.py              43      0   100%
timetable2json/Prepod.py              46      4    91%
timetable2json/__init__.py             1      0   100%
timetable2json/timetable2json.py      15     15     0%
------------------------------------------------------
TOTAL                                206     61    70%
----------------------------------------------------------------------
Ran 10 tests in 0.664s

OK
```
