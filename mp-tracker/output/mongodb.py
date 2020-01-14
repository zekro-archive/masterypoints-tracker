import pymongo
import logging
from output import Output


class MongoDB(Output):
    _con = None
    _db_name = None
    _client = None
    _db = None

    def __init__(self, argv):
        self._con = argv.connection
        self._db_name = argv.database
        self._client = pymongo.MongoClient(self._con)
        self._db = self._client[self._db_name]
        logging.info('OUTPUT : MONGO : connected to database \'{}\''.format(self._db_name))

    def push_data_set(self, data, **kwargs):
        # username = data.get('summoner_info').get('name')
        # server = data.get('summoner_info').get('server')
        colle = self._db.profiles
        colle.insert_one(data)

    @staticmethod
    def register_args(parser):
        g = parser.add_argument_group('MongoDB Connection')
        g.add_argument(
            '--connection', '-con', required=True, type=str,
            help='MongoDB connection URI string')
        g.add_argument(
            '--database', '-db', required=True, type=str,
            help='Database name')
