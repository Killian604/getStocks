"""
Use the stonks module to do things
"""

import argparse
import sys

import stonks

map_command_to_func = {
    'dash_app': stonks.apps.dash_app.run_dash.serve_dash,
    'createsqlite': stonks.apps.instantiate_sqlite3_database
}


def parse_args():
    # TODO: actually parse args
    if len(sys.argv) == 2:
        cmd = sys.argv[1]
    else:
        raise NotImplementedError('Command not implemented')
    args = {
        'main_command': cmd,
    }
    return args


def do(command):
    try:
        map_command_to_func[command]()
    except KeyError as ke:
        raise KeyError(f'Command not found: {command} // {repr(ke)}')


def main():
    x = parse_args()
    do(x['main_command'])
    pass


if __name__ == '__main__':
    main()
