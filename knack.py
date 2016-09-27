from urllib import urlencode

import requests
from slugify import slugify

class Knack(object):
    endpoint = 'https://api.knack.com/v1'
    resource = ''

    def __init__(self, **kwargs):
        self.headers = {
            'X-Knack-REST-API-Key': 'knack',
            'X-Knack-Application-Id': kwargs['application_id']
        }

    def scenes(self, scene_id):
        self.resource += '/scenes'
        if scene_id:
            self.resource += '/scene_' + scene_id
        return self

    def views(self, view_id):
        self.resource += '/views'
        if view_id:
            self.resource += '/view_' + view_id
        return self

    def records(self, record_id=''):
        self.resource += '/records'
        if record_id:
            self.resource += '/' + record_id
        return self

    def fields(self):
        self.resource += '/fields'
        return self

    def fetch(self, qs={}):
        uri = self.endpoint + self.resource

        if format not in qs: # allow user override
            qs['format'] = 'raw'

        uri += '?' + urlencode(qs)

        # Reset state
        self.resource = ''

        response = requests.get(uri, headers=self.headers)
        return response.json()

    def map_fields(self, data, fields):
        """ Create new data dict using field labels """
        mapped_data = {}

        field_map = {field['key']: slugify(field['label'], separator='_')
                        for field in fields['fields']}

        for key, value in data.iteritems():
            key_unraw = key.rstrip('_raw')

            if key in field_map:
                mapped_key = field_map[key]
                mapped_data[mapped_key] = value
            elif key_unraw in field_map:
                mapped_key_raw = field_map[key_unraw] + '_raw'
                mapped_data[mapped_key_raw] = value
            else:
                mapped_data[key] = value

        return mapped_data
