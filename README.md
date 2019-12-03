# TimetableExcelParser

## Description

Parses timetable of classes(input excel file) in a json file:  
````javascript
{
    "date"(str): {
        "1": [
            [<prepod_name>(str), \[\<groups>\](list of str), \<classroom>(str), <is_computer_class>(bool)],
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
- ````./builder```` - create venv and install requirements
- ````source ./venv/bin/activate````
- ````python timetable2json.py -i <input_excel> -o <output_json> [-ea]````

## Tests

Coming soon