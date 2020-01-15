#!/usr/bin/python3

import logging
import schedule
import time

import mod
import apiwrapper
import util
import const


DATA_DRIVER = const.DATA_DRIVER


def main():
    argv = util.get_args(DATA_DRIVER)
    util.setup_logging(argv.loglevel, argv.silent)
    logging.debug('MAIN : passed args: {}'.format(argv))

    mp = apiwrapper.MasteryPoints(argv.mpversion)
    dr = apiwrapper.DDragon(argv.patch)
    tr = mod.Tracker(mp, dr)
    out = DATA_DRIVER(argv)

    if argv.csv is not None:
        data = out.get_data_set(argv.username, argv.server)
        csv = mod.CSV(argv.csv, dr.get_champs_by_name())
        csv.generate_champs(data, argv.username[0], argv.champions)
        return

    def job():
        for uname in argv.username:
            logging.info('MAIN : fetching data for user {} ({})'.format(uname, argv.server))
            data = tr.get_data(uname, argv.server, argv.champions)
            out.push_data_set(data)

    if not argv.schedule:
        job()
        return

    if argv.every is not None:
        schedule.every(argv.every).minutes.do(job)
        logging.info('MAIN : scheduled job every {} minutes'.format(argv.every))
    elif argv.daily is not None:
        schedule.every().day.at(argv.daily).do(job)
        logging.info('MAIN : scheduled job every day at {}'.format(argv.daily))
    else:
        logging.fatal('MAIN : schedule interval must be set')
        return

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
