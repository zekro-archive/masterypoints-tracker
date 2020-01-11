import logging


class Tracker:
    """
    Tracker provides general functions to access and
    analyze the requested data.

    `masterypoints : MasteryPoints`
    MasteryPoints wrapper instance.

    `ddragon : DDragon`
    DDragon wrapper instance.
    """

    _mp = None
    _dr = None

    def __init__(self, masterypoints, ddragon):
        self._mp = masterypoints
        self._dr = ddragon

    def get_data(self, username, server, champ_names):
        """
        Returns parsed MasteryPoints API profile data
        of the summoner passed. If a list of champion
        names is provided, the mastery point entries will
        be filtered by them.

        `username : str`
        Summoner name of the target player.

        `server : str`
        Server identifier where the target
        player is registered on.

        `champ_names : str[]`
        A list of champion names to filter the result.
        If this is an empty list, no filter will be
        applied.
        """
        champ_ids = []
        if champ_names and len(champ_names) > 0:
            champ_ids = self._dr.get_champs_by_name(champ_names)
            logging.info('TRACKER : fetched champion ids: {}'.format(champ_ids))
        else:
            logging.info('TRACKER : fetch all champions')

        data = self._mp.get_profile(username, server)
        mastery_data = data.get('summoner_mastery').get('mastery_data')

        if len(champ_ids) > 0:
            mastery_data = [m for m in mastery_data if m.get('champion') in champ_ids]
            data['summoner_mastery']['mastery_data'] = mastery_data

        return data
