from flask import Flask, jsonify, request
from db_operations import FlightOperations as FlightOprs, Flight

flights = FlightOprs()
flights.create_database()
flights.create_table()

app = Flask(__name__)

# ------------------------
# Create Flight
# ------------------------
@app.route('/flights', methods=['POST'])
def flights_create():
    body = request.get_json()
    new_flight = Flight(
        body['airline'],
        body['source'],
        body['destination'],
        body['fare'],
        body['duration']
    )
    print(new_flight)
    id = flights.insert_row(new_flight)
    flight = flights.search_row(id)
    flight_dict = {
        'id': flight[0],
        'airline': flight[1],
        'source': flight[2],
        'destination': flight[3],
        'fare': flight[4],
        'duration': flight[5]
    }
    return jsonify(flight_dict)

# ------------------------
# Read Flight by ID
# ------------------------
@app.route('/flights/<id>', methods=['GET'])
def flights_read_by_id(id):
    flight = flights.search_row(id)
    if flight is None:
        return jsonify({"message": "Flight not found"})
    flight_dict = {
        'id': flight[0],
        'airline': flight[1],
        'source': flight[2],
        'destination': flight[3],
        'fare': flight[4],
        'duration': flight[5]
    }
    return jsonify(flight_dict)

# ------------------------
# Read All Flights
# ------------------------
@app.route('/flights', methods=['GET'])
def flights_read_all():
    flights_list = flights.list_all_rows()
    flights_dict = []
    for flight in flights_list:
        flights_dict.append({
            'id': flight[0],
            'airline': flight[1],
            'source': flight[2],
            'destination': flight[3],
            'fare': flight[4],
            'duration': flight[5]
        })
    return jsonify(flights_dict)

# ------------------------
# Update Flight
# ------------------------
@app.route('/flights/<id>', methods=['PUT'])
def flights_update(id):
    body = request.get_json()
    old_flight_obj = flights.search_row(id)
    if not old_flight_obj:
        return jsonify({'message': 'Flight not found'})

    updated_flight_obj = []
    updated_flight_obj.append(body['airline'])
    updated_flight_obj.append(body['source'])
    updated_flight_obj.append(body['destination'])
    updated_flight_obj.append(body['fare'])
    updated_flight_obj.append(body['duration'])
    updated_flight_obj.append(id)  # for WHERE id = ?
    updated_flight_obj = tuple(updated_flight_obj)

    flights.update_row(updated_flight_obj)

    flight = flights.search_row(id)
    flight_dict = {
        'id': flight[0],
        'airline': flight[1],
        'source': flight[2],
        'destination': flight[3],
        'fare': flight[4],
        'duration': flight[5]
    }
    return jsonify(flight_dict)

# ------------------------
# Delete Flight
# ------------------------
@app.route('/flights/<id>', methods=['DELETE'])
def flights_delete(id):
    old_flight_obj = flights.search_row(id)
    if not old_flight_obj:
        return jsonify({'message': 'Flight not found', 'is_error': 1})
    flights.delete_row(id)
    return jsonify({'message': 'Flight is deleted', 'is_error': 0})

if __name__ == '__main__':
    app.run(debug=True)
