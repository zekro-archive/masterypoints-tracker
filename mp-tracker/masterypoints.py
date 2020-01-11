import requests
import urllib
import logging


API_ROOT = 'https://www.masterypoints.com/api'


class MasteryPoints:
    """
    Masterypoints provides information from the
    Masterypoints REST API.

    `version : str`
    Masterypoints API version.
    """

    _version = None

    def __init__(self, version):
        self._version = version
        logging.info('MASTERYPOINTS : using api version {}'.format(self._version))

    def get_profile(self, username, server):
        """
        Returns a profile object of the passed summoner
        by username and server.

        `username : str`
        Summoner name of the player.

        `server : str`
        Server short identifier of the server the
        target summoner is registered on.
        """
        username = urllib.parse.quote(username)
        return self._get('summoner/{}/{}'.format(username, server))

    # --------------------------------------------------------------------

    def _get(self, path, params=None):
        """
        Returns the response object of a GET reqeust to
        the provided path of the masterypoints API base
        depending on the defined API version.

        `path : str`
        Path to the API resource.

        `[params : map]`
        Optional request parameters passed as URL queries.
        """
        res = requests.get(
            url='{}/{}/{}'.format(API_ROOT, self._version, path),
            params=params)
        if res.status_code >= 400:
            raise Exception('Request failed: {}\n{}'.format(res.status_code, res.json()))
        return res.json()
