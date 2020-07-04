from flask.json import JSONEncoder
from datetime import date
from bson import ObjectId
import decimal


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            
            if isinstance(obj, decimal.Decimal):
                return (str(obj) for obj in [obj])
  
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
