# TimetableExcelParser

## Description

Parses timetable of classes(input excel file) in a json file:  
    {  
        'date'(str): {  
            1: [   
                [<prepod_name>(str), \[\<groups>\](list of str), \<classroom>(str), <is_computer_class>(bool)],
                ...
                ]  
            2: [ ... ],  
            3: [ ... ],  
            4: [ ... ]  
        },  
        'another date': { ... },  
        ...  
    }
    
optional arguments:  
    
  -i INPUT, --input INPUT - input excel file  
  -o OUTPUT, --output OUTPUT - output json file  

(c) LeadNess 2019
    

## Usage

- ````git clone https://github.com/LeadNess/TimetableExcelParser.git````
- ````cd TimetableExcelParser````
- ````./builder```` - create venv and install requirements
- ````source ./venv/bin/activate````
- ````python timetable2json.py -i <input_excel> -o <output_json>````