from flask import jsonify
from marshmallow import validate

from app import app
from fib.fibonacci import get_fibonacci_range_sequence
from webargs import fields
from webargs.flaskparser import use_args

args_map = {
    'from': fields.Int(required=True, validate=[validate.Range(min=1)]),
    'to': fields.Int(required=True, validate=[validate.Range(min=1)])
}


@app.route('/fibonacci', methods=['GET'])
@use_args(args_map, location='query')
def get_fibonacci(args):
    """ Sending the fib sequence to user by JSON """

    return jsonify(sequence=get_fibonacci_range_sequence(args['from'], args['to']))
