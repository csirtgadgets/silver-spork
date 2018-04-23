from flask_restplus import Namespace, Resource, reqparse
from csirtg_ipsml import predict
import arrow

api = Namespace('ip', description='IP related operations')


@api.route('/')
@api.response(200, 'OK')
class IP(Resource):
    @api.param('q', 'Test an IP Address [q=ip,hour]')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q')
        args = parser.parse_args()

        q = args.q
        ts = arrow.utcnow().hour
        if ',' in q:
            q, ts = q.split(',')

        p = predict(q, ts)

        return {'data': str(p)}
