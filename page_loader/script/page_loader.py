#!/usr/bin/env python3
import argparse
import os
import sys

import requests

from page_loader.engine import loader
from page_loader.logger import logger


def main():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', help='set path for output', type=str,
                        default=os.path.join(os.getcwd(), ''))
    parser.add_argument('-l', '--logging_level', help='set logging verbosity', type=str,
                        choices=['debug', 'info', 'warning', 'error', 'critical'],
                        default='warning')
    args = parser.parse_args()
    try:
        logger.setLevel(args.logging_level.upper())
        loader(args.url, args.output)
    except requests.exceptions.RequestException as error:
        sys.exit(error.args[0])
    except OSError as error:
        sys.exit(error.args[0])
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
