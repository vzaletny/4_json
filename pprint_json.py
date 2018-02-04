import argparse
import json


def get_args():
    parser = argparse.ArgumentParser(description='''Pretty print 
                                                 any raw JSON file''')
    parser.add_argument('file',
                        metavar='JSON file',
                        help='Path to incoming raw JSON file')
    args = parser.parse_args()
    return args


def load_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as open_file:
        return json.load(open_file)


def pretty_print_json(json_content):
    print(json.dumps(json_content,
                     sort_keys=True,
                     indent=4,
                     ensure_ascii=False))


def _main():
    args = get_args()
    try:
        json_content = load_file(args.file)
    except FileNotFoundError:
        print('File not found')
    except OSError as error_msg:
        print('Something went wrong')
        print(error_msg)
    else:
        pretty_print_json(json_content)


if __name__ == '__main__':
    _main()
