from flask_restplus import fields
from libs.restplus import api_restplus

model_payload = api_restplus.model('model_payload', {
    'word': fields.String(description='word'),
})