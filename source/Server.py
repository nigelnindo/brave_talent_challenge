from flask import Flask, jsonify, make_response, request

from Extractor import get_number_plate
from PlateCounter import count_plates

app = Flask(__name__)


@app.route('/api/extractor', methods=['GET'])
def extractor():
    sentence = request.args.get('sentence')
    if sentence is not None:
        return jsonify({'result': get_number_plate(sentence)})
    return jsonify({'error': "supply 'sentence' query parameter"})


@app.route('/api/difference', methods=['GET'])
def difference():
    first = request.args.get('firstPlate')
    second = request.args.get('secondPlate')
    if first is None or second is None:
        return jsonify({'error': "supply both 'firstPlate' & 'secondPlate' query parameters"})
    return jsonify({'result': count_plates(first, second)})


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
