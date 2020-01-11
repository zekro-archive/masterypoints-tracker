import masterypoints
import ddragon
import args
import logsetup
import tracker
import logging


def main():
    argv = args.get_args()
    logsetup.setup_logging(argv.loglevel, argv.silent)
    logging.debug('MAIN : passed args: {}'.format(argv))

    mp = masterypoints.MasteryPoints(argv.mpversion)
    dr = ddragon.DDragon(argv.patch)
    tr = tracker.Tracker(mp, dr)

    champion_names = []
    if argv.champions and argv.champions != 'all':
        champion_names = argv.champions.split(',')
    
    data = tr.get_data(argv.username, argv.server, champion_names)
    with open('output.json', 'w', encoding='utf-8') as f:
        import json
        json.dump(data, f)


if __name__ == '__main__':
    main()
