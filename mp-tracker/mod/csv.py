import os
import logging
from os import path


class CSV:
    _output = None
    _champids = None

    def __init__(self, output, champids):
        self._output = output
        self._champids = champids

    def generate_champs(self, data, username, champs=[]):
        res = []
        for d in data:
            summinfo = d.get('summoner_info')
            if summinfo.get('name') != username:
                continue
            date = summinfo.get('last_info_update')
            mparr = d.get('summoner_mastery').get('mastery_data')
            mpmap = {}
            for m in mparr:
                cname = self._champids[m.get('champion')]
                mpmap[cname] = m.get('points')
            dline = []
            if champs:
                dline = [str(mpmap[n]) for n in champs]
            else:
                dline = [str(v) for v in mpmap.values()]
                champs = list(mpmap.keys())
            res.append(','.join([date] + dline))
        res.insert(0, ','.join(['date'] + champs))
        self._write_csv(res)

    def _write_csv(self, data_str_arr):
        outdir = path.dirname(self._output)
        if outdir != '' and not path.isdir(outdir):
            os.makedirs(outdir)
        with open(self._output, 'w', encoding='utf-8') as f:
            f.write('\n'.join(data_str_arr))
        logging.info('CSV : csv data output to {}'.format(self._output))
