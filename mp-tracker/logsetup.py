import logging


def setup_logging(loglevel, silent):
    """
    Sets up the global python logger with the
    passed log level. If silent is passed,
    logging will be supressed.

    `loglevel : number`
    Log level of the global logger.
    https://docs.python.org/3/library/logging.html#levels

    `silent : bool`
    If True, log output will be supressed.
    """
    logging.basicConfig(
        level=(50 if silent else loglevel),
        format='%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
