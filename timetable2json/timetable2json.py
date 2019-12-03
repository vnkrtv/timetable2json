# pylint: disable=missing-docstring, line-too-long
import sys
import argparse
from timetable2json.JSONSerializer import JSONSerializer


def create_parser():
    parser = argparse.ArgumentParser(
        prog='timetable2json',
        description='''Parses timetable of classes (input excel file) in a json file:
    {
        'date'(str): {
            1: [ 
                [<prepod_name>(str), [<groups>](list of str), <classroom>(str), <is_computer_class>(bool)],
                ...
                ]
            2: [ ... ],
            3: [ ... ],
            4: [ ... ]
        },
        'another date': { ... },
        ...
    }''',
        epilog='(c) LeadNess 2019',
    )
    parser.add_argument(
        '-i', '--input',
        help='input excel file',
        type=argparse.FileType(),
        required=True
    )
    parser.add_argument(
        '-o', '--output',
        help='output json file',
        default=sys.stdout
    )
    parser.add_argument(
        '-v', '--ensure-ascii',
        help=r'ensure ascii code instead unicode ("09 января" instead "09 \u044f\u043d\u0432\u0430\u0440\u044f")',
        action='store_const',
        const=True
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    JSONSerializer.serialize(excel_file=args.input.name).dump(
        file=args.output,
        ensure_ascii=not args.ensure_ascii
    )


if __name__ == '__main__':
    main()
