#!/usr/bin/env python3

import logging
import os
import textwrap
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

from flask import Flask
from flask_restplus import Api

from .email import api as email_api
from .url import api as url_api
from .domain import api as domain_api
from .ip import api as ip_api

# from .stats import api as stats_api

application = Flask(__name__)

# http://flask-restplus.readthedocs.io/en/stable/swagger.html#documenting-authorizations
api = Api(application, version='0.0.0a0', title='Predict API', description='The CSIRTG Predict REST API')

APIS = [
    email_api,
    url_api,
    domain_api,
    ip_api
]

for A in APIS:
    api.add_namespace(A)

ns = api.namespace('api', description='predict operations')

application.secret_key = os.urandom(2048)

log_level = logging.WARN

HTTP_LISTEN_PORT = os.getenv('APP_HTTP_PORT', 5000)
HTTP_LISTEN = os.getenv('APP_HTTP_LISTEN', '127.0.0.1')

console = logging.StreamHandler()
logging.getLogger('gunicorn.error').setLevel(log_level)
logging.getLogger('gunicorn.error').addHandler(console)
logger = logging.getLogger('gunicorn.error')


def main():
    p = ArgumentParser(
        description=textwrap.dedent('''\
            example usage:
                $ predictd -d
            '''),
        formatter_class=RawDescriptionHelpFormatter,
        prog='predictd-httpd'
    )

    p.add_argument('-d', '--debug', dest='debug', action="store_true")
    p.add_argument('--listen', help='specify the interface to listen on [default %(default)s]', default=HTTP_LISTEN)
    p.add_argument('--listen-port', help='specify the port to listen on [default %(default)s]',
                   default=HTTP_LISTEN_PORT)

    p.add_argument('--fdebug', action='store_true')  # flask debug on

    args = p.parse_args()
    #setup_logging(args)
    logger.info('loglevel is: {}'.format(logging.getLevelName(logger.getEffectiveLevel())))

    try:
        logger.info('starting up...')
        application.run(host=args.listen, port=args.listen_port, debug=args.debug, threaded=True)
    except KeyboardInterrupt:
        logger.info('shutting down...')
        raise SystemExit


if __name__ == "__main__":
    main()
