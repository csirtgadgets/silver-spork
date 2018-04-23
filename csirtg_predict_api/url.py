from flask_restplus import Namespace, Resource, fields, reqparse
from urllib.parse import urlparse
import os, re

from csirtg_urlsml import predict
from .whitelist import lookup as is_whitelisted

api = Namespace('url', description='URL related operations')

RE_IMAGES = re.compile(r'.[png|jpg]$')

me = os.path.dirname(__file__)


@api.route('/')
@api.response(200, 'OK')
class Url(Resource):
    @api.param('q', 'Test a URL')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q')
        args = parser.parse_args()

        images = args.get('images', False)

        u = urlparse(args.q)
        if is_whitelisted(u.netloc):
            p = 0

        elif not images and RE_IMAGES.search(u.geturl()):
            p = 0

        else:
            p = predict(u.geturl())

        return {'data': str(p)}
