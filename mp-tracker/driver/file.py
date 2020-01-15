import os
import json
import logging
from os import path
from driver import Driver
from time import gmtime, strftime


class File(Driver):
    """
    File output drievr pushes data to json files
    stored in directories like following:
      {location}/{server}/{username}/profile_{timestamp}.json

    `argv : Namespace`
    Parsed programm arguments namespace.
    """

    _loc = None
    _indent = False

    def __init__(self, argv):
        self._loc = argv.output
        self._indent = argv.indent
        if not path.isdir(self._loc):
            os.makedirs(self._loc)
            logging.info('OUTPUT : FILE : making dirs {}'.format(self._loc))

    def push_data_set(self, data, **kwargs):
        username = data.get('summoner_info').get('name')
        server = data.get('summoner_info').get('server')
        loc = '{}/{}/{}'.format(self._loc, server, username)
        if not path.isdir(loc):
            os.makedirs(loc)
        timestamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
        filename = '{}/profile_{}.json'.format(loc, timestamp)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=('  ' if self._indent else None))
        logging.info('OUTPUT : FILE : pushed data to {}'.format(filename))

    def get_data_set(self, usernames, server, champions):
        raise Exception('get_data_set is not implemented')

    @staticmethod
    def register_args(parser):
        g = parser.add_argument_group('File Output')
        g.add_argument(
            '--output', '-o', default='output', type=str,
            help='Output files location')
        g.add_argument(
            '--indent', default=False, action='store_true',
            help='If set, output files are saved with indentations')
