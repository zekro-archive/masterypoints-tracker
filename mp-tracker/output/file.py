import os
import json
import logging
from os import path
from output import Output
from time import gmtime, strftime


class File(Output):
    """
    File output drievr pushes data to json files
    stored in directories like following:
      {location}/{server}/{username}/profile_{timestamp}.json

    `argv : Namespace`
    Parsed programm arguments namespace.
    """

    _loc = None

    def __init__(self, argv):
        self._loc = argv.output
        if not path.isdir(loc):
            os.makedirs(loc)
            logging.info('OUTPUT : FILE : making dirs {}'.format(loc))

    def push_data_set(self, data, ident=False):
        username = data.get('summoner_info').get('name')
        server = data.get('summoner_info').get('server')
        loc = '{}/{}/{}'.format(self._loc, server, username)
        if not path.isdir(loc):
            os.makedirs(loc)
        timestamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
        filename = '{}/profile_{}.json'.format(loc, timestamp)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=('  ' if ident else None))
        logging.info('OUTPUT : FILE : pushed data to {}'.format(filename))

    @staticmethod
    def register_args(parser):
        g = parser.add_argument_group('File Output')
        g.add_argument(
            '--output', '-o', default='output', type=str,
            help='Output files location')
