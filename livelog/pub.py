import time,json
from datetime import datetime
from decimal import Decimal


class JsonCustomSerializer(json.JSONEncoder):

    def default(self, field):

        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(field, Decimal):
            return str(field)

        else:
            return json.JSONEncoder.default(self,field)