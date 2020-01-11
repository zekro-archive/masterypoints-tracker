import argparse


DEFAULT_MP_VERSION = 'v1.1'


def get_args():
    """
    Parses command line arguments and returns a Namespace
    containing the keys and values of the parsed arguments.
    """
    parser = argparse.ArgumentParser('masterypoint tracker')

    # Masterypoints
    mp_args = parser.add_argument_group('Masterypoints API options')
    mp_args.add_argument(
        '--username', '-u', required=True, type=str,
        help='Summoner name of the target player')
    mp_args.add_argument(
        '--server', '-s', required=True, type=str,
        help='Server where to locate the target player')
    mp_args.add_argument(
        '--mpversion', type=str, default=DEFAULT_MP_VERSION,
        help='Masterypoints API version to be used')

    # DDragon
    dr_args = parser.add_argument_group('League of Legends API options')
    dr_args.add_argument(
        '--patch', type=str,
        help='Patch version of League of Legends data')
    dr_args.add_argument(
        '--champions', '-c', type=str, default='all',
        help='Comma seperated array of champions to be fetched - not set means all')

    # Logging
    lg_args = parser.add_argument_group('Logging and output options')
    lg_args.add_argument(
        '--loglevel', '-l', default=30, type=int,
        choices=[0, 10, 20, 30, 40, 50],
        help='Log level of the global logger')
    lg_args.add_argument(
        '--silent', default=False, action='store_true',
        help='Supress console output')

    return parser.parse_args()
