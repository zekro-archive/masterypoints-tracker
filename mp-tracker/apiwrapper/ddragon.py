import requests
import logging


API_ROOT = 'http://ddragon.leagueoflegends.com/api'
CDN_ROOT = 'http://ddragon.leagueoflegends.com/cdn'


class DDragon:
    """
    DDragon provides data from the League of Legends data
    dragon API.

    `version : str`
    Data Dragon API patch version. When not provided,
    the most recent patch version will be fetched from
    the datadragon API.
    """

    _version = None

    def __init__(self, version=None):
        available_versions = self.get_versions()
        if not version:
            self._version = available_versions[0]
        else:
            if version not in available_versions:
                raise Exception('invalid cdn version')
            self._version = version
        logging.info('DDRAGON : using api version {}'.format(self._version))

    def get_versions(self):
        """
        Returns a list of available versions from the API.
        """
        return self._get_api('versions.json')

    def get_champs_by_name(self, champ_names=[]):
        """
        Returns a list of champion IDs related to the
        list of champion names. The names of the champions
        will be normalized, so spaces, quote characters (`'`),
        dots (`.`) and ampersand (`&`) will be replaced.

        `champ_names : str[]`
        List of champion names.
        """
        res = self._get_cdn('data/en_US/champion.json')
        ids = {}
        champs_map = res.get('data')
        if not champs_map:
            raise Exception('champs result was Null')
        champ_names = [DDragon._reduce_champ_name(n).lower() for n in champ_names]
        for k, v in champs_map.items():
            cname = DDragon._reduce_champ_name(k)
            if len(champ_names) <= 0 or cname in champ_names:
                cid = int(v.get('key'))
                ids[cid] = cname
        if len(ids) < len(champ_names):
            logging.warn('DDRAGON : some champion names could not be found')
        return ids

    # --------------------------------------------------------------------

    def _get(self, url, params=None):
        """
        Returns the result of a GET reqeust to a given
        URL using the given parameters.
        If the response code is an error 4xx code, an
        exception will bhe risen.

        `url : str`
        The URL to be requested.

        `[params : map]`
        Optional request parameters passed as URL queries.
        """
        res = requests.get(
            url=url,
            params=params)
        if res.status_code >= 400:
            raise Exception('Request failed: {}\n{}'.format(res.status_code, res.json()))
        return res

    def _get_api(self, path, params=None):
        """
        Returns the parsed JSON object result of
        a GET request performed on the DDragon API
        root.

        `path : str`
        The path of the request resource.

        `[params : map]`
        Optional request parameters passed as URL queries.
        """
        res = self._get(
            url='{}/{}'.format(API_ROOT, path),
            params=params)
        return res.json()

    def _get_cdn(self, path, params=None):
        """
        Returns the parsed JSON object result of
        a GET request performed on the DDragon CDN
        root using the fetched or given patch version.

        `path : str`
        The path of the request resource.

        `[params : map]`
        Optional request parameters passed as URL queries.
        """
        res = self._get(
            url='{}/{}/{}'.format(CDN_ROOT, self._version, path),
            params=params)
        return res.json()

    @staticmethod
    def _reduce_champ_name(n):
        """
        Returns a champion name lowercased and with space,
        quote, dot and ampersand characters replaced.
        """
        return n.lower().replace(' ', '').replace('\'', '').replace('.', '').replace('&', '')
