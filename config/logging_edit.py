import json_log_formatter
import datetime
from pythonjsonlogger import jsonlogger

class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        extra['message'] = message
        extra['levelname'] = record.__dict__['levelname']
        extra['name'] = record.__dict__['name']
        extra['lineno'] = record.__dict__['lineno']
        extra['filename'] = record.__dict__['filename']
        extra['pathname'] = record.__dict__['pathname']
        extra['created'] = record.__dict__['created']
        request = extra.pop('request', None)
        if request:
            extra['x_forward_for'] = request.META.get('X-FORWARD-FOR')
        return extra

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(
            log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname