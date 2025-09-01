from flask import Flask, jsonify, request
from db_operations import PersonOperations as PersonOprs, Person

persons = PersonOprs()
persons.create_database()
persons.create_table()

app = Flask(__name__)

# ------------------------
# Create Person
# ------------------------
@app.route('/persons', methods=['POST'])
def persons_create():
    body = request.get_json()
    new_person = Person(
        body['name'],
        body['gender'],
        body['age'],
        body['location']
    )
    print(new_person)
    id = persons.insert_row(new_person)
    person = persons.search_row(id)
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'age': person[3],
        'location': person[4]
    }
    return jsonify(person_dict)

# ------------------------
# Read Person by ID
# ------------------------
@app.route('/persons/<id>', methods=['GET'])
def persons_read_by_id(id):
    person = persons.search_row(id)
    if person is None:
        return jsonify({"message": "Person not found"})
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'age': person[3],
        'location': person[4]
    }
    return jsonify(person_dict)

# ------------------------
# Read All Persons
# ------------------------
@app.route('/persons', methods=['GET'])
def persons_read_all():
    persons_list = persons.list_all_rows()
    persons_dict = []
    for person in persons_list:
        persons_dict.append({
            'id': person[0],
            'name': person[1],
            'gender': person[2],
            'age': person[3],
            'location': person[4]
        })
    return jsonify(persons_dict)

# ------------------------
# Update Person
# ------------------------
@app.route('/persons/<id>', methods=['PUT'])
def persons_update(id):
    body = request.get_json()
    old_person_obj = persons.search_row(id)
    if not old_person_obj:
        return jsonify({'message': 'Person not found'})

    updated_person_obj = []
    updated_person_obj.append(body['name'])
    updated_person_obj.append(body['gender'])
    updated_person_obj.append(body['age'])
    updated_person_obj.append(body['location'])
    updated_person_obj.append(id)  # last for WHERE id = ?
    updated_person_obj = tuple(updated_person_obj)

    persons.update_row(updated_person_obj)

    person = persons.search_row(id)
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'age': person[3],
        'location': person[4]
    }
    return jsonify(person_dict)

# ------------------------
# Delete Person
# ------------------------
@app.route('/persons/<id>', methods=['DELETE'])
def persons_delete(id):
    old_person_obj = persons.search_row(id)
    if not old_person_obj:
        return jsonify({'message': 'Person not found', 'is_error': 1})
    persons.delete_row(id)
    return jsonify({'message': 'Person is deleted', 'is_error': 0})

if __name__ == '__main__':
    app.run(debug=True)