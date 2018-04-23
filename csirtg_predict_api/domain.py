from flask_restplus import Namespace, Resource, reqparse
from csirtg_domainsml import predict
from .whitelist import lookup as is_whitelisted

api = Namespace('domain', description='Domain related operations')


@api.route('/')
@api.response(200, 'OK')
class Domain(Resource):
    @api.param('q', 'Test a FQDN')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q')
        args = parser.parse_args()

        if is_whitelisted(args.q):
            p = 0

        else:
            p = predict(args.q)

        return {'data': str(p)}
