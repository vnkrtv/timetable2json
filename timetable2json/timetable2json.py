# pylint: disable=missing-docstring, line-too-long, logging-not-lazy
import sys
import argparse
import logging
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
    )
    parser.add_argument(
        '-l', '--logs',
        help='logfile',
    )
    parser.add_argument(
        '-e', '--ensure-ascii',
        help=r'ensure ascii code instead unicode ("09 января" instead "09 \u044f\u043d\u0432\u0430\u0440\u044f")',
        action='store_const',
        const=True
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    output = open(args.output, 'w') if args.output else sys.stdout
    log_file = open(args.logs, 'w') if args.logs else sys.stdout

    logger = logging.getLogger("timetable2json")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logging.info("Start parsing %s " % args.input.name)
    JSONSerializer.serialize(excel_file=args.input.name).dump(
        file=output,
        ensure_ascii=not args.ensure_ascii
    )
    logging.info("Complete parsing %s into %s" % (args.input.name, output.name))


if __name__ == '__main__':
    main()
