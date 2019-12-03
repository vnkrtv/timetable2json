  # TimetableExcelParser

## Description

```csv
понедельник;09 сентября;16 сентября
	 09:00 - 10:35;Упр. инф. безоп.: лаб.раб-1 ауд. 20_УНЦ гр. 7353	Техн.принятия решений:  ПЗ-1 ауд. 209 гр. 7353
	 10:50 - 12:25;Упр. инф. безоп.: ПЗ-1 ауд. 20_УНЦ гр. 7353	Упр. инф. безоп.: ПЗ-2 ауд. 20_УНЦ гр. 7353
	 12:40 - 14:15		
	 15:15 - 16:50	Безопасность ОС: ПЗ-15 ауд. 122 гр. 7333	Безопасность ОС: ПЗ-16 ауд. 122 гр. 7333
вторник		10 сентября	17 сентября
	 09:00 - 10:35		
	 10:50 - 12:25		
	 12:40 - 14:15		
	 15:15 - 16:50		

```

Parses timetable of classes(input excel file) in a json file:  
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
  ````-o OUTPUT, --output OUTPUT```` - output json file  
  ````-ea, --ensure-ascii```` - ensure ascii code instead unicode ("09 января" instead "09 \u044f\u043d\u0432\u0430\u0440\u044f")  
    

## Usage

- ````git clone https://github.com/LeadNess/TimetableExcelParser.git````
- ````cd TimetableExcelParser````
- ```python3 setup.py install```
- ````timetable2json -i <input_excel> -o <output_json> [-ea]````

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