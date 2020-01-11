import logging

import mod
import apiwrapper
import util


def main():
    argv = util.get_args()
    util.setup_logging(argv.loglevel, argv.silent)
    logging.debug('MAIN : passed args: {}'.format(argv))

    mp = apiwrapper.MasteryPoints(argv.mpversion)
    dr = apiwrapper.DDragon(argv.patch)
    tr = mod.Tracker(mp, dr)

    champion_names = []
    if argv.champions and argv.champions != 'all':
        champion_names = argv.champions.split(',')

    data = tr.get_data(argv.username, argv.server, champion_names)
    with open('output.json', 'w', encoding='utf-8') as f:
        import json
        json.dump(data, f)


if __name__ == '__main__':
    main()
