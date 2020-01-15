import argparse


DEFAULT_MP_VERSION = 'v1.1'


def get_args(*additional_registers):
    """
    Parses command line arguments and returns a Namespace
    containing the keys and values of the parsed arguments.
    """
    parser = argparse.ArgumentParser('masterypoint tracker')

    # Masterypoints
    mp_args = parser.add_argument_group('Masterypoints API options')
    mp_args.add_argument(
        '--username', '-u', required=True, type=str, nargs='+',
        help='Summoner name(s) of the target player')
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
        '--champions', '-c', type=str, default=[], nargs='+',
        help='Champions to be fetched - not set means all')

    # Scheduler
    sd_args = parser.add_argument_group('Scheduler')
    sd_args.add_argument(
        '--schedule', default=False, action='store_true',
        help='Use scheduler instead of running once')
    sd_args.add_argument(
        '--every', type=int,
        help='Execute scheduler job every x minutes')
    sd_args.add_argument(
        '--daily', type=str,
        help='Run scheduler job daily at specified time')

    # CSV
    csv_args = parser.add_argument_group('CSV Output')
    csv_args.add_argument(
        '--csv', '-csv', type=str,
        help='Output data as CSV file with specified location')

    # Logging
    lg_args = parser.add_argument_group('Logging and output options')
    lg_args.add_argument(
        '--loglevel', '-l', default=30, type=int,
        choices=[0, 10, 20, 30, 40, 50],
        help='Log level of the global logger')
    lg_args.add_argument(
        '--silent', default=False, action='store_true',
        help='Supress console output')

    for r in additional_registers:
        r.register_args(parser)

    return parser.parse_args()
