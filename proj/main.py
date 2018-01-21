"""
Main entrypoint
"""
import logging
import argparse

from .base import Main

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
logging.basicConfig()


def get_cli_parser():
    """Create CLI parser
    """
    _parser = argparse.ArgumentParser(description='My New Project')

    _parser.add_argument('--string',
                         action='store',
                         required=True,
                         dest='a_string',
                         help='A string to use')

    _parser.add_argument('--number',
                         type=int,
                         required=False,
                         default=1,
                         action='store',
                         dest='a_number')

    _parser.add_argument('--upper',
                         action='store_true',
                         dest='to_upper',
                         default=False)

    return _parser


if __name__ == '__main__':
    parser = get_cli_parser()
    args = parser.parse_args()

    MAIN = Main(args.a_string, args.a_number)
    ret_str = MAIN.run(args.to_upper)

    LOGGER.info(ret_str)
