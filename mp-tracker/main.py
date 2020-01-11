import logging

import mod
import apiwrapper
import util
import output


OUTPUT_DRIVER = output.File


def main():
    argv = util.get_args(OUTPUT_DRIVER)
    util.setup_logging(argv.loglevel, argv.silent)
    logging.debug('MAIN : passed args: {}'.format(argv))

    mp = apiwrapper.MasteryPoints(argv.mpversion)
    dr = apiwrapper.DDragon(argv.patch)
    tr = mod.Tracker(mp, dr)
    out = OUTPUT_DRIVER(argv)

    for uname in argv.username:
        logging.info('MAIN : fetching data for user {} ({})'.format(uname, argv.server))
        data = tr.get_data(uname, argv.server, argv.champions)
        out.push_data_set(data, ident=True)


if __name__ == '__main__':
    main()
