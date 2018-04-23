from flask_restplus import Namespace, Resource, fields, reqparse
from flask import session, request

import pyzmail
import re

from csirtg_mail.urls import extract_urls as extract_urls
from csirtg_mail.urls import extract_email_addresses
from csirtg_urlsml import predict

api = Namespace('email', description='Email message related operations')

RE_FWD = re.compile('\^(FWD?|Fwd?):')


def parse_headers(message):
    keys = message.keys()
    values = message.values()
    headers = {}

    for k, v in zip(keys, values):
        headers.setdefault(k.lower(), []).append(v)

    return headers

# https://stackoverflow.com/questions/2168719/parsing-forwarded-emails
# https://github.com/zapier/email-reply-parser
# https://en.wikipedia.org/wiki/Email_forwarding
# https://en.wikipedia.org/wiki/List_of_email_subject_abbreviations


def is_redirect(message):
    assert isinstance(message, pyzmail.PyzMessage)

    headers = parse_headers(message)

    if headers['resent-to'][0]:
        return True

    if headers['x-envelope-to'][0]:
        return True

    return False


def is_fwd(message):
    assert isinstance(message, pyzmail.PyzMessage)

    headers = parse_headers(message)

    if RE_FWD.match(headers['subject'][0]):
        return True

    if headers.get('x-forwarded-message-id'):
        return True

    # no subject, but attachment
    ## either .eml or [.docx?|.zip|.html?]

    return is_redirect(message)


resource_fields = api.model('Resource', {
    'email': fields.Arbitrary,
})


@api.route('/')
@api.response(200, 'OK')
class Email(Resource):
    @api.expect(resource_fields)
    def post(self):
        data = request.data
        message = pyzmail.PyzMessage.factory(data)
        headers = parse_headers(message)

        # for mailpart in message.mailparts:
        #     print '    %sfilename=%r alt_filename=%r type=%s charset=%s desc=%s size=%d' % ( \
        #         '*' if mailpart.is_body else ' ', \
        #         mailpart.filename, \
        #         mailpart.sanitized_filename, \
        #         mailpart.type, \
        #         mailpart.charset, \
        #         mailpart.part.get('Content-Description'), \
        #         len(mailpart.get_payload()))
        #
        #     if mailpart.type.startswith('text/'):
        #         # display first line of the text
        #         payload, used_charset = pyzmail.decode_text(mailpart.get_payload(), mailpart.charset, None)
        #         print '        >', payload.split('\\n')[0]

        # is fwd

        ## inline
        ## attachment is .eml
        ## is html
        ## is txt
        ## attachment is [.docx?|.zip|.html?|.xlsx?]
        ## multiple .eml attachments
        ## is html
        ## is txt

        if message.html_part:
            body = message.html_part.get_payload()
            urls = extract_urls(body, html=True)
            email_addresses = extract_email_addresses(body, html=True)
        else:
            if message.text_part:
                body = message.text_part.get_payload()
                urls = extract_urls(body)
                email_addresses = extract_email_addresses(body)
            else:
                from pprint import pprint
                pprint(message)
                return api.abort(422)

        return {
            'message': body.decode('utf-8'),
            'urls': list(urls),
            'email_addresses': list(email_addresses),
            'headers': headers
        }